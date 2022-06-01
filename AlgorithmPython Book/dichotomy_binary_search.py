def solution(parameter, value):
    return dichotomy_binary_search(parameter, value)


def dichotomy_binary_search(parameter, value):
    first_term, last_term = 0, len(parameter)-1
    middle_term = (first_term + last_term) // 2
    count = middle_term
    while parameter[middle_term] != value and count != 0:
        if count != 0:
            count -= 1
            if parameter[middle_term] > value:
                last_term = middle_term
                middle_term = (first_term + last_term) // 2
            else:
                first_term = middle_term
                middle_term = (first_term + last_term) // 2
        else:
            # value == parameter[middle_term]:
            return f'Value found at index {middle_term}'
    return f'Value not found'


print(solution([0, 1, 2, 4, 6, 7, 9, 11, 55, 98, 121], 6))
