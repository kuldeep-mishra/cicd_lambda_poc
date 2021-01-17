import json
import os
import boto3
import datetime

def lambda_handler(event, context):

    print("TEST CI/CD")  
    print("Testing Webhook 2")
    print("hi from GHE test ")
    print("test code pipeline ")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda using CICD!')
    }
