maximum_number, d_number = 0, 0
for i in range(2, 1000000):
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
        print(f'The maximum number is {maximum_number}')
        maximum_number = count
        d_number = i
print(f'The maximum count for {maximum_number} is {d_number}')
"The maximum count for 524 is 837799"
