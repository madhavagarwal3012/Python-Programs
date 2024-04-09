#PROGRAM 2 TO COMPUTE COMPOUND INTEREST
 
p = float(input("Enter The Principal Amount : "))

t = float(input("Enter The Number Of Years : "))
 
r = float(input("Enter The Rate Of Interest : "))
 
#Compute Compound Interest
CI = p * (pow((1 + r / 100), t)) 
 
#print
print("Compound Interest : ", round(CI))




