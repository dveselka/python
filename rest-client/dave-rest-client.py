import requests
import os
import sys
import json
from pprint import pprint


def getPerson(hostName):

    url = 'http://' + hostName + ':7001/rdf-rest-api/webresources/persons'

    print ("Get person url=" + url)

    print ('--------------------------------------------------------------------')

    os.environ['no_proxy'] = hostName
    os.environ['PYTHONWARNINGS'] = "ignore:Unverified HTTPS request"


    headers = {
        'Accept': 'application/json',
        'X-Requested-By': 'MyClient',
    }

    params = (
        ('{id}', '1'),
    )

    response = requests.get(url, headers=headers, params=params, verify=False)

    data = response.json()

    print data


if len(sys.argv)>1:
    WEBLOGIC_HOST=sys.argv[1]
else:
    WEBLOGIC_HOST=os.environ.get('HOSTNAME')

print ("WEBLOGIC_HOST=" + WEBLOGIC_HOST)

getPerson(WEBLOGIC_HOST)









