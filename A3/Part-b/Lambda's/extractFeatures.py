import re               #[1]
import json             #[2]
import boto3            #[3]

def lambda_handler(event, context):
    s3 = boto3.client('s3')         #[4]
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']

    response = s3.get_object(Bucket=bucket_name, Key=file_key)      #[5]
    text = response['Body'].read().decode('utf-8')

    pattern = r'\b[A-Z][A-Za-z]+\b'
    named_entities = re.findall(pattern, text)

    named_entities_count = {}
    for entity in named_entities:
        named_entities_count[entity] = named_entities_count.get(entity, 0) + 1

    output_dict = {file_key[:-4] + 'ne': named_entities_count}
    output_text = json.dumps(output_dict)

    target_bucket = 'tagsb00934548'
    target_key = file_key[:-4] + 'ne.txt'  
    s3.put_object(Body=output_text, Bucket=target_bucket, Key=target_key)

    print(output_dict)

    return output_text

# References
# [1] Python Software Foundation, "re — Regular expression operations," Python Software Foundation, 2023. [Online]. [Accessed 21 July 2023].
# [2] Python Software Foundation, "json," Python Software Foundation, 2023. [Online]. Available: https://docs.python.org/3/library/json.html. [Accessed 20 Kuly 2023].
# [3] Amazon Web Services, Inc, "Boto3 documentation," Amazon Web Services, Inc, 2023. [Online]. Available: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html. [Accessed 20 July 2023].
# [4] Amazon Web Services, Inc, "Client," Amazon Web Services, Inc, 2023. [Online]. Available: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html. [Accessed 23 July 2023].
# [5] Amazon Web Services, Inc, "get_object," Amazon Web Services, Inc, 2023. [Online]. Available: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_object.html. [Accessed 21 July 2023].