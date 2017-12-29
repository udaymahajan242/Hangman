# Name - Uday Mahajan
#Hangman - Final Project

print("Student: Uday Mahajan")
print("Assignment - Hangman - Final Project\n")


# Create a method that accepts a string as a message
# and asks the user a question with that message (input).
# Then return the user's response as the return value
# of the method
# Name: getQuestionNumber
# Input: string
# Returns: string

def getQuestionNumber(message):
    return input(message + "\n")

# Create a method that accepts the word the
# user guessed, as well as the correct answer
# and compares the two. If they match, return a
# string that tells the user that they guesses correctly,
# and tells them the guess and the correct answer.
# Make sure the word they submitted as a guess appears
# to them wrapped in double quotes
# Name: correctMessage
# Input: string, string
# Returns: string

def correctMessage(userGuess,questionAnswer):
    return ("Congratulations! You entered \"" + userGuess +  "\" and the answer is "+questionAnswer+ "!\n")

# Create a method that accepts the word the
# user guessed, as well as the correct answer
# and compares the two as lowercase strings.
# If they match, return True, otherwise return False
# Name: isCorrect
# Input: string, string
# Returns: bool

def isCorrect(userGuess,questionAnswer):
    if userGuess.lower() == questionAnswer.lower():
        return True
    return False

# Create a method that accepts a string as a message
# and asks the user a question with that message (input).
# Then return the user's response as the return value
# of the method
# Name: tryAnswer
# Input: string
# Returns: string

def tryAnswer(message):
    userResponse = input(str(message))
    return userResponse


# Create a method that accepts the correct answer
# Return a string that tells the user that the
# game is over, and what the correct answer was.
# Make sure the word they submitted as a guess appears
# to them wrapped in double quotes
# Name: gameOver
# Input: string
# Returns: string

def gameOver(questionAnswer):
    gameOverMessage = ("Sorry! The word was \"" + questionAnswer+"." +  "\" , Play Again ! \n")
    #gameOverMessage = ("Game is over. The correct answer was "+questionAnswer)
    return gameOverMessage


def main():
    # Create a dictionary of dictionaries that contain the
    # following pairs: An integer key, and a dictionary value
    # The dictionary value is a dictionary with the question's
    # answer, as the key, and the clue as the value. Assign the
    # dictionary to a variable called cluesDictionary
    cluesDictionary = {1: {"whale": "This is the largest mammal type"},
                       2: {"eagle": "This is the US national bird"},
                       3: {"football": "This popular sport is played with helmets and pads"},
                       4: {"hawaii": "This state is a collection of islands"},
                       5: {"moon": "This satellite helps control the tides"}}

    # Create a string variable that holds the following message:
    # "Enter as question number from 1 to 5, and you will play that clue. Enter -1 to quit "

    introMessage = "Enter a question number from 1 to 5, and you will play that clue. Enter -1 to quit"

    # Create a bool variable to tell the game whether to keep
    # looping, or to quit the game. Initialize the variable to True

    keepGoing = True

    # Begin a while loop that the rest of the game will live inside
    # The while loop should be a terminal loop that will be ended
    # with a break statement later if the user enters a value of "-1"

    while keepGoing == True:

    # Using a try/except block, ask the user for a number
    # and convert the result to an integer. Be sure to use
    # the getQuestionNumber method to ask for the number
    # If the user's answer cannot be converted to an integer
    # make sure the exception block ends with a continue statement
    # so that the user is asked the question again
        try:
            questionNumber = int(getQuestionNumber(introMessage))

        except:
            continue

    # If the user entered "-1" as the question number
    # tell the user "Goodbye", and set the variable called
    # keepGoing to False. Also make sure the block ends
    # with a break statement so the while loop terminates
        if questionNumber == int("-1"):
            print("GoodBye")
            keepGoing = False
            break

    # If the question number is not a value between
    # 1 and 5, return to the top of the loop with a
    # continue statement so the question is asked again

        if questionNumber not in range(1, 6):
            continue

    # Set a variable that creates a string message showing the clue
    # and ends with "What is it?"

        questionMessage = list(cluesDictionary[questionNumber].values())[0] + ". What is it?"


    # Set a variable that creates a string message showing the answer
    # in lower case
        questionAnswer = list(cluesDictionary[questionNumber].keys())[0].lower()

    # Tell the user the clue, and ask them for the correct answer
    # Be sure to use the tryAnswer method for this, and to pass
    # in the right argument (the variable questionMessage)

        userGuess = tryAnswer(questionMessage + "\n")





    # If the user entered the correct word, congratulate them
    # and tell them what they entered and what the correct word was.
    # Be sure to use the isCorrect and correctMessage methods
    # to complete this

        if isCorrect(userGuess,questionAnswer):
            print(correctMessage(userGuess, questionAnswer))
            continue



    # Else tell the user they entered an incorrect word. Use a
    # for loop to loop through letters in the correct answer until
    # they guess correctly or until they have attempted to answer
    # the same number of times as there are letters in the answer word.
    # You must tell them that they are either on the first letter,
    # the last letter or another letter in the middle when you
    # present the letters.
        else:
            print("Incorrect")


    # Create a counter variable to know the current
    # position you are at in the answer word

        index = 0

    # Begin a for loop to loop through the answer word that
    # was answered incorrectly

        for i in questionAnswer:


    # If this is the first letter, tell them so,
    # and what the letter is
    # Increment the counter
    # Tell them to guess again using the
    # tryAnswer method. Use the isCorrect
    # method to determine if the new answer
    # is correct. If the new answer is correct
    # tell them so using the correctMessage method
    # and break from the for loop
            if index == 0:
                print("The first letter is",i)
                index +=1
                userGuess = tryAnswer("Try Again! \n")
                if isCorrect(userGuess,questionAnswer):
                    print(correctMessage(userGuess,questionAnswer))
                    break

    # If this is the last letter, tell them so,
    # and what the letter is
    # Increment the counter
    # Tell them what the last letter was and
    # tell them, using the gameOver method, to play again
            elif index == len(questionAnswer)-1:
                print("The last letter was", i)
                print(gameOver(questionAnswer))

    # If this is a letter other than the first or last letter,
    # tell them so, and what the letter is
    # Increment the counter
    # Tell them to guess again using the
    # tryAnswer method. Use the isCorrect
    # method to determine if the new answer
    # is correct. If the new answer is correct
    # tell them so using the correctMessage method
    # and break from the for loop
            else:
                print("The next letter is",i)
                index+=1
                userGuess = tryAnswer("Try Again!\n")
                if (isCorrect(userGuess,questionAnswer)):
                    print(correctMessage(userGuess,questionAnswer))
                    break

    # end for
    # end while


main()
