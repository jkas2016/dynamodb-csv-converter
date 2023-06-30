import boto3
import csv
# from decimal import Decimal


def csv_to_dynamodb():
    session = boto3.Session(profile_name='<YOUR-PROFILE-NAME>', region_name='<YOUR-REGION-NAME>')
    dynamodb = session.resource('dynamodb')
    table = dynamodb.Table('<YOUR-TABLE-NAME>')

    with open('<FILE-NAME>.csv', 'r') as data:
        next(data)  # Skip the header
        reader = csv.reader(data)
        for row in reader:
            item = {
                'id': row[0],  # Replace this with your table's primary key column name
                'value': row[1] if row[1] and row[1].strip() else None,
                # 'value': Decimal(row[1]) if row[1] and row[1].strip() else None,
                # 'value': int(row[1]) if row[1] and row[1].strip() else None,
                # 'value': float(row[1]) if row[1] and row[1].strip() else None,
            }
            table.put_item(Item=item)


csv_to_dynamodb()
