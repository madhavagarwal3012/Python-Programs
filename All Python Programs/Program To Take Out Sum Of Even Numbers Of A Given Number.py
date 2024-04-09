a=int(input("Enter Number : "))
sum=0
for i in range(0,a):
	if i<=a:
		if i%2==0:
			print()
			print(i)
			sum=sum+i		
	else:
		i+=1
print()
print("the sum of even numbers of the given number is",sum)
			
		