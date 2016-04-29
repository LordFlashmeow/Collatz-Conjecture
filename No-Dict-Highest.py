start_num = int(input("Enter the number to start at "))
end_num = int(input("Enter the number to end at ")) + 1
repeat_times = end_num - start_num

if start_num < 1:
    start_num = 1

temp = set()

for x in range(repeat_times):

    new_num = start_num

    while start_num != 1:

        if new_num == 1:
            hinum = int(max(temp))
            combined = str(start_num) + "," + str(hinum) + "\n"
            table = open('No_Dict.csv', 'a')
            table.write(combined)
            table.close()
            temp.clear()
            break

        elif new_num % 2 == 0:
            new_num /= 2
            temp.add(new_num)

        else:
            new_num *= 3
            new_num += 1
            temp.add(new_num)
    start_num += 1

end = input("Complete.\nPress enter to quit")