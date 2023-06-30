import boto3
import csv
# from boto3.dynamodb.conditions import Key
from boto3.dynamodb.conditions import Attr


def dynamodb_to_csv():
    session = boto3.Session(profile_name='<YOUR-PROFILE-NAME>', region_name='<YOUR-REGION-NAME>')
    dynamodb = session.resource('dynamodb')
    table = dynamodb.Table('<YOUR-TABLE-NAME>')

    # Fetch items from the table
    response = table.scan(
        # FilterExpression=Key('<YOUR-KEY>').eq(<KEY-VALUE>)
        FilterExpression=Attr('<YOUR-ATTRIBUTE>').eq('<ATTRIBUTE-VALUE>')
    )
    items = response['Items']

    with open('<FILE-NAME>.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["row1", "row2"])
        for item in items:
            writer.writerow([item.get('key1', ''), item.get('key2', '')])


dynamodb_to_csv()
