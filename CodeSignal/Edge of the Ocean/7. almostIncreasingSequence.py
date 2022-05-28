"""
Problem Statement

Given a sequence of integers as an array, determine whether it is possible to obtain a strictly
increasing sequence by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing
only one element is also considered to be strictly increasing.

Example

For sequence = [1, 3, 2, 1], the output should be
solution(sequence) = false.

There is no one element in this array that can be removed in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
solution(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get
the strictly increasing sequence [1, 3].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer sequence

Guaranteed constraints:
2 ≤ sequence.length ≤ 105,
-105 ≤ sequence[i] ≤ 105.

[output] boolean

Return true if it is possible to remove one element from the array in order to get a strictly increasing sequence,
otherwise return false.

"""


def solution(sequence):
    count, count_, count__, count_l, = 0, 0, 0, 0
    # minimum = min(sequence)
    # if len(sequence) > 8:
    #     sequence.remove(max(sequence))
    another = sorted(sequence)
    if len(sequence) == 2 and sequence[0] == sequence[1]:
        return True
    if another[0] == another[1] and another[-1] == another[-2]:
        return False
    if another[-1] == another[-2] == another[-3]:
        return False


    for i in range(len(sequence) - 1):
        if sequence[i] > sequence[i + 1]:
            count += 1
            if count >= 2:
                return False

    # for i in range(len(sequence) - 1):
    #     if minimum == another[i + 1]:
    #         count__ += 1
    #         if count__ >= 2:
    #             return False
    for i in range(len(sequence) - 1):
        if another[i] == another[i + 1]:
            count_ += 1
            if count_ >= 2:
                return False

    for i in range(len(sequence) - 1):
        for j in range(i, len(sequence) - 1):
            if sequence[i] > sequence[j]:
                count_l += 1
                if count_l >= 2:
                    return False

    return True


print(solution([1, 3, 2, 1]))
print(solution([10, 1, 2, 3, 4, 5]))
print(solution([40, 50, 60, 10, 20, 30]))


# def solution(sequence):
#     count, count_, count__, count_l, = 0, 0, 0, 0
#     minimum = min(sequence)
#     if (len(sequence) > 8): sequence.remove(max(sequence))
#     another = sorted(sequence)
#     if (len(sequence) == 2 and sequence[0] == sequence[1]): return True
#     if (another[0] == another[1] and another[-1] == another[-2]): return False
#     if (another[-1] == another[-2] == another[-3]): return False
#
#     for i in range(len(sequence) - 1):
#         for j in range(i, len(sequence) - 1):
#             if (sequence[i] > sequence[j]):
#                 count_l += 1
#                 if count_l >= 2:
#                     return False
#         if (sequence[i] > sequence[i + 1]):
#             count += 1
#             if count >= 2:
#                 return False
#         elif (minimum == another[i + 1]):
#             count__ += 1
#             if count__ >= 2:
#                 return False
#         elif (another[i] == another[i + 1]):
#             count_ += 1
#             if count_ >= 2:
#                 return False
#
#     return True


