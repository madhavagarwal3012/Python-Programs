#PROGRAM 4 TO PRINT ALL PRIME NUMBERS IN AN INTERVAL

lower = int(input("Enter lower number : "))
upper = int(input("Enter upper number :"))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # All prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
