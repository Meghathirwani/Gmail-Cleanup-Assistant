from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import base64

# Define Gmail API scope
SCOPES = ['https://mail.google.com/']

# Authenticate Gmail API with OAuth and save the token to token.json
def authenticate_gmail():
    flow = InstalledAppFlow.from_client_secrets_file(
        r"C:\Users\MEGHA\MeganGmailAIAssistantProject\credentials.json", SCOPES)
        
    # Use run_local_server with a specific port to avoid connection issues
    creds = flow.run_local_server(port=8080)
    
    # Save the token for future use in a token.json file in the same directory
    with open("token.json", "w") as token:
        token.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds)

# Fetch all emails in the Social category from LinkedIn
def fetch_linkedin_social_emails(service):
    # Query for emails in the Social category with "LinkedIn" keyword
    query = "category:social LinkedIn"
    results = service.users().messages().list(userId='me', q=query).execute()
    messages = results.get('messages', [])
    print(f"Found {len(messages)} LinkedIn emails in the Social category.")  # Print the number of emails found
    return messages

# Permanently delete email
def delete_email(service, message_id):
    service.users().messages().delete(userId='me', id=message_id).execute()

# Main function to delete all LinkedIn emails in the Social category
def main():
    # Authenticate and connect to Gmail
    service = authenticate_gmail()
    
    # Fetch LinkedIn emails in the Social category
    linkedin_emails = fetch_linkedin_social_emails(service)
    
    # Permanently delete each email that meets the criteria
    for message in linkedin_emails:
        delete_email(service, message['id'])
        print("Deleted a LinkedIn email from the Social category.")

# Run the main function
if __name__ == "__main__":
    main()
