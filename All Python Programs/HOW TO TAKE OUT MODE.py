#MAKE A PROGRAM TO FIND OUT MODE OF A LIST ENTERED BY USER AT RUNTIME

l=eval(input("Enter List : "))
set(l)
mode= max(set(l), key=l.count)
print("Mode Of The Given List Is : ",mode)

