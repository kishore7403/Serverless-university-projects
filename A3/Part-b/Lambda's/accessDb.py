import boto3            # [1]
import json             # [2]

def lambda_handler(event, context):
    s3 = boto3.client('s3')         # [3]
    dynamodb = boto3.client('dynamodb')  # [3]


    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']

 
    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    file_content = response['Body'].read().decode('utf-8')

    data = json.loads(file_content)         #[1]


    for key, value in data.items():
        for entity, count in value.items():
            dynamodb.put_item(              #[4]
                TableName='outputTable',
                Item={
                    'key': {'S': entity},
                    'value': {'S': str(count)}
                }
            )
    print("sucsess - "+str(file_key))
    return 'DynamoDB table updated successfully'

# References
# [1] Amazon Web Services, Inc, "Boto3 documentation," Amazon Web Services, Inc, 2023. [Online]. Available: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html. [Accessed 20 July 2023].
# [2] Python Software Foundation, "json," Python Software Foundation, 2023. [Online]. Available: https://docs.python.org/3/library/json.html. [Accessed 20 Kuly 2023].
# [3] Amazon Web Services, Inc, "Client," Amazon Web Services, Inc, 2023. [Online]. Available: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html. [Accessed 23 July 2023].
# [4] Amazon Web Services, Inc, "put_item," Amazon Web Services, Inc, 2023. [Online]. Available: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/put_item.html. [Accessed 20 July 2023].