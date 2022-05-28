def solution(parameter):
    answer = maximum_number(parameter)
    return answer


def maximum_number(parameter):
    biggest = parameter[0]
    for i in range(len(parameter) - 1):
        if parameter[i] > biggest:
            biggest = parameter[i]
    return biggest


print(solution([2, 4, 72, 98, 0, 121]))


# def maxi(arrays):
#     length = len(arrays)
#     for i in range(0, length - 1):
#         if arrays[i] > arrays[i + 1]:
#             arrays[i], arrays[i + 1] = arrays[i + 1], arrays[i]
#         max_value = arrays[length - 1]
#     return max_value
#
#
# scores = [60, 50, 95, 80, 70]
# max_value = maxi(scores)
# print("Max Value = ", max_value)
