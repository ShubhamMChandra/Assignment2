#Shubham Chandra
#Problem 4

# Implement a function that takes three numbers as input and returns the largest of the three. 
# While there is a built-in function max() in Python, do not use it.

def max_of_three(x, y, z):
    largest = x #arbitrarily set x as the largest
    if y > largest:  #if y is larger, then it is now largest
        largest = y
    if z > largest: #if z is larger, then z is now largest
        largest = z
    return largest #store the one that is now in the largest spot

print(max_of_three(1,2,-10)) #test with three random numbers

