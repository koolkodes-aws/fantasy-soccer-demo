#Author: Kehinde Otubamowo
#Email: otubamk@amazon.com
#Generate random points for soccer players


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

if int(n) <= 9:
    GWStr="GW-0"+ n
else:
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