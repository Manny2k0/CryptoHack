from pwn import exclusive_or

encrypted_data = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
encryption_key = exclusive_or(encrypted_data[:7], 'crypto{') + exclusive_or(encrypted_data[-1], '}')  # we know first 7 bytes and the last 1
# the first part is 'myExclusiveOrKe' and the last is 'y'
print(exclusive_or(encrypted_data, encryption_key))