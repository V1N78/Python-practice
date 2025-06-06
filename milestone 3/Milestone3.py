#intro
score = 0
print("Welcome to my general knowledge quiz!")
print("----------------------------------------")
print("In this quiz, you have to answer questions.. Goodluck!")
print("----------------------------------------")
#question 1
user_answer = input("1. Which is the largest ocean on Earth?")
A1 = "Pacific ocean"
A1 = "pacific ocean"
print("Your answer is: " + user_answer)
if user_answer == A1:
    print("Correct!")
    print("----------------------------------------")
    score += 1
else:
    print("Incorrect! Better luck next time")
    print("The correct answer was Pacific Ocean")
    print("----------------------------------------")

#question 2
user_answer = input("2. How many bones are there in the adult human body?")
A1 = "206"
print("Your answer is: " + user_answer)
if user_answer == A1:
    print("Correct!")
    print("----------------------------------------")
    score += 1
else:
    print("Incorrect! Better luck next time")
    print("the correct answer was 206")
    print("----------------------------------------")

#question 3
user_answer = input("3. Which gas is most abundant in the Earth’s atmosphere?")
A1 = "Nitrogen"
A1 = "nitrogen"
print("Your answer is: " + user_answer)
if user_answer == A1:
    print("Correct!")
    print("----------------------------------------")
    score += 1
else:
    print("Incorrect! Better luck next time")
    print("the correct answer was Nitrogen")
    print("----------------------------------------")

#question 4
user_answer = input("4. Which U.S. state is farthest west?")
A1 = "Alaska"
A1 = "alaska"
print("Your answer is: " + user_answer)
if user_answer == A1:
    print("Correct! Alaska crosses the 180° meridian")
    print("----------------------------------------")
    score += 1
else:
    print("Incorrect! Better luck next time")
    print("the correct answer was Alaska")
    print("----------------------------------------")

#question 5
user_answer = input("5. Which country has the most natural lakes?")
A1 = "Canada"
A1 = "canada"
print("Your answer is: " + user_answer)
if user_answer == A1:
    print("Correct!")
    print("----------------------------------------")
    score += 1
else:
    print("Incorrect! Better luck next time")
    print("the correct answer was Canada")
    print("----------------------------------------")

#question 6
user_answer = input("6. Which country has the most time zones?")
A1 = "France"
A1 = "france"
print("Your answer is: " + user_answer)
if user_answer == A1:
    print("Correct! It is due to overseas territories.")
    print("----------------------------------------")
    score += 1
else:
    print("Incorrect! Better luck next time")
    print("the correct answer was France")
    print("----------------------------------------")

#question 7
user_answer = input("7. What is the capital city of Canada?")
A1 = "ottawa"
A1 = "Ottawa"
print("Your answer is: " + user_answer)
if user_answer == A1:
    print("Correct!")
    print("----------------------------------------")
    score += 1
else:
    print("Incorrect! Better luck next time")
    print("the correct answer was Ottawa")
    print("----------------------------------------")

#question 8
user_answer = input("8. Which is the largest desert in the world?")
A1 = "Antarctic Desert"
A1 = "antarctic desert"
A1 = "Antarctic desert"
print("Your answer is: " + user_answer)
if user_answer == A1:
    print("Correct!")
    print("----------------------------------------")
    score += 1
else:
    print("Incorrect! Better luck next time")
    print("the correct answer was Antarctic Dessert")
    print("----------------------------------------")

#question 9
user_answer = input("9. What planet is known as the Red Planet?")
A1 = "Mars"
A1 = "mars"
print("Your answer is: " + user_answer)
if user_answer == A1:
    print("Correct!")
    print("----------------------------------------")
    score += 1
else:
    print("Incorrect! Better luck next time")
    print("the correct answer was Mars")
    print("----------------------------------------")

#question 10
user_answer = input("10. In which year did World War II end?")
A1 = "1945"
print("Your answer is: " + user_answer)
if user_answer == A1:
    print("Correct!")
    print("----------------------------------------")
    score += 1
else:
    print("Incorrect! Better luck next time")
    print("the correct answer was 1945")
    print("----------------------------------------")

#ending
print("Thank you for participating in the quiz!")
print("Good job, your score was:", score)