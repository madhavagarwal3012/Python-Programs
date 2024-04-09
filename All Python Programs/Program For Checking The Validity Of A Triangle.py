print("How You Want To Check The Validity Of A Triangle")
print("1)Lengthwise")
print("2)Anglewise")
print()
option=int(input("Enter Your Choice: "))
if option==1:
	print()
	print("Enter Length Of Sides")
	a = eval(input("Enter Side 1: "))
	b = eval(input("Enter Side 2: "))
	c = eval(input("Enter Side 3: "))
	if a+b>c and b+c>a and c+a>b:
		print()
		print("Triangle Is Valid")
	else:
		print("Triangle Is Invalid")

if option==2:
		print()
		print("Enter Angles Of Sides")
		print()
		a = eval(input("Enter Angle 1: "))
		b = eval(input("Enter Angle 2: "))
		c = eval(input("Enter Angle 3: "))
		print()
		print("How You Want To Take Out")
		print("1)By Determining 180°")
		print("2)By Determining Sum Or Equality")
		print()
		option=int(input("Enter Your Choice: "))
		if option==1:
			if a+b+c==180:
				print()
				print("Triangle Is Valid")
			else:
				print("Triangle Is Invalid")
		if option==2:
			if a+b>=c and b+c>=a and c+a>=b:
				print()
				print("Triangle Is Valid")
			else:
				print("Triangle Is Invalid")
