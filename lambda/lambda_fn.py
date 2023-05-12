import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    bucketName=event["Records"][0]["s3"]["bucket"]["name"]
    fileName=event["Records"][0]["s3"]["object"]["key"]
    
    print(bucketName)
    print(fileName)
    
    glue=boto3.client('glue')
    response=glue.start_job_run(
        JobName='cdc-s3-pyspark',
        Arguments = {
            '--s3_target_path_key':fileName,
            '--s3_target_path_bucket':bucketName
        }
    )
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
