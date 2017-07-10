#!python

import requests
import json

cert_file_path = "../../dev.bbc.co.uk.cert"
key_file_path = "../../dev.bbc.co.uk.key"

# cosmos url and json headers
#headers = {'Content-Type: application/json'}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

# read wrapper file (contains template of full request to be sent to cosmos)
with open ("componentwrapper") as myfile:
    wrapper = myfile.read()

# define values for cloudstack formation (these can be moved out as options later)
# the variable infrastructure is forwarding the cloudstack formation to this request
device_values = {
    'XComponentName': 'news-tools-test-jenkins-agents',
    'XProjectName': 'news-devops-toolchain'
}

url = "https://api.live.bbc.co.uk/cosmos/components/create"
#url = "https://httpbin.org/post"

# replace values in wrapper with values as assigned in device_values
for key,val in device_values.items():
    wrapper = wrapper.replace(key,val)

certificate = (cert_file_path, key_file_path)

# send request to cosmos to create new Component
r = requests.post(url, data=(wrapper), cert=certificate, headers=headers)
print r.content
