input_string = "label"  # String to be transformed

# Start the output with the "crypto{" prefix
print("crypto{", end="")

# Apply XOR with 13 on each character of the string and print the result
for char in input_string:
    print(chr(ord(char) ^ 13), end="")

# Close the output with the "}" suffix
print("}")
