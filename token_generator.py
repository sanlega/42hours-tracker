import requests
import json

def generate_token():
    with open('tokens.json', 'r') as file:
        tokens = json.load(file)

    client_id = tokens['client_id']
    client_secret = tokens['client_secret']
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
