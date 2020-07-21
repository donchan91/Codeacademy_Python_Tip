# Number guess game. Written for the Number Guess Game challenge in CodeAcademy's Learn Python 2 project.
# Please put print statements within parentheses if running this program on Python 3. 

#2 Impoorting randint from the random module
from random import randint 

#3 Importing the sleep function from the time module
#Remember: from module import function
from time import sleep

#4 + 5 Prompting the user to make a guess
def get_user_guess():
#6 Turning the input number (string) into an integer
  guess = int(raw_input("Guess a number between 2-12: "))
#7 Return the user's guess  
  return guess
#8 Building roll_dice() function for the pair of dice
#9 Adding parameter number_of_sides
def roll_dice(number_of_sides):
#10 first_roll as dice roll No. 1/2
  first_roll = randint(1, number_of_sides)
#11 second_roll as the dice roll No. 2/2
  second_roll = randint(1, number_of_sides)
#12 Maximum value that the dice can roll
  max_val = number_of_sides * 2
#13 Printing out max_val
  print "The maximum possible value is %d." % max_val
#14 Storing get_user_guess() in guess
  guess = get_user_guess()
#15 Error check
  if guess > max_val or guess < 1:
#16 Error message when it's too big
    print "Error: Invalid input."
#18 Else statement to get the dice rolling
  else:
    print "Rolling..."
#19 Program pauses for 2 seconds
    sleep(2)
#20 Print the first roll and pause for one second 
    print "The 1st roll is: %d" % first_roll
    sleep (1)
    #21 Print the second roll and pause for one second
    print "The 2nd roll is: %d" % second_roll
    #22. Creating total_roll
    total_roll = first_roll + second_roll
    #23 Printing the total
    print "Result... %d" % total_roll
    sleep (1)
    #24 If statement within the else block to check if the user input is the same as 
    if guess == total_roll:
      print "Congratulations! You guessed right!"
    #25 When the guess is not the same
    else:
      print "Sorry! You guessed the wrong number!"
#26 Call the roll_dice function
roll_dice(6)

#27 Run the program. python NumberGuess.py




  