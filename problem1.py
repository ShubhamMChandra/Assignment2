# Create a temperature converter program that takes input from a user in Fahrenheit and converts it to Celsius. 
#Shubham Chandra
#Problem 1

# You should check that the input is valid (ie. the input is a positive, whole number). 
# If it is not, warn the user to enter a whole number, positive number and exit the program.  
# If it is a valid number, print the temperature rounded to two decimal places.

def is_float(value):
    if value.replace(".","").isnumeric():
        return True
    else:
        return False

while True:
    f_temp = input("Enter a temperature in Fahrenheit:")
    if is_float(f_temp) and float(f_temp).is_integer() and float(f_temp) > 0: 
        f_temp_int = int(f_temp)
        c_temp = ((f_temp_int - 32) * 5/9)
        c_temp_round = str(round(c_temp,2))
        print(f"The temperature is {c_temp_round} in Celsius")
    else:
        print("Please enter a positive, whole number numeric temperature.")

