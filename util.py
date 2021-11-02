#
#  Copyright 2020-2021 Viens Consulting, LLC. All Rights Reserved.
#

import json
import datetime
from datetime import datetime


# Utility functions
def converter(obj):
    if isinstance(obj, datetime):
        return obj.__str__()


def prettyprint(jsonObj):
    print('{}'.format(json.dumps(jsonObj, indent=2, sort_keys=False, default=converter)))


def timestamp():
    now = datetime.now()  # current date and time
    return now.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]
