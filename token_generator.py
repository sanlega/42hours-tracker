import requests

def generate_token():
    client_id = 'u-s4t2ud-4a351e097a5c08076de2466ff3a3c25ba5de87435fb74c9eb71c736010ad1566'
    client_secret = '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'
    token_url = 'https://api.intra.42.fr/oauth/token'

    # Set up the request parameters
    data = {'grant_type': 'client_credentials', 'client_id': client_id, 'client_secret': client_secret}

    # Send the request to the token endpoint
    response = requests.post(token_url, data=data)

    # Parse the response and extract the access token
    if response.status_code == 200:
        token = response.json()['access_token']
        return token
    else:
        print(f'Error: {response.status_code} - {response.text}')
        return None

