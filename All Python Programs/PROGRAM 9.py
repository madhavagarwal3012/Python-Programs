#PROGRAM 9 FOR FINDING n\'th MULTIPLE OF A NUMBER IN FIBONACCI NUMBER

#Number Of Whose Multiple We Are Finding 
n= int(input(" Enter Number : "))

#Multiple No.
m= int(input (" Enter Multiple No. "))

def find(n, m):
    f1 = 0
    f2 = 1
    i =2; 
    while i!=0:
        f3 = f1 + f2;
        f1 = f2;
        f2 = f3;
 
        if f2%n == 0:
            return m*i
 
        i+=1
         
    return
print("Position Of n\'th Multiple Of A Number In Fibonacci Series Is: ", find(n,m)+1)
