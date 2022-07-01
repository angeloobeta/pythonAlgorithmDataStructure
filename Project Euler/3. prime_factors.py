def is_prime(number):
    for i in range(3, number // 2, 2):
        if number % i == 0:
            return False
    return True


def prime_factor(number):
    maximum_number = 0
    for i in range(3, number // 2, 2):
        if number % i == 0 and is_prime(i):
            maximum_number = i
    return maximum_number


print(prime_factor(21))
