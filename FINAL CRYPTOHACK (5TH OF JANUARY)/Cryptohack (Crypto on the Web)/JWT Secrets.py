import requests
import jwt

# Send a request to create a session for the user "Natsec"
session_creation_url = "http://web.cryptohack.org/jwt-secrets/create_session/Natsec"
response = requests.get(session_creation_url)

# Print the raw response from the server
print(response.text)

# Extract the session token from the JSON response
session_token = response.json()["session"]

# Define the secret key used for encoding and decoding JWT tokens
default_secret_key = "secret"

# Decode the token using the secret key and print the result
decoded_token = jwt.decode(session_token, default_secret_key, algorithms=["HS256"])
print(decoded_token)

# Forge a new JWT token with modified claims (username and admin status)
forged_token = jwt.encode({"username": "Natsec", "admin": "True"}, default_secret_key, algorithm="HS256")
print(forged_token)

# Send the forged token to the server for authorization
auth_url = f"http://web.cryptohack.org/jwt-secrets/authorise/{forged_token}"
authorization_response = requests.get(auth_url)

# Print the response from the server after sending the forged token
print(authorization_response.text)
