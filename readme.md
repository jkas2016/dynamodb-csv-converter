# Dynamodb-csv-converter

## Description

This is a simple tool to convert a csv to dynamodb and vice versa.

## Usage

```bash
python3 dynamodb_to_csv.py
python3 csv_to_dynamodb.py
```

## Example

```python
# csv_to_dynamodb.py
import boto3
import csv

def csv_to_dynamodb():
    # Replace <YOUR-PROFILE-NAME>, <YOUR-REGION-NAME>, and <YOUR-TABLE-NAME> with your values
    session = boto3.Session(profile_name='<YOUR-PROFILE-NAME>', region_name='<YOUR-REGION-NAME>')
    dynamodb = session.resource('dynamodb')
    table = dynamodb.Table('<YOUR-TABLE-NAME>')

    # Replace <FILE-NAME> with your file name
    with open('<FILE-NAME>.csv', 'r') as data:
        next(data)  # Skip the header
        reader = csv.reader(data)
        for row in reader:
            item = {
                'id': row[0],  # Replace this with your table's primary key column name
                'value': row[1] if row[1] and row[1].strip() else None,
            }
            table.put_item(Item=item)
```