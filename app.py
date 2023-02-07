from datetime import datetime
import json
import requests
import jwt
import time

# loading in secrets file that contains username, password, etc.
file = open('cert/secrets.json')
secrets = json.load(file)

# opening the private key file
with open('./cert/private-key.pem') as fd:
    private_key = fd.read()

payload = {
    'iss' : secrets['CLIENT_ID'],
    'exp' : int(time.time()) + 300,
    'aud' : secrets['DOMAIN'],
    'sub' : secrets['USERNAME']
}

encoded_token = jwt.encode(payload, private_key, algorithm='RS256',headers={'alg':'RS256'})

response = requests.post(f'{secrets["DOMAIN"]}/services/oauth2/token', data={
    'assertion' : encoded_token,
    'grant_type' : 'urn:ietf:params:oauth:grant-type:jwt-bearer'
})

print(f'STATUS : {response.status_code}')
print(response.json())