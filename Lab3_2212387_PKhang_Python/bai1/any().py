#with all true values
samplelist1 = [1,1,True]
print("any() True values::",any(samplelist1))

#with one false
samplelist2 = [0,1,True,1]
print("any() One false value ::",any(samplelist2))


#with all false
samplelist3 = [0,0,False]
print("any() all false values ::",any(samplelist3))

#empty list
samplelist4 = []
print("any() Empty list ::",any(samplelist4))