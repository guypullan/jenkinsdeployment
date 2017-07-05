#!python

# test code to prove principal from website example
#url = "http://localhost:8080"
#data = {'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}
#headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
#r = requests.post(url, data=json.dumps(data), headers=headers)

import requests
import json

cert_file_path = "../../dev.bbc.co.uk.cert"
key_file_path = "../../dev.bbc.co.uk.key"

# cosmos url and json headers
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

# read wrapper file (contains template of full request to be sent to cosmos)
with open ("wrapper") as myfile:
    wrapper = myfile.read()

# read cloudstack configuration
with open ("infrastructure.json") as myfile:
    infrastructure = myfile.read()

# define values for cloudstack formation (these can be moved out as options later)
# the variable infrastructure is forwarding the cloudstack formation to this request
device_values = {
    'XBastionAccessSecurityGroup': 'sg-acf510d4',
    'XComponentName': 'news-tools-dev-jenkins-agents',
    'Xinfrastructure': infrastructure,
    'XEnvironment': 'int',
    'XImageId': 'ami-badd3ec3',
    'XInstanceType': 't2.micro',
    'XKeyName': 'cosmos',
    'XPrivateSubnets': 'subnet-a914c9ce,subnet-cbcf1482,subnet-8de2fbd5',
    'XProjectName': 'news-devops-toolchain',
    'XScalingMaxInstances': '1',
    'XScalingMinInstances': '1',
    'XSlaveSecurityGroup': 'sg-c5de27bd',
    'XVpcId': 'vpc-f2ee3095',
    'Xcomponent': 'ComponentName',
    'Xstack': 'Environment',
}

url = "https://api.live.bbc.co.uk/cosmos/env/{XEnvironment}/component/{XComponentName}/stacks/create".format(**device_values)

# replace values in wrapper with values as assigned in device_values
for key,val in device_values.items():
    wrapper = wrapper.replace(key,val)

certificate = (cert_file_path, key_file_path)

print url
print wrapper

# send request to cosmos to create new stack
r = requests.post(url, data=json.dumps(wrapper), cert=certificate, headers=headers)
print r
