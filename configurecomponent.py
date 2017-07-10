#!python

def componentconfiguration(wrapperfile, variablelist, certificate, certkey):

    import requests
    import json

    cert_file_path = certificate
    key_file_path = certkey

#    print "wrapperfile", wrapperfile
#    print "variablelist", variablelist

    with open (variablelist) as myfile:
        device_valuesfromfile = json.load(myfile)

    with open (wrapperfile) as myfile:
        wrapper = myfile.read()

    for key,val in device_valuesfromfile.items():
        wrapper = wrapper.replace(key,val)

    component_valuesfromfile = {}

    for key,val in device_valuesfromfile.items():
        if "X" not in key :
            component_valuesfromfile.update({key: val})

    # cosmos url and json headers
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    certificate = (cert_file_path, key_file_path)

    for key,val in component_valuesfromfile.items():
        url = "https://api.live.bbc.co.uk/cosmos/env/{XEnvironment}/component/{XComponentName}/configuration/".format(**device_valuesfromfile)
        url = url + key
    #url = "https://httpbin.org/post"

#    print wrapper, certificate, headers, url

    # send request to cosmos to create new Component
    r = requests.post(url, data=(wrapper), cert=certificate, headers=headers)
    print r.content
