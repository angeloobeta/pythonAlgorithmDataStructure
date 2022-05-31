def solution(parameter):
    return reverse_array(parameter)


def reverse_array(parameter):
    length_of_list = len(parameter) - 1
    for i in range(len(parameter) // 2):
        parameter[i], parameter[length_of_list - i] = parameter[length_of_list - i], parameter[i]
    return parameter


print(solution([2, 4, 6, 7, 9, 0, 1, 55, 11]))
