def longest(start, stop):
    begin = start
    dict_numbers = {1: 0}
    while begin <= stop:
        numbers = []
        number = begin
        while number > 1:
            if number % 2 == 0:
                number /= 2
                numbers.append(int(number))
            else:
                number = (number * 3) + 1
                numbers.append(int(number))
        dict_numbers[begin] = numbers
        begin += 1
    print(dict_numbers)

    longest(int(input("Enter the number to start at")), int(input("Enter the number to stop at (Inclusive)")))
longest(int(input("Enter the number to start at")), int(input("Enter the number to stop at (Inclusive)")))
