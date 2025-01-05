import base64

# The input hex data
hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Convert the hex string into a byte array
byte_sequence = bytes.fromhex(hex_string)

# Encode the byte array into a base64 string
encoded_base64 = base64.b64encode(byte_sequence).decode('utf-8')

# Display the base64 encoded result
print(encoded_base64)