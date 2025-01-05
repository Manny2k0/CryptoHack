# Perform XOR manually using Python's built-in functions
key_1 = bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
key_2_3 = bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
encoded_flag = bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')

# XOR operation between the three byte sequences
decoded_flag = bytes(a ^ b ^ c for a, b, c in zip(key_1, key_2_3, encoded_flag))

decoded_flag  # Display the decoded result
