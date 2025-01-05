import requests



base_url = 'http://aes.cryptohack.org/symmetry'



BLOCK_LENGTH = 16



def exploit():

  api_response = requests.get(url=f"{base_url}/encrypt_flag/").json()

  encrypted_message = bytes.fromhex(api_response['ciphertext'])



  # Split the encrypted_message into the initialization_vector and the actual encrypted_message

  initialization_vector, encrypted_message = encrypted_message[:BLOCK_LENGTH], encrypted_message[BLOCK_LENGTH:]



  # Encrypt the encrypted_message (E_K(initialization_vector) ^ FLAG) which just will encrypt the supplied

  # initialization_vector as E_K(initialization_vector) and XOR it with the encrypted_message and recover the flag.

  # Abuses the fact that encryption and decryption perform the same operation in OFB mode.

  api_response = requests.get(url=f"{base_url}/encrypt/{encrypted_message.hex()}/{initialization_vector.hex()}").json()

  decrypted_message = bytes.fromhex(api_response['ciphertext'])

  return decrypted_message.decode()



if __name__ == '__main__':

  secret_code = exploit()

  print(secret_code)