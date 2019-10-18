def find_max(input_list):
    max_value = input_list[0]
    for num in input_list:
        if num > max_value:
            max_value = num
    print(max_value)