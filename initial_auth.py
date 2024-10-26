from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://mail.google.com/']

# Load credentials.json and start authentication flow with offline access
flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
creds = flow.run_local_server(port=8080, access_type='offline', prompt='consent')

# Save the credentials (with the refresh token) to token.json
with open('token.json', 'w') as token:
    token.write(creds.to_json())

print("Token has been saved to token.json")
