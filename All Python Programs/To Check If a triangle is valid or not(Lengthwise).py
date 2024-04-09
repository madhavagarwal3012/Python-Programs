a = eval(input("Enter Side 1: "))
b = eval(input("Enter Side 2: "))
c = eval(input("Enter Side 3: "))

if a+b>c and b+c>a and c+a>b:
	print("Triangle Is Valid")
else:
	print("Triangle Is Invalid")
