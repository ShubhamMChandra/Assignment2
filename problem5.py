#Shubham Chandra
#Problem 5 

#To determine divisibility by 11, take the alternating sum of the digits in the number, read from left to right. 
# If that sum is divisible by 11, so is the original number.
# example: 123 > 1 - 2 + 3

number = input("Please enter a number: ") # start the number and leave as a string so that we can iterate through it

if number.isnumeric():
    even = True #set this counter to check which place we are in for the characters in the string
    total = 0 #what is the total character count values? We will be adding to this so we start at 0
    for char in number: #we take each character in the string
        new = int(char) #to properly add, we convert the character to an integer
        if even == True: #if it's even we add
            total = total + new
            even = False
        else: #if its not even (else) we subtract 
            total = total - new
            even = True
    if total % 11 == 0: #if no remainder,it's good to be divided by 11
        print("This is divisible by 11")
    else:
        print("This is not divisible by 11")
else:
    print("Invalid input, please try a number next time and restart program")



          
    