import json                                     # [1]
import boto3                                    # [2]
import random                                   # [3]

def lambda_handler(event, context):
    
    topic_arn = 'arn:aws:sns:us-east-1:572897718615:HalifaxTaxi-SNS'
    
    CAR = ['Compact', 'Mid-size Sedan', 'SUV', 'Luxury']
    ADDON = ['GPS', 'Camera']
    CLIENT = ["6050 University Avenue","1333 South Park St","1881 Young street","2429 Barrington Stt","1551 Quinpool Road","123 Main Street"]
    
    car_type = random.choice(CAR)               #[3]
    car_accessory = random.choice(ADDON)        #[3]  
    street_address = random.choice(CLIENT)      #[3]
    
    message_dict = {'cartype': car_type,'carAccessory': car_accessory,'streetAddress': street_address}
    
    message_json = json.dumps(message_dict)     #[3]
    
    sns_client = boto3.client('sns')            #[2]
    
    response = sns_client.publish(              #[4]
        TopicArn=topic_arn,
        Message=message_json
    )
    
    
    print(message_json)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Message published') #[1]
    }

# References
# [1] Python Software Foundation, "json," Python Software Foundation, 2023. [Online]. Available: https://docs.python.org/3/library/json.html. [Accessed 20 Kuly 2023].
# [2] Amazon Web Services, Inc, "Boto3 documentation," Amazon Web Services, Inc, 2023. [Online]. Available: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html. [Accessed 20 July 2023].
# [3] Python Software Foundation., "random," Python Software Foundation., 2023. [Online]. Available: https://docs.python.org/3/library/random.html. [Accessed 20 July 2023].
# [4] Amazon Web Services, Inc., "Publish," Amazon Web Services, Inc., 2023. [Online]. Available: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/client/publish.html. [Accessed 20 July 2023].