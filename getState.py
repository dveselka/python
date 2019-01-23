import requests
import os
import sys
import json
from pprint import pprint

failed = False

def getAppState(hostName, serverName):

    global failed

    print ("serverName=" + serverName)
    print ('--------------------------------------------------------------------')

    url = 'https://' + hostName + ':7001/management/weblogic/latest/domainRuntime/serverRuntimes/' + serverName + '/applicationRuntimes'

    os.environ['no_proxy'] = hostName
    os.environ['PYTHONWARNINGS'] = "ignore:Unverified HTTPS request"


    headers = {
        'Accept': 'application/json',
        'X-Requested-By': 'MyClient',
    }

    params = (
        ('links', 'none'),
    )

    response = requests.get(url, headers=headers, params=params, auth=AUTH, verify=False)

    data = response.json()

    if data:
        for key,value in data.items():
            # print(key, '=', value)
            for app in value:
                print (app['applicationName'] + ".state=" +  app['healthState']['state'])
                if app['healthState']['state'] != 'ok':
                    print ("NOT OK")
                    sys.exit(1)
        print ('--------------------------------------------------------------------')
    else:
        print ("Server " + serverName + " not running")
        print ('--------------------------------------------------------------------')


def getDeploymentState(hostName):

    global failed

    url = 'https://' + hostName + ':7001/management/tenant-monitoring/applications'

    print ("Get deplyemnt state =" + url)

    print ('--------------------------------------------------------------------')

    os.environ['no_proxy'] = hostName
    os.environ['PYTHONWARNINGS'] = "ignore:Unverified HTTPS request"


    headers = {
        'Accept': 'application/json',
        'X-Requested-By': 'MyClient',
    }

    params = (
        ('links', 'none'),
    )

    response = requests.get(url, headers=headers, params=params, auth=AUTH, verify=False)

    data = response.json()

    if data['body']['items']:
        for key,value in data['body'].items():
            # print(key, '=', value)
            for app in value:
                print (app['name'] + ".state=" +  app['state'])
                if app['state'] == 'STATE_FAILED':
                    print (app['name'] + " NOT OK !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    failed = True
        print ('--------------------------------------------------------------------')
    else:
        print ("Server " + hostName + " not reachable")
        failed = True
        print ('--------------------------------------------------------------------')





WEBLOGIC_USER = 'weblogic'
WEBLOGIC_PASSWORD = os.environ.get('ADMIN_PWD') # set env var  in shell

if not WEBLOGIC_PASSWORD:
    print ("WEBLOGIC_PASSWORD must be provided")
    sys.exit(1)

AUTH = (WEBLOGIC_USER, WEBLOGIC_PASSWORD)

if len(sys.argv)>1:
    WEBLOGIC_HOST=sys.argv[1]
else:
    WEBLOGIC_HOST=os.environ.get('HOSTNAME')

print ("WEBLOGIC_HOST=" + WEBLOGIC_HOST)

getDeploymentState(WEBLOGIC_HOST)

getAppState(WEBLOGIC_HOST, 'AdminServer')

if failed:
    print ("Applications not deployed OK")
    sys.exit(1)

print ("Applications  deployed OK")
