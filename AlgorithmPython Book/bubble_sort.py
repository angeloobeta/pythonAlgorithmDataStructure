def solution(parameter, order=True):
    sort = bubble_sort([8, 3.2, 67, 88, 90, 17, 7, 33], order)
    return sort


def bubble_sort(parameter, order):
    for i in range(len(parameter) - 1):
        for j in range(len(parameter) - i - 1):
            if order:
                if parameter[j] > parameter[j + 1]:
                    parameter[j], parameter[j + 1] = parameter[j + 1], parameter[j]
                print(parameter)
            else:
                if parameter[j] < parameter[j + 1]:
                    parameter[j], parameter[j + 1] = parameter[j + 1], parameter[j]

    return parameter


print(solution([8, 3.2, 67], False))
# print(solution([8, 3.2, 88, 67, 90, 17, 7, 33], True))
