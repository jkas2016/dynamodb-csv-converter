import boto3
import csv
# from boto3.dynamodb.conditions import Key
from boto3.dynamodb.conditions import Attr


def dynamodb_to_csv():
    session = boto3.Session(profile_name='<YOUR-PROFILE>', region_name='<YOUR-REGION>')
    dynamodb = session.resource('dynamodb')
    table = dynamodb.Table('<YOUR-TABLE-NAME>')

    # Initialize parameters for scan
    scan_kwargs = {
        # 'FilterExpression': Key('<YOUR-KEY>').eq(<KEY-VALUE>)
        'FilterExpression': Attr('<YOUR-ATTR>').eq('<ATTR-VALUE>')
    }
    done = False
    start_key = None

    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['key1', 'key2'])

        # Loop through pages of the scan response
        while not done:
            if start_key:
                scan_kwargs['ExclusiveStartKey'] = start_key
            response = table.scan(**scan_kwargs)
            items = response.get('Items', [])

            for item in items:
                writer.writerow([item.get('key1', ''), item.get('key2', '')])

            start_key = response.get('LastEvaluatedKey', None)
            done = start_key is None


dynamodb_to_csv()
