from blockutils import *
from string import printable
from multiprocessing import Pool
from functools import partial

def encode_chars(hex_values):
    return getdata(f'ctrime/encrypt/{hex_values}', 'ciphertext')  # getdata is a function from my blockutils module

def determine_length(current_str, current_char):
    return (current_char, len(encode_chars(strtohex(current_str[-5:] + current_char))))  # strtohex is another function from blockutils, just string.encode().hex()

current_string = 'crypto{'

pool_instance = Pool(50)
while '}' not in current_string:
    length_results = pool_instance.map(partial(determine_length, current_string), printable)  # try every printable character
    selected_char = min(length_results, key=lambda item: item[1])[0]  # the correct one must be the shortest
    current_string += selected_char
    print(current_string, end='\r')
print()