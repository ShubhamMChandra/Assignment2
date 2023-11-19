#Shubham Chandra
#Problem 3


#check if the string is equal to or longer than 12 char
def IsLong(string):
    if len(string) >= 12:
        return True
    else:
        return False

#check it has a lower case letter
def hasLOWERletter(string):
    letters = "abcdefghijklmnopqrstuvwxyz"
    for char in string:
        if char in letters:
            return True
    return False

#check if string has numeber in it
def hasnum(string):
    numbers = "0123456789"
    for char in string:
        if char in numbers:
            return True
    return False

#check that string has upper case in it
def hasUPPERletter(string):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in string:
        if char in letters:
            return True
    return False

#Check that string has a special character in it
def hasSpecial(string):
    special = "!@#$%"
    for char in string:
        if char in special:
            return True
    return False

#get password
pwd = input("Enter a password:")

#check against all conditions
if hasLOWERletter(pwd) and hasnum(pwd) and IsLong(pwd) and hasUPPERletter(pwd) and hasSpecial(pwd):
    print("This is a strong password :)")
else: 
    print("This is not a strong password :(")