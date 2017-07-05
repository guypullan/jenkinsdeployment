#!python

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
    'XComponentName': 'news-tools-test-jenkins-agents',
    'Xinfrastructure': infrastructure,
    'XEnvironment': 'test',
    'XImageId': 'ami-1a51b763',
    'XInstanceType': 't2.micro',
    'XKeyName': 'cosmos',
    'XPrivateSubnets': 'subnet-a914c9ce,subnet-cbcf1482,subnet-8de2fbd5',
    'XProjectName': 'news-devops-toolchain',
    'XScalingMaxInstances': '1',
    'XScalingMinInstances': '1',
    'XSlaveSecurityGroup': 'sg-04985e7c',
    'XVpcId': 'vpc-f2ee3095',
    'Xaws_account_id': '329802642264',
    'Xaws_region': 'eu-west-1'
#    'Xcomponent': 'ComponentName',
#    'Xstack': 'Environment',
}

url = "https://api.live.bbc.co.uk/cosmos/env/{XEnvironment}/component/{XComponentName}/stacks/create".format(**device_values)
#url = "https://httpbin.org/post"

# replace values in wrapper with values as assigned in device_values
for key,val in device_values.items():
    wrapper = wrapper.replace(key,val)

certificate = (cert_file_path, key_file_path)

print url
#print wrapper

# send request to cosmos to create new stack
r = requests.post(url, data=(wrapper), cert=certificate, headers=headers)

#print r.content
print r.status_code
print r
