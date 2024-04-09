a = int(input("enter first number :"))
b = int(input("enter second number :"))
c = int(input("enter third number: "))

if a>b and b>c:
	print("The largest number is : ", a)
	
elif b>c and c>a:
	print("The largest number is : ", b)
	
elif c>b and b>a:
	print("The largest number is : ", c)
	
else:
	print("No number is found largest among the given 3 numbers")
	
	