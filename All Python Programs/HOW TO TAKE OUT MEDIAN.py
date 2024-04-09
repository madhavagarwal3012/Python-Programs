#MAKE A PROGRAM TO FIND OUT MEDIAN OF A LIST ENTERED BY USER AT RUNTIME

l=eval(input("Enter list : "))
len(l)
l.sort()

if len(l)%2==0:
    median1 = l[len(l)//2]
    median2 = l[len(l)//2-1]
    median = (median1 + median2)/2

else:
    median = l[len(l)//2]

print("Median Of The Given List Is: " + str(median)) 
