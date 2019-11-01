# Build Tower by the following given argument:
# number of floors (integer and always greater than 0).

# for example, a tower of 3 floors looks like below
#
# [
#   '  *  ',
#   ' *** ',
#   '*****'
# ]


# def tower_builder(n_floors):
#     tower = []
#     for num in range(n_floors):
#         tower.append(' ' * (n_floors - num - 1) + '*' * (2 * num + 1) + ' ' * (n_floors - num - 1))
#     return '\n'.join(tower)
#
#
# print(tower_builder(20))
# '\n'.join(tower)

# def tower_builder(n):
#     return '\n'.join([("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)])


def tower_builder(n):
    tower = []
    for i in range(1, n + 1):
        tower.append(("*" * (i*2-1)).center(n*2-1))
    return '\n'.join(tower)


print(tower_builder(5))

