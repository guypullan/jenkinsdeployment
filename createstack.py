#!python

import requests
import json

def stackcreation (wrapperfile, cloudstackconfigfile, variablelisting, certificate, certkey):
    cert_file_path = certificate
    key_file_path = certkey

    # cosmos url and json headers
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    # read wrapper file (contains template of full request to be sent to cosmos)
    with open (wrapperfile) as myfile:
        wrapper = myfile.read()

    #read cloudstack configuration
    with open (cloudstackconfigfile) as myfile:
        infrastructure = myfile.read()

    with open (variablelisting) as myfile:
        variablelistingoutput = json.load(myfile)

    for key,val in variablelistingoutput.items():
        wrapper = wrapper.replace(key,val)

    infrastructure_dictionary = {
        'Xinfrastructure': infrastructure,
    }

    for key,val in infrastructure_dictionary.items():
        wrapper = wrapper.replace(key,val)

    url = "https://api.live.bbc.co.uk/cosmos/env/{XEnvironment}/component/{XComponentName}/stacks/create".format(**variablelistingoutput)
    #url = "https://httpbin.org/post"

    certificate = (cert_file_path, key_file_path)


    # send request to cosmos to create new stack
#    r = requests.post(url, data=(wrapper), cert=certificate, headers=headers)
#    print r.content
#    print r.status_code

    print wrapper

    exit
