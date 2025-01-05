# Flag: Cryp{ASCII_print4bl3}

# The program converts ASCII values into characters and concatenates them into a string.
ascii_values = [199, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

# Convert ASCII values to characters and concatenate them into a string
# The list comprehension converts each ASCII value to its corresponding character using the chr() function
# and joins them into a single string.
output_flag = ''.join(chr(value) for value in ascii_values)

# Output the flag
# The resulting string is stored in output_flag and printed, which outputs Cryp{ASCII_print4bl3}.
print(output_flag)  # Cryp{ASCII_print4bl3}