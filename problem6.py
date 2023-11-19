#Shubham Chandra
#problem 6

#A palindrome is a word, phrase, or sequence that reads the same backward as forward. For example, mom , racecar , "never odd or even", and "do geese see god" are all palindromes.

#Write a program that prompts a user to enter a word or phrase and test if it is a palindrome. Ignore any spaces when evaulating the strings.

word = input("Enter a word or phrase: ")

for i in range(len(word)): #check each character
    palindrome = True #assume palindrome from start
    if word[i] == word[-i-1]: #if the first character is equal to last, then palindrome. Check from outside in as i iterates upwards
        pass
    else: #if the condition is not met, it is not a palindrome, and we adjust the variable to reflect this
        palindrome = False
        break

if palindrome == True:
    print("This is a palindrome")
else:
    print("This is not a palindrome")