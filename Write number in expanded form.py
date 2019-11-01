"""You will be given a number and you will need to return it as a string in Expanded Form.
For example:"""
# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'


# def expanded_form(num):
#     str_lst = []
#     power = len(str(num)) - 1
#     for i in str(num):
#         str_lst.append(str(int(i) * 10 ** power))
#         power -= 1
#     print(str_lst)
#     return f'Expanded form of {num} is: ' + ' + '.join([x for x in str_lst if x != '0'])
#
#
# print(expanded_form(70304))


# def expanded_form(num):
#     num = list(str(num))
#     print(num)
#     return ' + '.join(x + '0' * (len(num) - y - 1) for y, x in enumerate(num) if x != '0')


# def expanded_form(num):
#     num = list(str(num))
#     for y, x in enumerate(num):
#         if x != 0:
#             return ' + '.join(x + '0' * (len(num) - y - 1))


def expanded_form(num):
    str_lst = []
    power = len(str(num)) - 1
    for i in str(num):
        if i == '0':
            power -= 1
            continue
        str_lst.append(str(int(i) * 10 ** power))
        power -= 1
    print(str_lst)
    return f'Expanded form of {num} is: ' + ' + '.join([x for x in str_lst])


print(expanded_form(70304))
