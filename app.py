# this file authorizes a user for a salesforce org as
# specified by the details in your secrets.json file
# and then queries the Account object using the token
# recieved upon authorization

from authorize import authorize_salesforce
import requests
import json

# loading in secrets file that contains username, password, etc.
file = open("./cert/secrets.json")
secrets = json.load(file)
token = authorize_salesforce(secrets['CLIENT_ID'],secrets['USERNAME'])

# Note the API version in the URL
url_for_request = f'{secrets["DOMAIN"]}/services/data/v52.0/sobjects/Account'

header_for_request = {
    "Authorization": "Bearer " + token
}

response = requests.get(
    url_for_request,
    headers=header_for_request,
)

print('RESPONSE BODY')
print(response.json())
