# fantasy-soccer-demo

This code creates sample data for a mini fantasy soccer game.

For the purpose of this demo, teams will consist of 7 players, a typical selection would include 1 goalkeeper, 4 outfield players and 2 substitutes. We will also assign random points to each game player each game week. To model this game, we used three tables; Gamers, Soccer_Players and Gamer_Teams. 

Gamers table stores information about gamers playing the game. Soccer_Players table contains information about soccer players that can be selected by gamers each gameweek. Finally, we will store teams selected by each gamer in the Gamer_Teams table. 

## Prequisites:
1. Python
2. AWS Console / CLI

Before running the code below, please follow these steps to setup your workspace if you have not set it up already:

1. Setup credentials for DynamoDB access. One of the ways to setup credentials is to add them to ~/.aws/credentials file (C:\Users\USER_NAME\.aws\credentials file for Windows users) in following format:

```python
#    [<profile_name>]
#    aws_access_key_id = YOUR_ACCESS_KEY_ID
#    aws_secret_access_key = YOUR_SECRET_ACCESS_KEY
```
If <profile_name> is specified as "default" then AWS SDKs and CLI will be able to read the credentials without any additional configuration. But if a different profile name is used then it needs to be specified while initializing DynamoDB client via AWS SDKs or while configuring AWS CLI. 

Please refer following guide for more details on credential configuration: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration

2. Install the latest Boto 3 release via pip:
```bash
pip install boto3
```

Please refer following guide for more details on Boto 3 installation: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation

Please note that you may need to follow additional setup steps for using Boto 3 from an IDE. Refer your IDE's documentation if you run into issues.

## Steps to generate sample data:
1. Import json file - "fantasy-soccer-data-model.josn" to NoSQL Workbench.

2. Commit data model to DynamoDB.
!(workbench-screen-shot.jpg)

3. Initialize game players (Input: number of gamers)
```bash
python3 initialize_gamers.py
```

4. Insert gameweek points for soccer players (Input: specify game week) 
```bash
python3 soccer-players-weekly-update.py
```

5. Insert gameweek team selections for gamers: (Input: specify game week)
```bash
python3 insert-gw-data.py
```
