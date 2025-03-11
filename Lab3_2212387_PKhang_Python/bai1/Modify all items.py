my_list = list([2, 4, 6, 8])

# change value of all items
for i in range(len(my_list)):
    # calculate square of each number
    square = my_list[i] * my_list[i]
    my_list[i] = square

print(my_list)
# Output [4, 16, 36, 64]