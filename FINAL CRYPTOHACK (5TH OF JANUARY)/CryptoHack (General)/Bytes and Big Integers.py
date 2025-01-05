from Crypto.Util.number import *

big_number = "11515195063862318899931685488813747395775516287289682636499965282714637259206269"  # Large numeric string
# Convert the large number into bytes and decode:
byte_representation = long_to_bytes(int(big_number))  # Convert the string to a long integer and then to bytes
decoded_message = byte_representation.decode('utf-8')  # Decode the byte sequence into a string
print(decoded_message)  # Output the decoded message
