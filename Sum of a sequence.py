"""Your task is to make function, which returns the sum of a sequence of integers.

The sequence is defined by 3 non-negative values: begin, end, step.

If begin value is greater than the end, function should returns 0
"""
# Examples
#
# sequenceSum(2,2,2) === 2
# sequenceSum(2,6,2) === 12 // 2 + 4 + 6
# sequenceSum(1,5,1) === 15 // 1 + 2 + 3 + 4 + 5
# sequenceSum(1,5,3) === 5 // 1 + 4


# def sequence_sum(begin_number, end_number, step):
#     if begin_number < end_number:
#         sequence = []
#         for num in range(begin_number, end_number + 1, step):
#             sequence.append(begin_number)
#             begin_number += step
#         return sum(sequence)
#     elif begin_number == end_number:
#         return begin_number
#     else:
#         return 0


def sequence_sum(begin_number, end_number, step):
    return sum(range(begin_number, end_number+1, step))


print(sequence_sum(1, 5, 1))
