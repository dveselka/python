import requests
import os
import sys
import json
from pprint import pprint


def postPerson(hostName):
    url = 'http://' + hostName + ':7001/rdf-rest-api/webresources/persons'

    print ("Post to =" + url)

    print ('--------------------------------------------------------------------')

    os.environ['no_proxy'] = hostName
    os.environ['PYTHONWARNINGS'] = "ignore:Unverified HTTPS request"

    headers = {
        'Accept': 'application/json',
        'X-Requested-By': 'MyClient',
    }

    # data to be sent to api
    data = {'name': 'Person_4',
            'age': 44
            }

    # sending post request and saving response as response object
    response = requests.post(url, data=data)



if len(sys.argv) > 1:
    WEBLOGIC_HOST = sys.argv[1]
else:
    WEBLOGIC_HOST = os.environ.get('HOSTNAME')

print ("WEBLOGIC_HOST=" + WEBLOGIC_HOST)

postPerson(WEBLOGIC_HOST)
