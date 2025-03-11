# packing variables into tuple
tuple1 = 1, 2, "Hello"
# display tuple
print(tuple1)  
# Output (1, 2, 'Hello')

print(type(tuple1))  
# Output class 'tuple'

# unpacking tuple into variable
i, j, k = tuple1
# printing the variables
print(i, j,) 
# Output 1 2 Hello