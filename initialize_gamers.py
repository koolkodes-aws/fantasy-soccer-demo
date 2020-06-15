#Author: Kehinde Otubamowo
#Email: otubamk@amazon.com
#Instantiate random gamers that will play the fantasy league game


# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + #
#                                                                                                                                                               #
#   Fantasy football or fantasy soccer is a game in which participants assemble an imaginary team of real life footballers and score points                     #
#   based on those players' actual statistical performance or their perceived contribution on the field of play.                                                #                                                       #        
#                                                                                                                                                               #
#   Fantasy games are very popular, with most variants having millions of players worldwide.                                                                    #
#   In fantasy soccer, points are then gained or deducted depending on players' performances each game week.                                                    #
#   Points systems vary between games, but points are typically awarded for achievements like scoring a goal, earning an assist or keeping a clean sheetself.   #                                                                                     #
#                                                                                                                                                               #
#   For the purpose of this demo, teams will consist of 7 players, a typical selection would include 1 goalkeeper, 4 outfield players and 2 substitutes.        #
#   We will also assign random points to each game player each game week.                                                                                       #
#                                                                                                                                                               #
#   To model this game, we used three tables; Gamers, Soccer_Players and Gamer_Teams. Gamers table stores information about gamers playing the game.            #
#   Soccer_Players table contains information about soccer players that can be selected by gamers each gameweek.                                                #
#                                                                                                                                                               #
#   Finally, we will store teams selected by each gamer in the Gamer_Teams table.                                                                               #
#                                                                                                                                                               #
# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + #


import boto3
import string
import random
import time
from datetime import datetime

print("Starting...")

start_time = time.time()

dt_object = datetime.fromtimestamp(start_time)

print(dt_object)


dynamodb = boto3.resource('dynamodb')

Gamers_Table = dynamodb.Table('Gamers')

Country_List=["USA","Canada","India","Brazil","India","Nigeria","South Africa","UK"]

Char1 = string.ascii_uppercase

Char2 = string.ascii_lowercase

Char3 = string.digits

x=0
n=0

n = input("Enter amount of gamers you want to instantiate: ")

type(n)


with Gamers_Table.batch_writer() as batch:
    for i in range(int(n)):
        item = {}
        item['Gamer_ID'] = ''.join(random.choice(Char1) for i in range(1) ) + ''.join(random.choice(Char2) for i in range(4)) +''.join(random.choice(Char3) for i in range(5))
        item['Gamer_Details'] = {}
        item['Gamer_Details']['Country'] = random.choice(Country_List)
        item['Gamer_Details']['Age'] = random.randint(18, 65)
        x+=1
        player_list = []
        try:
            batch.put_item(Item=item)
        except:
            print("Something went wrong, check Gamers Table")
        else:
            print("Gamer", item['Gamer_ID'],"from",item['Gamer_Details']['Country'],"initialized")
            
            
print(" ")

print("--- Summary ---")

print(x, "gamers initialized")

print("Runtime","%s seconds" % (time.time() - start_time))