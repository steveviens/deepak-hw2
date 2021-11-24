import boto3
import json
import logging

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

            # TODO: GET THE 'USER-SUPPLIED' LABELS FROM HTTP HEADER

            # TODO: ADD USER-SUPPLIED & REKOGNITION-DERIVED LABELS TO OPEN SEARCH INDEX HERE

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
