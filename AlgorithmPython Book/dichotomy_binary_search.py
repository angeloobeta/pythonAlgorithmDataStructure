def solution(parameter, value):
    return dichotomy_binary_search(parameter, value)


def dichotomy_binary_search(parameter, value):
    middle_term, count = (len(parameter) - 1) // 2, (len(parameter) - 1) // 2
    while parameter[middle_term] != value and count != 0:
        count -= 1
        if middle_term > value:
            middle_term = (middle_term + len(parameter)-1)//2
        else:
            middle_term = (middle_term - 1) // 2


print(solution([0, 1, 2, 4, 6, 7, 9, 11, 55, 98, 121], 6))
