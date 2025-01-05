import base64
from Crypto.Util.number import long_to_bytes

def decode_value(method, encoded_text):
    if method == 'base64':
        return base64.b64decode(encoded_text).decode()
    elif method == 'bigint':
        return long_to_bytes(int(encoded_text, 16)).decode()
    else:
        raise ValueError(f"Unknown encoding method: {method}")

def receive_json():
    # This function should be implemented to receive JSON data
    pass

for i in range(1, 101):
    message = receive_json()

    # Uncomment for debugging purposes
    # print(f"Question {i}")
    # print(f"Received encoding method: {message['type']}")
    # print(f"Received encoded value: {message['encoded']}")

    answer = {"decoded": decode_value(message["type"], message["encoded"])}

    # Uncomment for debugging purposes
    # print(f"Answer: {answer} \n")