import json
import logging
import sys
import hw2_lambda2

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))


event = {
}

results = lambda_function_2.lambda_handler(event, context={})
print("HTTP STATUS  = {}".format(results.get('statusCode')))
print('RESULTS={}'.format(json.dumps(results, indent=2, sort_keys=False)))