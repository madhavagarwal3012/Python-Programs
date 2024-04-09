#PROGRAM 6 TO DISPLAY FIBONNICI SEQUENCE UPTO Nth TERM
nterms = int(input("How Many Terms? : "))

#First Two Terms
n1, n2 = 0, 1
count = 0

#Check If The Number Of Terms Is Valid
if nterms <= 0:
   print("Please Enter A Positive Integer")
   
#If There Is Only One Term, Return n1
elif nterms == 1:
   print("Fibonacci Sequence Upto",nterms,":")
   print(n1)
   
#Generate Fibonacci Sequence
else:
   print("Fibonacci Sequence :")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       
       # Update Values
       n1 = n2
       n2 = nth
       count += 1
