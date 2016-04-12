import json
import pytz


def lambda_handler(event, context):

    fruit = event['params']["querystring"]['fruit']
    message = '{} is on!'.format(fruit)

    return {
        'message' : message
    }
