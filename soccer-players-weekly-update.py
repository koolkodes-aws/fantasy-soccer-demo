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
import json
import time
from datetime import datetime


print("Starting...")

start_time = time.time()

dt_object = datetime.fromtimestamp(start_time)

print(dt_object)


dynamodb = boto3.resource('dynamodb')

Soccer_Players_Table = dynamodb.Table('Soccer_Players')

response = Soccer_Players_Table.scan()

response = Soccer_Players_Table.scan()

players = response['Items']

player_ids = [player for player in players]

n = input("Enter Game Week you want to randomize scores in Soccer Players Table: ")

type(n)

GW=int(n)

GWStr="GW-"+ n


for player_id in player_ids:
    item = {}
    try:
        Soccer_Players_Table.update_item(
            Key={
                'Player_ID': player_id['Player_ID']
            },
            UpdateExpression = "SET Game_Week_Scores.#GW = :number",
            ExpressionAttributeNames = { "#GW" : GWStr },
            ExpressionAttributeValues = { ":number" : random.randint(0, 40) },
            ConditionExpression = "attribute_not_exists(Game_Week_Scores.#GW)"
        )
    except:
        print("Check Soccer Players Table,", GWStr, "score already exists for", player_id['Player_ID'])
    else:
        print(GWStr," score updated for ", player_id['Player_ID'])


            
print(" ")

print("--- Summary ---")

print(GWStr, "scores initialized")

print("Runtime","%s seconds" % (time.time() - start_time))