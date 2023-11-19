#Shubham Chandra
#Problem 2
# consulted https://stackoverflow.com/questions/5424716/how-can-i-check-if-string-input-is-a-number     

def letter_grade(your_score):
    score = int(your_score)
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

number_score = input("Enter a score:")

if number_score.isnumeric() and int(number_score) <= 100 and int(number_score) >= 0:
    your_grade = letter_grade(number_score)
    if your_grade == "A" or your_grade == "E" or your_grade == "F":
        print(f"You receieved an {your_grade}!")
    else:
        print(f"You received a {your_grade}!")
else:
    print("That is not valid input.")