#with all true values
samplelist1 = [1,1,True]
print("all() All True values::",all(samplelist1))

#with one false
samplelist2 = [0,1,True,1]
print("all() with One false value ::",all(samplelist2))

#with all false
samplelist3 = [0,0,False]
print("all() with all false values ::",all(samplelist3))

#empty list
samplelist4 = []