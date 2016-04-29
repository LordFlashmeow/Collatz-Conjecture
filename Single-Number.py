def calculate(start):
    number = start
    numbers = []
    while number > 1:
        if number % 2 == 0:
            number /= 2
            numbers.append(number)
        else:
            number = (number * 3) + 1
            numbers.append(number)
    print(numbers)
    calculate(int(input("Enter the number to test")))
calculate(int(input("Enter the number to test")))
