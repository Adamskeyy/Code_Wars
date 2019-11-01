
"""# Funkcja zwracająca w podanym zakresie wszystkie liczby,
dla których suma wszystkich cyfr tej liczby podniesionych do kolejnych potęg poczynając od 1
jest równa tej liczbie
Przykład: 89 = 8^1 + 9^2
"""
# test.assert_equals( sum_dig_pow(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9])
# test.assert_equals(sum_dig_pow(1, 100), [1, 2, 3, 4, 5, 6, 7, 8, 9, 89])
# test.assert_equals(sum_dig_pow(10, 89),  [89])
# test.assert_equals(sum_dig_pow(10, 100),  [89])
# test.assert_equals(sum_dig_pow(90, 100), [])
# test.assert_equals(sum_dig_pow(89, 135), [89, 135])


# def sum_dig_pow(a, b):
#     eureka_nums = []
#     for i in range(a, b + 1):
#         s = str(i)
#         len_s = len(s)
#         p = 1
#         eureka_sub = []
#         for j in s:
#             j = int(j)
#             j **= p
#             eureka_sub.append(j)
#             p += 1
#         j = sum(eureka_sub)
#         if i == j:
#             eureka_nums.append(j)
#     return eureka_nums


def sum_dig_pow(a, b):
    eureka_nums = []
    for number in range(a, b + 1):
        s_number = str(number)
        p = 1
        eureka_sub = []
        for char in s_number:
            eureka_sub.append(int(char)**p)
            p += 1
        if sum(eureka_sub) == number:
            eureka_nums.append(number)
    return eureka_nums


print(sum_dig_pow(1, 100))
