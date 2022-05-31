def solution(parameter, value):
    return linear_table_search(parameter, value)


def linear_table_search(parameter, value):
    for i in range(len(parameter)):
        if value == parameter[i]:
            return f"Value was found at index {i}"
    return -1


print(solution([2, 4, 6, 7, 9, 0, 1, 55, 11], 0))