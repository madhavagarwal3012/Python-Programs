#PROGRAM FOR FINDING OUT NUMBER OF LOWER AND UPPER CASE LETTERS IN A STRING ENTERED BY USER AT RUN TIME
string=eval(input("Enter String : "))
count1=0
count2=0

for i in string:
    if(i.islower()):
        count1= count1+1
    elif(i.isupper()):
        count2=count2+1

print("The number of lowercase characters is : ", count1)
print ("The number of uppercase characters is : ", count2)

#HERE WE HAVE SIMPLE USE LOOP TO FINDING THE NUMBER OF CHARACTERS
            
