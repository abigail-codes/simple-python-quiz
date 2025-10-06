"""
The purpose of this program is to let the user answer a quiz.
The input will be the user's answer. The output will be whether
the answer is correct or not. At the end of the quiz, the total
percentage of score will be displayed to the user, and the user
is given a choice to retake the quiz or quit.
"""

#Quiz Intro
print("Welcome to the quiz!")
print("Press enter to continue")
input()#the user is required to enter to continue

#function of the quiz
def quiz():
    score=0 #the score is set to 0

    try:
        #display question 1
        print("\nQuestion 1:")
        print("5 x 6 = ?")
        answer1=int(input("Answer: "))#user input answer
        if answer1==30:#checking if answer is correct
            print("Correct!")
            score=score+1 #1 is added to score if correct
        else:
            print("Wrong! The correct answer is 30!")

        print("\nPress enter to continue!")
        input()#the user is required to enter to continue

        #display question 2
        print("Question 2")
        print("The capital city of Malaysia is _____.")
        answer2=str(input("Answer: ")).lower()#user input answer
        if answer2=="kuala lumpur" or "kl": #checking if answer is correct
            print("Correct!")
            score=score+1#1 is added to score if correct
        else:
            print("Wrong! The correct answer is Kuala Lumpur!")

        print("\nPress enter to continue!")
        input()#the user is required to enter to continue

        #display question 3
        print("Question 3")
        print("How many states are in Malaysia?(including federal territories)")
        answer3=int(input("Answer: "))#user input answer
        if answer3==14:#checking if answer is correct
            print("Correct!")
            score=score+1#1 is added to score if correct
        else:
            print("Wrong! The correct answer is 14!")

        print("\nPress enter to continue!")
        input()#the user is required to enter to continue

        #display question 4
        print("Question 4:")
        print("Type the value of pi, rounded to 3 decimal places")
        answer4=float(input("Answer: "))#user input answer
        if answer4==3.142:#checking if answer is correct
            print("Correct")
            score=score+1#1 is added to score if correct
        else:
            print("Wrong! The correct answer is 3.142!")

        print("\nPress enter to continue!")
        input()#the user is required to enter to continue

        #display question 5
        print("Question 5:")
        print("Where is Taylor's University located at?")
        print("A)Penang")
        print("B)Subang Jaya")
        print("C)Johor")
        print("D)Shah Alam")
        answer5=str(input("Enter your choice:")).lower()#user input answer
        if answer5=="b":#checking if answer is correct
            print("Correct")
            score=score+1#1 is added to score if correct
        else:
            print("Wrong! The correct answer is B!")

        print("\nPress enter to continue!")
        input()
    
        #quiz ending
        print("You have reach the end of the quiz!")

        #calculating the percentage of score
        percentage= (score/5)*100
        print("Your total score is {:.2f}%".format(percentage)) #the score is formatted to 2 decimal places then displayed

    except ValueError: #Print a message if player enters an invalid value
        print("Invalid Answer. Please try again.")
        
#Give choice to player whether to exit or retake quiz
while True:
    quiz()
    print("\nWould you like to retake the quiz?:")
    print("1) Yes")
    print("2) No")
    choice = input(":")
    if choice != "1": 
        print("Thank you for playing!")
        break



