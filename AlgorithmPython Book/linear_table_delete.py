def solution(parameter, position):
    return linear_table_delete(parameter, position)


def linear_table_delete(parameter, position):
    temp = [0 for i in range(len(parameter) - 1)]
    for i in range(len(temp)):
        if i < position:
            temp[i] = parameter[i]
        else:
            temp[i] = parameter[i + 1]
    return temp


print(solution([2, 4, 1, 6, 7, 9, 0, 1, 55, 11], 2))
