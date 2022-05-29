def solution(parameter, value, position):
    return linear_table_insertion(parameter, value, position)


def linear_table_insertion(parameter, value, position):
    if position > len(parameter): return f'Please your Insertion Position is above the Threshold, \nPlease try a lower number'
    temp = [0 for i in range(len(parameter) + 1)]
    for i in range(len(parameter)):
        if i < position-1:
            temp[i] = parameter[i]
        else:
            temp[i+1] = parameter[i]
    temp[position-1] = value
    return temp


print(solution([54, 26, 93, 17, 77, 31, 44, 55, 20, 1], 25, 5))
print(solution([54, 26, 93, 17, 77, 31, 44, 55, 20, 1], 25, 12))
