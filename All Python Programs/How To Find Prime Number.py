#MAKE A PROGRAM TO KNOW WHETHER A NUMBER IS A PRIME NUMBER OR NOT

#ENTERED BY USER AT RUN TIME 

n=int(input("Enter Number : "))
for i in range(2,n):
    if n%i==0:
        print(n,"not a prime number")
        break
else:
    print(n,"is a prime number")
