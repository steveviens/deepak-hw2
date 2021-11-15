import boto3
import json
import logging
import sys

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):

    # Print formatted JSON event object to log
    logger.info(json.dumps(event, indent=2, sort_keys=False))

    try:

        # Loop through list of record objects
        records = event.get('Records')
        for record in records:

            # Pull S3 bucket name and S3 object key from the record
            bucketName = record['s3']['bucket']['name']
            objectKey = record['s3']['object']['key']

            # Invoke AWS Rekognition with bucketName & S3 objectKey
            rekognition = boto3.client('rekognition')
            labels = rekognition.detect_labels(
                Image={
                    'S3Object': {
                        'Bucket': bucketName,
                        'Name': objectKey,
                    }
                },
                MaxLabels=10,
                MinConfidence=80)

            # Print formatted JSON labels object to log
            logger.info('{}/{}: {}'.format(bucketName, objectKey, json.dumps(labels, indent=2, sort_keys=False)))

        return {
            'statusCode': 200   # Ok
        }

    except Exception as error:

        return {
            'statusCode': 400,  # Bad Request
            'body': error
        }


# TEST DRIVER
logger.addHandler(logging.StreamHandler(sys.stdout))

s3_trigger_event = {
    "Records": [
        {
            "eventVersion": "2.1",
            "eventSource": "aws:s3",
            "awsRegion": "us-east-1",
            "eventTime": "2021-11-15T03:56:39.173Z",
            "eventName": "ObjectCreated:Put",
            "userIdentity": {
                "principalId": "A1BSMQFK02VGJI"
            },
            "requestParameters": {
                "sourceIPAddress": "24.147.242.97"
            },
            "responseElements": {
                "x-amz-request-id": "TRTCGJGHN8CA5YHG",
                "x-amz-id-2": "InAqNu5gmIEJkNdTVDSYUgSUTPN9uctT1QTzp1ASDsMJZ1VWVd4YuqfP/m8P+foirXoNiKMeuR/gZt9SuSsBTYhxzUbq6v7aMyKfeper0lc="
            },
            "s3": {
                "s3SchemaVersion": "1.0",
                "configurationId": "8319f1d6-4213-479b-b4b5-52908863f5f8",
                "bucket": {
                    "name": "assignment2-photos.us-east-1.677126791323",
                    "ownerIdentity": {
                        "principalId": "A1BSMQFK02VGJI"
                    },
                    "arn": "arn:aws:s3:::assignment2-photos.us-east-1.677126791323"
                },
                "object": {
                    "key": "assignment2-photo-3.jpeg",
                    "size": 101996,
                    "eTag": "027ce768d566cc290b247bd1869a05ae",
                    "sequencer": "006191DA7723BDA06F"
                }
            }
        }
    ]
}

results = lambda_handler(s3_trigger_event, context={})
print("HTTP STATUS  = {}".format(results.get('statusCode')))
print('RESULTS={}'.format(json.dumps(results, indent=2, sort_keys=False)))
