from Crypto.Util.strxor import strxor
import requests

# Known header bytes for PNG files (magic bytes + header)
png_magic_header = "89504e470d0a1a0a0000000d49484452"

# Retrieve the encrypted ciphertext from the server
encrypted_content = bytes.fromhex(requests.get("https://aes.cryptohack.org/bean_counter/encrypt/").json()["encrypted"])

# Use the known PNG header bytes to extract the key (first 16 bytes of the ciphertext)
known_header = bytes.fromhex(png_magic_header)
extracted_key = strxor(encrypted_content[:16], known_header)  # Derive the key using XOR with known plaintext and ciphertext

# Known last eleven bytes (used for padding or other purposes)
ending_bytes = b"\xa2&\x08\xe6\xb8\xf6\x91\x14\xff\xd3/"

# XOR the key with the first 11 bytes of the known last bytes (not needed for decryption, but included for completeness)
processed_ending = strxor(extracted_key[:11], ending_bytes)

# Write the decrypted data to a file (simulate saving the PNG data)
with open("output_file.png", "wb") as output_png:
    current_position = 0
    current_block = encrypted_content[current_position:current_position+16]
    while current_block:
        # XOR the ciphertext block with the key or write the decrypted last bytes if it's not a full block
        output_png.write(strxor(current_block, extracted_key) if len(current_block) == 16 else processed_ending)
        current_position += 16
        current_block = encrypted_content[current_position:current_position+16]