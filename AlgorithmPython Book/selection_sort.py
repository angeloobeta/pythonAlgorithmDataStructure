def solution(parameter):
    # sort_ = select_sort(parameter)
    sort_ = selection_sort(parameter, False)
    return sort_


# def select_sort(parameter):
#     for i in range(len(parameter)-1):
#         minimum, index = parameter[i], i
#         for j in range(i + 1, len(parameter)):
#             if minimum > parameter[j]:
#                 minimum, index, = parameter[j], j
#         parameter[index], parameter[i] = parameter[i], parameter[index]
#     return parameter

def selection_sort(parameter, order=True):
    if order:
        for i in range(len(parameter) - 1):
            minimum = parameter[i]
            for j in range(i + 1, len(parameter)):
                if minimum > parameter[j]:
                    minimum = parameter[j]
            # parameter[i], parameter[parameter.index(minimum)] = minimum, parameter[i]
            parameter[parameter.index(minimum)], parameter[i] = parameter[i], minimum
        return parameter
    else:
        for i in range(len(parameter) - 1):
            minimum = parameter[i]
            for j in range(i + 1, len(parameter)):
                if minimum > parameter[j]:
                    minimum = parameter[j]
            # parameter[i], parameter[parameter.index(minimum)] = minimum, parameter[i]
            parameter[parameter.index(minimum)], parameter[i] = parameter[i], minimum
        return parameter


print(solution([50, 8, 55, 3, 17, 70]))
