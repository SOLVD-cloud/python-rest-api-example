# this function will authenticate with Salesforce and authorize a user
# the return for this function is the authentication token

def authorize_salesforce(client_id, username):
    import requests
    import jwt
    import time

    # opening the private key file
    with open("./cert/private-key.pem") as fd:
        private_key = fd.read()

    payload = {
        "iss": client_id,
        "exp": int(time.time()) + 300,
        "aud": "https://login.salesforce.com",
        "sub": username,
    }

    encoded_token = jwt.encode(
        payload, private_key, algorithm="RS256", headers={"alg": "RS256"}
    )

    response = requests.post(
        "https://login.salesforce.com/services/oauth2/token",
        data={
            "assertion": encoded_token,
            "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        },
    )

    json_repsonse = response.json()

    print(f"STATUS : {response.status_code}")
    print(json_repsonse)

    return json_repsonse["access_token"]
