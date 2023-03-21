import requests
import re
from datetime import timedelta
from token_generator import generate_token

access_token = generate_token()
if not access_token:
    print("Unable to generate access token. Exiting.")
    exit()
    
user_login = input("Login of the Student: ")  # Replace this with the user you want to target
url = f'https://api.intra.42.fr/v2/users/{user_login}/locations_stats'
headers = {'Authorization': f'Bearer {access_token}'}

# Send the request to the API
response = requests.get(url, headers=headers)

# Check the response status code and print the results or error message
if response.status_code == 200:
    data = response.json()
    total_duration = timedelta()
    for key, value in data.items():
        match = re.match(r'(\d+):(\d+):(\d+(\.\d+)?)', value)
        if match:
            hours, minutes, seconds = int(match.group(1)), int(match.group(2)), float(match.group(3))
            duration = timedelta(hours=hours, minutes=minutes, seconds=seconds)
            total_duration += duration
    total_hours = total_duration.total_seconds() / 3600
    print(f'Total hours spent by {user_login}: {total_hours}')
else:
    print(f'Error: {response.status_code} - {response.text}')
