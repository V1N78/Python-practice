#start
score = 0
print("Welcome to my general knowledge quiz!")
print("----------------------------------------")
print("In this quiz, you have to answer questions.. Goodluck!")
print("----------------------------------------")

#question 1
user_answer = input("1. Which planet has the most moons?").lower()
A1 = "saturn"
print("Your answer is: " + user_answer)
if user_answer == A1:
    print("Correct!")
    print("----------------------------------------")
    score += 1
else:
    print("Incorrect! Better luck next time!")
    print("The correct answer was: Saturn")
    print("----------------------------------------")

#question 2
user_answer = input("2. How many bones are there in the adult human body?")
A2 = "206"
print("Your answer is: " + user_answer)
if user_answer == A2:
    print("Correct!")
    print("----------------------------------------")
    score += 1
else:
    print("Incorrect! Better luck next time!")
    print("the correct answer was: 206")
    print("----------------------------------------")

#question 3
user_answer = input("3. Which gas is most abundant in the Earth’s atmosphere?").lower()
A3 = "Nitrogen"
print("Your answer is: " + user_answer)
if user_answer == A3:
    print("Correct!")
    print("----------------------------------------")
    score += 1
else:
    print("Incorrect! Better luck next time!")
    print("the correct answer was: Nitrogen")
    print("----------------------------------------")

#question 4
user_answer = input("4. Which U.S. state is farthest west?").lower()
A4 = "Alaska"
print("Your answer is: " + user_answer)
if user_answer == A4:
    print("Correct! Alaska crosses the 180° meridian")
    print("----------------------------------------")
    score += 1
else:
    print("Incorrect! Better luck next time!")
    print("the correct answer was: Alaska")
    print("----------------------------------------")

#question 5
user_answer = input("5. Which country has the most natural lakes?").lower()
A5 = "Canada"
print("Your answer is: " + user_answer)
if user_answer == A5:
    print("Correct!")
    print("----------------------------------------")
    score += 1
else:
    print("Incorrect! Better luck next time!")
    print("the correct answer was: Canada")
    print("----------------------------------------")

#question 6
user_answer = input("6. Which country has the most time zones?").lower()
A6 = "France"
print("Your answer is: " + user_answer)
if user_answer == A6:
    print("Correct! It is due to overseas territories.")
    print("----------------------------------------")
    score += 1
else:
    print("Incorrect! Better luck next time!")
    print("the correct answer was: France")
    print("----------------------------------------")

#question 7
user_answer = input("7. What is the capital city of Canada?").lower()
A7 = "Ottawa"
print("Your answer is: " + user_answer)
if user_answer == A7:
    print("Correct!")
    print("----------------------------------------")
    score += 1
else:
    print("Incorrect! Better luck next time!")
    print("the correct answer was: Ottawa")
    print("----------------------------------------")

#question 8
user_answer = input("8. Which is the largest desert in the world?").lower()
A8 = "Antarctic desert"
print("Your answer is: " + user_answer)
if user_answer == A8:
    print("Correct!")
    print("----------------------------------------")
    score += 1
else:
    print("Incorrect! Better luck next time!")
    print("the correct answer was: Antarctic Dessert")
    print("----------------------------------------")

#question 9
user_answer = input("9. What planet is known as the Red Planet?").lower()
A9 = "Mars"
print("Your answer is: " + user_answer)
if user_answer == A9:
    print("Correct!")
    print("----------------------------------------")
    score += 1
else:
    print("Incorrect! Better luck next time!")
    print("the correct answer was: Mars")
    print("----------------------------------------")

#question 10
user_answer = input("10. In which year did World War II end?")
A10 = "1945"
print("Your answer is: " + user_answer)
if user_answer == A10:
    print("Correct!")
    print("----------------------------------------")
    score += 1
else:
    print("Incorrect! Better luck next time!")
    print("the correct answer was: 1945")
    print("----------------------------------------")

#ending
print("Thank you for participating in the quiz!")
print("Good job, you scored:", score, "out of 10!")