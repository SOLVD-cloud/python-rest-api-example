# python-rest-api-example

REST API example developed on Python

Small POC of subscribing to Salesforce REST API using Python.

Utilizes the OAuth 2.0 JWT Bearer flow for authenticating to Salesforce.

## Requirements

Python 3
OpenSSL
Access to a Salesforce Org with a Platform Event created

# Setup

Note: The following (at this time) has been tested on a macOS machine. I can't vouch for the Certificate Generation section working on Linux or Windows environments running WSL.

## Certificate Generation

Clone this repo to your local machine
Duplicate ./scripts/generate-certificate.sh.example into ./scripts/generate-certificate.sh
Fill in your correct information in generate-certificate.sh
Run cd scripts/ && chmod +x generate-certificate.sh && cd ..
Generate the certificate: npm run create-cert
Connected App Setup
Example Connected App Setup

## Screen shot of Connected App Setup

![Example Screenshot](/assets/connected-app-screenshot.png)

Set up Connected App with the .crt that was generated via the shell script
Navigate to Setup > Manage Connected Apps > Your newly-created App
Edit the app and switch the App's "Permitted Users" option to Admin approved users are pre-authorized
Create a new Permission Set that allows access to this Connected App
Assign your user to the Permission Set

## Local Config Setup

Duplicate secrets.json.example into secrets.json
Set up the secrets.json according to the information from your Connected App and SFDC instance
Install dependencies pip install -r requirements.txt
Run: python app.py
