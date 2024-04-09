#MAKE A PROGRAM TO FIND OUT WHETHER A NUMBER IS SINGLE OR DOUBLE DIGIT

#ENTERED BY USER AT RUN TIME

number=int(input("Enter Number : "))
if number >=1 and number <=9:
    print("Single Digit Number")
elif number >=10 and number <=99:
    print("Double Digit Number")
