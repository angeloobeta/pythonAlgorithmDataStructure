def solution(parameter):
    return insertion_sort(parameter)


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

def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        current_value = a_list[i]
        insertion_position = i
        while insertion_position > 0 and a_list[insertion_position - 1] > current_value:
            a_list[insertion_position] = a_list[insertion_position - 1]
            insertion_position -= 1
        a_list[insertion_position] = current_value
    return a_list


print(solution([7, 2, 4, 1, 98, 0, 121]))
print(solution([54, 26, 93, 17, 77, 31, 44, 55, 20]))
