def solution(parameter):
    mini = minimum(parameter)
    return mini


def minimum(parameter):
    for i in range(len(parameter)-1):
        if parameter[i] < parameter[i + 1]:
            parameter[i], parameter[i + 1] = parameter[i + 1], parameter[i]
    return parameter[-1]


print(minimum([8,3.2,67, 5, 2,0.1, 0.07, 0]))