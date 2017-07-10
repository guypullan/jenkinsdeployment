#!python

def componentcreation(wrapperfile, variablelist, certificate, certkey):

    import requests
    import json

    cert_file_path = certificate
    key_file_path = certkey

    url = "https://api.live.bbc.co.uk/cosmos/components/create"
    #url = "https://httpbin.org/post"

    # cosmos url and json headers
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    # read wrapper file (contains template of full request to be sent to cosmos)
    with open (wrapperfile) as myfile:
        wrapper = myfile.read()

    with open (variablelist) as myfile:
        device_valuesfromfile = json.load(myfile)

    for key,val in device_valuesfromfile.items():
        wrapper = wrapper.replace(key,val)

    certificate = (cert_file_path, key_file_path)

    # send request to cosmos to create new Component
    r = requests.post(url, data=(wrapper), cert=certificate, headers=headers)
    print r.content
