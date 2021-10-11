import requests
import json

# Defining the api-endpoint
url = 'https://api.abuseipdb.com/api/v2/report'

headers = {
'Accept': 'application/json',
'Key': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' #your API Key
}

# String holding parameters to pass in json format
f = open("ip.txt", "r") #location of the IPs file
for x in f:
    ip_val = x.strip()
    print(ip_val)
    params = {
    'ip':ip_val,
    'categories':'22,23', #Change or add port numbers as per your requirements.
    'comment':'SSH login attempts.' #Add a comment to classify the attack type.
    }
    response = requests.request(method='POST', url=url,headers=headers, params=params)
    decodedResponse = json.loads(response.text)
    try:
        with open('results.txt','a+') as wr:
            wr.write(decodedResponse['data']['ipAddress']+","+str(decodedResponse['data']['abuseConfidenceScore'])+"\n")
    except Exception as ec:
        print(str(ec))
        continue
    print(json.dumps(decodedResponse, sort_keys=True, indent=4))
