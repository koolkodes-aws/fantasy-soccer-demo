# fantasy-soccer-demo

This is code to create sample data for a mini fantasy soccer game.

For the purpose of this demo, teams will consist of 7 players, a typical selection would include 1 goalkeeper, 4 outfield players and 2 substitutes. We will also assign random points to each game player each game week. To model this game, we used three tables; Gamers, Soccer_Players and Gamer_Teams. 

Gamers table stores information about gamers playing the game. Soccer_Players table contains information about soccer players that can be selected by gamers each gameweek. Finally, we will store teams selected by each gamer in the Gamer_Teams table. 

## Prequisites:
1. Python
2. AWS Console / CLI

## Steps to generate sample data:
1. Create table schema in DynamoDB:
```json
{
  "DataModel": [
    {
      "TableName": "Gamer_Teams",
      "KeyAttributes": {
        "PartitionKey": {
          "AttributeName": "Gamer_ID",
          "AttributeType": "S"
        },
        "SortKey": {
          "AttributeName": "Game_Week",
          "AttributeType": "S"
        }
      },
      "NonKeyAttributes": [
        {
          "AttributeName": "GW_Team",
          "AttributeType": "M"
        }
      ]
    },
    {
      "TableName": "Soccer_Players",
      "KeyAttributes": {
        "PartitionKey": {
          "AttributeName": "Player_ID",
          "AttributeType": "S"
        }
      },
      "NonKeyAttributes": [
        {
          "AttributeName": "Player_Profile",
          "AttributeType": "M"
        },
        {
          "AttributeName": "Game_Week_Scores",
          "AttributeType": "M"
        }
      ]
    },
    {
      "TableName": "Gamers",
      "KeyAttributes": {
        "PartitionKey": {
          "AttributeName": "Gamer_ID",
          "AttributeType": "S"
        }
      },
      "NonKeyAttributes": [
        {
          "AttributeName": "Gamer_Details",
          "AttributeType": "M"
        }
      ]
    }
  ]
}
```

2. Initialize game players (Input: number of gamers)
```bash
python3 initialize_gamers.py
```

3. Insert gameweek points for soccer players (Input: specify game week) 
```bash
python3 soccer-players-weekly-update.py
```

4. Insert gameweek team selections for gamers: (Input: specify game week)
```bash
python3 insert-gw-data.py
```
