def check_prime(number):
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True

success_powers = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]
prime_numbers = [prime for prime in range(100, 1000) if check_prime(prime)]

for prime in prime_numbers:
    for multiplier in range(1, prime):
        for index in range(len(success_powers) - 1):
            if not (multiplier * success_powers[index]) % prime == success_powers[index + 1]:
                break
            elif index == len(success_powers) - 2:
                print("prime:", prime)
                print("multiplier:", multiplier)
                exit()