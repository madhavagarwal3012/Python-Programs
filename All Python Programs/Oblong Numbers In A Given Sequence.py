#DEFINATION
print("What Is An Oblong Number ?")
print("\u27A1 An Oblong Number is any number that is the product of two consecutive integers. Oblong numbers are also known as pronic numbers. The first few of them are: 0, 2, 6, 12, 20, and 30.")
print()


#PROGRAM

#FUNCTION DEFINATION
def checkOblong():    

    #IMPORTING MODULE
    import math     

    #TAKING INPUT FROM THE USER IN STRING
    numbers = input("Enter List Of Numbers: ")

    #CONVERTING THE GIVEN STRING INPUT IN LIST
    numbers = numbers.split()

    #CONVERTING ELEMENTS OF LIST FROM STRING TO INTEGER VALUE USING TYPECAST
    for element in range(len(numbers)):
        numbers[element] = int(numbers[element])

    #CREATING AN EMPTY LIST FOR STORING OBLONG NUMBERS
    Oblong = []

    #CREATING AN EMPTY LIST FOR STORING NON-OBLONG NUMBERS
    Non_Oblong = []


    #IMPLEMENTATION OF FOR LOOP & DEFINING RANGE THROUGH LEN FUNCTION
    for element in range(len(numbers)):

        #FINDING FIRST CONSECUTIVE NUMBER THROUGH SQUARE ROOT OF THE ELEMENT IN THE LIST
        consecutive_number1 = int(math.sqrt(numbers[element]))

        #SECOND CONSECUTIVE NUMBER IS NEXT TO FIRST CONSECUTIVE NUMBER SO SIMPLY ADDING 1
        consecutive_number2 = consecutive_number1 + 1

        #IMPLEMENTING IF CONDITION TO CHECK IF THE PRODUCT OF TWO CONSECUTIVE NUMBERS IS EQUAL TO THE ELEMENT IN THE LIST
        if(consecutive_number1 * consecutive_number2 == numbers[element]):

            #IF CONDITION IS SATISYFING, THE INSERTING THE ELEMENT IN THE OBLONG LIST
            Oblong.append(numbers[element])
            
            print()
            print(f"{numbers[element]} Is An Oblong Number Because Consecutive Number({consecutive_number1} * {consecutive_number2}) Is Equal To {numbers[element]}")

        #IMPLEMENTING ELSE CONDITION FOR THE CASE WHERE THE PRODUCT OF TWO CONSECUTIVE NUMBERS IS NOT EQUAL TO THE ELEMENT IN THE LIST
        else:

            #INSERTING THE ELEMENT IN THE NON-OBLONG LIST
            Non_Oblong.append(numbers[element])
            
            print()
            print(f"{numbers[element]} Is A Non-Oblong Number Because Multiplication Of Any Consecutive Number Is Not Equal To {numbers[element]}")

    #DEFINING AN EMPTY DICTIONARY FOR STORING BOTH OBLONG AND NON-OBLONG NUMBERS, TWO KEYS(OBLONG NUMBERS, NON_OBLONG NUMEBRS)
    numberDictionary = {}

    #INSERTING FIRST KEY
    numberDictionary["Oblong Numbers"] = Oblong

    #INSERTING SECOND KEY
    numberDictionary["Non-Oblong Numbers"] = Non_Oblong

    print()

    #PRINTING THE FINAL DICTIONARY
    print(numberDictionary)

#FUNCTION CALLING
checkOblong()
