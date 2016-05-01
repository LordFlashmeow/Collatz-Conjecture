def highest(start, stop):
    begin = start
    dict_max = {}
    while begin <= stop:
        current = set()
        number = begin
        if begin == 1:
            number = 2
        while number >= 1:
            if number == 1:
                max_num = int(max(current))
                break

            elif number % 2 == 0:
                number /= 2
                current.add(number)

            else:
                number = (number * 3) + 1
                current.add(int(number))
        if begin == 1:
            dict_max[1] = 0
        else:
            dict_max[begin] = max_num
        begin += 1
    return dict_max


def longest(start, stop):
    begin = start
    dict_length = {1: 0}
    while begin <= stop:
        number = begin
        numbers = set()
        while number > 1:
            if number % 2 == 0:
                number /= 2
                numbers.add(int(number))
            else:
                number = (number * 3) + 1
                numbers.add(int(number))
        dict_length[begin] = len(numbers)
        begin += 1
    return dict_length


def combined(start, stop,):
    dict_length = longest(start, stop)
    dict_max = highest(start, stop)

    final_dict = {}
    for key in (dict_length.keys() | dict_max.keys()):
        if key in dict_length: final_dict.setdefault(key, []).append(dict_length[key])
        if key in dict_max: final_dict.setdefault(key, []).append(dict_max[key])
    return final_dict


start_num = int(input("Enter the number to start at "))
stop_num = int(input("Enter the number to end at "))

print(combined(start_num, stop_num))


