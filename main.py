def is_even(digit):
    return digit % 2 == 0

assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')


def prime_generator(end):
    if end < 2:
        return

    is_prime = [True] * (end + 1)
    is_prime[0] = is_prime[1] = False

    for start in range(2, int(end ** 0.5) + 1):
        if is_prime[start]:
            for multiple in range(start * start, end + 1, start):
                is_prime[multiple] = False

    for num in range(2, end + 1):
        if is_prime[num]:
            yield num

from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')

## HW10.3 and HW11.1