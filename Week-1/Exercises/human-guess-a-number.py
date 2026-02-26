#Computer guess a number

print("Think of an integer number between 1 and 100. The computer will guess a number. If it is " \
"not the number you're thinking of, type 'No', and if your number is higher than the computer's guess" \
", type 'Higher', or it it is lower, type 'Lower' when prompted. If the guess is correct, type 'Yes'.")

from random import randint

def guess_question():
    #a function that asks the player if they're thinking of a number, the number being the 
    #computer's latest guess
    return input("Is the number you are thinking of " + str(guess) + "? ")

def higher_lower():
    #a function asking the player if the number they have in mind is higher or lower than the
    #computer's latest guess
    return input("Is the number you are thinking of higher or lower than " + str(guess) + "? ")

upper_bound = 100
lower_bound = 1

guess = randint(1, 100)

running = True
#use this for while loop condition instead of while guess_question() == "No" to allow for different
#paths to be taken when the guess_question() is asked, including in the case the player makes
#an error and writes neither yes nor no.

while running:

    answer = guess_question()
    #Player asked the guess question and the answer is stored as the variable answer
    if answer == "No":
        if higher_lower() == "Higher":
        #Player asked higher/lower question. If the answer is higher:
            lower_bound = guess+1
            #The lower bound of the range from which the computer will choose the next guess
            #increases to one above the guess made.
        else:
            upper_bound = guess-1
            #If the answer is lower, the upper bound of the next guess range will reduce to one
            #below the current guess.
        guess = randint(lower_bound, upper_bound)
        #a new guess is generated
    elif answer == "Yes":
    #If the computer guesses correctly:
        running = False
        #Stop the while loop by changing the condition away from that which keeps it running
        print("Woohoo, I won!")
        #Celebrate!
    else:
        print("Please answer either 'Yes' or 'No'.")
        #If the player writes anything other than yes or no in response to the guess question, 
        #remind them of the rules. The loop restarts so they are asked the first question again.

#Human guess a number game version below

#"""Simple game where the computer chooses a number between 1 and 100, which the user must guess."""
#
#from random import randint
#
#def check_int(s):
#    """ Check if string 's' represents an integer. """
#    # Convert s to string
#    s = str(s) 
#
#    # If first character of the string s is - or +, ignore it when checking
#    if s[0] in ('-', '+'):
#        return s[1:].isdigit()
#    
#    # Otherwise, check the entire string
#    return s.isdigit()
#
#def input_integer(prompt):
#    """ Asks user for an integer input. If valid, the string input is returned as an integer. """
#    guess = input(prompt) # Ask the user for their guess
#    while not check_int(guess): # Repeat until the user inputs a valid integer
#        print('Please, enter a n integer number')
#        guess = input(prompt)  
#    return int(guess)
#
#target = randint(1, 100) # Computer selects a random number between 1 and 100 inclusive
#print("I am thinking about a number between 1 and 100. Try to find it!")
#guess = input_integer("Your guess (1-100)? ")
#
#while guess != target: # Repeat until the user guesses.
#    print("Your guess is too low!") if guess < target else print("Your guess is too high!\n")
#    guess = input_integer("New guess? ")
#
#print("You win! The number was indeed " + str(target))