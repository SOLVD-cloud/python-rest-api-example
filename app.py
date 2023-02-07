# this file authorizes a user for a salesforce org as
# specified by the details in your secrets.json file
# and then queries the Account object using the token
# recieved upon authorization

from authorize import Authorize_Salesforce
import requests
import json

# loading in secrets file that contains username, password, etc.
file = open("./cert/secrets.json")
secrets = json.load(file)
token = Authorize_Salesforce()

# make sure you pick an API version that corresponds with your org
response = requests.get(
    f'{secrets["DOMAIN"]}/services/data/v52.0/sobjects/Account',
    headers={"Authorization": "Bearer " + token},
)

print('RESPONSE BODY')
print(response.json())
