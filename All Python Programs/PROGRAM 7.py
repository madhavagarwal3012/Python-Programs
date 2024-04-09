#PROGRAM 7 FOR FIBONACCI NUMBER

n= int(input("Enter Number : "))

def Fibonnici(n):
      if n <= 2:
            return n - 1
      else:
            return Fibonnici(n - 1) + Fibonnici(n - 2)

print(Fibonnici(n))

