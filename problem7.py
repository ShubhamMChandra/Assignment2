#Shubham Chandra
#problem 7

#Write a function that draws a triangle out of asterix similar to that below. The function should take an integer argument that represents the height of the triangle. Do not use a recursive function.

def pyramid(height):
    int_height = int(height) #convert to integer
    i = 1 #start at 1 asterisk to be printed
    while i <= int_height:  #increase till the target height
        print(i * "*")
        i = i+1


pyramid(5) #test the function