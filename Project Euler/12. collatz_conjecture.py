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
    return f"{d_number} has {maximum_number} counts for {f} numbers"


# print(collatz_conjecture(2, 10000000))
# print(collatz_conjecture(2, 1000000000))
"The maximum count for 1000000 number is 524 with  counts"
"837799 has 524 counts for 1,000,000 numbers"
"8400511 has 685 counts for 10,000,000 numbers"
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
