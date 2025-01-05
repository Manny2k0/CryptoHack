from Crypto.Util.number import long_to_bytes

# Given values for a and p
a_value = 288260533169915
p_value = 1007621497415251

# Read the list of integers from the file and evaluate the content
with open("adrien_output.txt", "r") as file:
    values_list = eval(file.read())

# Initialize an empty result string
binary_result = ""

# Loop through each number in the list to compute the quadratic residue
for num in values_list:
    computed_value = pow(num, (p_value - 1) // 2, p_value)
    if computed_value == 1:
        binary_result += "1"
    else:
        binary_result += "0"

# Convert the binary result to bytes and print it
byte_result = long_to_bytes(int(binary_result, 2))
print(byte_result)
