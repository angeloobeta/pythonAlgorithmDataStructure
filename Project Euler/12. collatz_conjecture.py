from timeit import timeit


def collatz_conjecture(e, f):
    maximum_number, d_number = 0, 0
    for i in range(e, f):
        count = 0
        b = i
        while b != 1:
            if b % 2 == 0:
                b = b / 2
                # print(f'Under the even part b is {b}')
                count += 1
            elif b % 2 != 0:
                b = (b * 3) + 1
                # print(f'Under the odd part b is {b}')
                count += 1
        if count > maximum_number:
            # print(f'The maximum number is {maximum_number}')
            maximum_number = count
            d_number = i
    return f'The maximum count for {maximum_number} is {d_number}'


print(collatz_conjecture(2, 1000000))
"The maximum count for 524 is 837799"

fun = '''
def custom_power(x, y):
    result = 1
    for i in range(y):
        result = result * x
        # print(result)
    return result
'''
# t = timeit("custom_power(3,4)", setup=fun)
# print(t)
