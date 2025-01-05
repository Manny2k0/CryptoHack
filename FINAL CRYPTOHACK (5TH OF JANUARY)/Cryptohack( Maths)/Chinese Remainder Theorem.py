from functools import reduce

def find_chinese_remainder(moduli, remainders):
    total = 0
    product = reduce(lambda x, y: x * y, moduli)
    for modulus, remainder in zip(moduli, remainders):
        partial_product = product // modulus
        total += remainder * modular_inverse(partial_product, modulus) * partial_product
    return total % product
    
def modular_inverse(a, b):
    original_b = b
    previous, current = 0, 1
    if b == 1:
        return 1
    while a > 1:
        quotient = a // b
        a, b = b, a % b
        previous, current = current - quotient * previous, previous
    if current < 0:
        current += original_b
    return current

remainders = [2, 3, 5]  # x ≡ a mod x
moduli = [5, 11, 17]    # x ≡ x mod n

print(find_chinese_remainder(moduli, remainders))