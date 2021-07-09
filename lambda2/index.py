import json
from test import add

print('Loading function')
print('Jenkins here')
print('new job trigger build')
a = 2
b = 2


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    print("value1 = " + event['key1'])
    result = add(a, b)
    return {
        "statusCode": 200,
        "body": {
            "expression": result,
            "event": event['key1']
        }
    }