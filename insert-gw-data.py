#Author: Kehinde Otubamowo
#Email: otubamk@amazon.com
#Generate randon game week team selections for gamers


import boto3
import string
import random
import time
from datetime import datetime

print("Starting...")


start_time = time.time()

dt_object = datetime.fromtimestamp(start_time)

print(dt_object)


# Get the service resource.
dynamodb = boto3.resource('dynamodb')


# Instantiate a table resource object without actually
# creating a DynamoDB table. Note that the attributes of this table
# are lazy-loaded: a request is not made nor are the attribute
# values populated until the attributes
# on the table resource are accessed or its load() method is called.


Gamers_Table = dynamodb.Table('Gamers')

Game_Week_Table = dynamodb.Table('Gamer_Teams')

Soccer_Players_Table = dynamodb.Table('Soccer_Players')


response = Soccer_Players_Table.scan()

players = response['Items']

goalkeepers = [player for player in players if player["Player_Profile"]["Position"] == "Goalie"]

outfeild_players = [player for player in players if not player["Player_Profile"]["Position"] == "Goalie"]

#response = Gamers_Table.scan()
#gamers = response['Items']
#gamer_ids = [gamer for gamer in gamers]

scan_kwargs = {
        'ProjectionExpression': "Gamer_ID",
    }


x=1

done = False

start_key = None

n = input("Enter Game Week you want to instantiate: ")

type(n)

if int(n) <= 9:
    GWStr="GW-0"+ n
else:
    GWStr="GW-"+ n

with Game_Week_Table.batch_writer() as batch:
    while not done:
        if start_key:
            scan_kwargs['ExclusiveStartKey'] = start_key
        response = Gamers_Table.scan(**scan_kwargs)
        gamers = response['Items']
        gamer_ids = [gamer for gamer in gamers]
        for gamer_id in gamer_ids:
            item = {}
            item['Gamer_ID'] = gamer_id['Gamer_ID']
            item['Game_Week'] = GWStr
            item["GW_Team"] = {}
            #print(item['Gamer_ID']," ",x)
            player_list = []
            temp_non_goalkeepers = outfeild_players[:]
            goalkeeper = random.choice(goalkeepers)["Player_ID"]

    
            for i in range(4):
                player = random.choice(temp_non_goalkeepers)["Player_ID"]
                temp_non_goalkeepers = [non_goalkeeper for non_goalkeeper in temp_non_goalkeepers if not non_goalkeeper["Player_ID"] == player]
                player_list.append(player)
        
            item["GW_Team"]["Captain"] = player_list[0]
            player_list.append(goalkeeper)
 

            item["GW_Team"]["GoalKeeper"] = goalkeeper
            item["GW_Team"]["Players"] = player_list
    
    
            player_list = []
    
            for i in range(2):
                player = random.choice(temp_non_goalkeepers)["Player_ID"]
                temp_non_goalkeepers = [non_goalkeeper for non_goalkeeper in temp_non_goalkeepers if not non_goalkeeper["Player_ID"] == player]
                player_list.append(player)
            
            
            item["GW_Team"]["Subs"] = player_list
            #batch.put_item(Item=item)
        
        
            try:
                batch.put_item(Item=item)
            except:
                print(item['Gamer_ID'], item['Game_Week'], " already exists")
            else:
                print(item['Gamer_ID']," ",item['Game_Week']," ",x)
                x+=1
                
        start_key = response.get('LastEvaluatedKey', None)
        done = start_key is None
    
    
    
print(" ")

print("--- Summary ---")

print(GWStr, "Teams initialized for",x,"Gamers")

print("Runtime","%s seconds" % (time.time() - start_time))