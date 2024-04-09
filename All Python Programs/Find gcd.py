a= int(input(" Enter First Number : "))
b= int(input(" Enter Second Number : "))

smaller = a

if a<b:
	if b%a==0:
		print(a)

else:
	smaller = b
	if a%b==0:
		print(b)
	else:
		i=2
		gcd=1
		if i<=smaller:
			a%i==0 and b%i==0
			gcd=i
		else:
			print(gcd)
i=i+1
	