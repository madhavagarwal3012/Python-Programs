#PROGRAM 8 FOR CHECKING THAT IF A GIVEN NUMBER IS FIBONACCI NUMBER OR NOT
n= int(input("Enter The Number You Want To Check : "))
 
#Variables For Generating Fibonacci Sequence
f3 = 0
f1 = 1
f2 = 1

#0 And 1 Both Are Fibonacci Numbers
if (n == 0 or n == 1):
    print("Given Number Is A Fibonacci Number")
 
else:
    #Generating The Fibonacci Numbers Until The Generated Number Is Less Than n
    while f3 < n:
        f3 = f1 + f2
        f2 = f1
        f1 = f3
    if f3 == n:
        print("Given Number Is Fibonacci Number")
    else:
        print("No It’s Not A Fibonacci Number")
