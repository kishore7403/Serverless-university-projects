import json                                     # [1]
import boto3                                    # [2]

def lambda_handler(event, context):
    queue_url = 'https://sqs.us-east-1.amazonaws.com/572897718615/CarDetail'
    sns_topic_arn = 'arn:aws:sns:us-east-1:572897718615:HalifaxTaxi-EmailService'
    dynamodb_table_name = 'EmailMessagesTable'
    sqs_client = boto3.client('sqs')            #[2] 
    sns_client = boto3.client('sns')            #[2]
    dynamodb_client = boto3.client('dynamodb')  #[2]
    
    response = sqs_client.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=10, 
        WaitTimeSeconds=20
    )
    for message in response.get('Messages', []):
        message_body = message['Body']
        print("Received Message:", message_body)
        
        message_json = json.loads(message_body)     #[1]
        message_content = json.loads(message_json['Message'])  # Parse the Message JSON [1]
        
        message_email = 'Your order for {} with {} at {} is confirmed.'.format(
            message_content['cartype'],
            message_content['carAccessory'],
            message_content['streetAddress']  
        )
        sns_client.publish(                     #[3]
            TopicArn=sns_topic_arn,
            Message=message_email 
        )

        message_id = message_json['MessageId']
        item = {
            'MessageID': {'S': message_id},
            'MessageContent': {'S': message_email}
        }
        dynamodb_client.put_item(               #[4]
            TableName=dynamodb_table_name,
            Item=item
        )
        
        receipt_handle = message['ReceiptHandle']
        sqs_client.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=receipt_handle
        )
 
    return {
        'statusCode': 200,
        'body': json.dumps('Email')
    }
# References
# [1] Python Software Foundation, "json," Python Software Foundation, 2023. [Online]. Available: https://docs.python.org/3/library/json.html. [Accessed 20 Kuly 2023].
# [2] Amazon Web Services, Inc, "Boto3 documentation," Amazon Web Services, Inc, 2023. [Online]. Available: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html. [Accessed 20 July 2023].
# [3]Amazon Web Services, Inc., "Publish," Amazon Web Services, Inc., 2023. [Online]. Available: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/client/publish.html. [Accessed 20 July 2023].
# [4] Amazon Web Services, Inc. , "Put an item in a DynamoDB table using an AWS SDK," Amazon Web Services, Inc. , 2023. [Online]. Available: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_PutItem_section.html. [Accessed 20 July 2023].