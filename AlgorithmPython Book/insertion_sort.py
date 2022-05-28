def solution(parameter):
    return insertion_sort_whileloop(parameter)
    # return insertion_sort_forloop(parameter)


# def insertion_sort(array):
#     for i in range(len(array) - 2):
#         insert_element = array[i]
#         insert_position = i
#         for j in range(len(array) - 1, -1):
#             if insert_element < array[j]:
#                 array[j + 1] = array[j]
#                 insert_position -= 1
#             array[insert_position] = insert_element
#     return array


# def insertion_sor(array):
#     for i in range(len(array) - 1):
#         temp = [i for i in range(len(array))]
#         insert_element = array[i]
#         insertion_position = i
#     for j in range(insertion_position + 1):
#         if array[insert_element] > array[j + insertion_position]:
#             insert_element -= 1
#             continue
#         temp[i], temp[i+1] = array[j+1], array[j]
# Implementation using While Loop
def insertion_sort_whileloop(parameter):
    for i in range(1, len(parameter)):
        current_value = parameter[i]
        current_position = i
        while current_position > 0 and parameter[current_position - 1] > current_value:
            parameter[current_position] = parameter[current_position - 1]
            current_position -= 1
        parameter[current_position] = current_value
    return parameter


# Implementation using For Loop
def insertion_sort_forloop(parameter):
    for i in range(1, len(parameter)):
        current_value = parameter[i]
        current_position = i
        for i in range(i):
            if current_position > 0 and parameter[current_position - 1] > current_value:
                parameter[current_position] = parameter[current_position - 1]
                current_position -= 1
        parameter[current_position] = current_value
    return parameter


# print(solution([7, 2, 4, 1, 98, 0, 121]))
print(solution([54, 26, 93, 17, 77, 31, 44, 55, 20, 1]))
