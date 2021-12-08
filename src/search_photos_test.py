import json
import logging
import sys
import search_photos_function

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))


event = {
}

results = search_photos_function.lambda_handler(event, context={})
print("HTTP STATUS  = {}".format(results.get('statusCode')))
print('RESULTS={}'.format(json.dumps(results, indent=2, sort_keys=False)))
