nestedlist = [[2,4,6,8,10],[1,3,5,7,9]]

print("Accessing the third element of the second list",nestedlist[1][2])
for i in nestedlist:
  print("list",i,"elements")
  for j in i:
    print(j)