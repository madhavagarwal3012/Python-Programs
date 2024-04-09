#MAKE A PROGRAM TO FIND OUT MEAN OF A LIST ENTERED BY USER AT RUNTIME

l=eval(input("Enter List : "))
len(l)

sum=0
for i in range(0,len(l)):
    sum+=l[i]

mean=sum/len(l)
print("The mean of the given list is : ",mean)
