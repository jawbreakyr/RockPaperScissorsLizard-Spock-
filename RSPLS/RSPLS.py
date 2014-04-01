"rock", "paper", "scissors", "lizard", "Spock"
import random


def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    else:
        name == "scissors"
        return 4

    
# convert a number to name function
def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    else:
        number == 4
        return "scissors"
    

def rpsls(player_choice):
    
    print " " 
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # computer picks a random number using randrange()
    comp_number = random.randrange(0, 5)
    # convert the computer's number to computer choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    difference = (comp_number - player_number) % 5
    # print out the message for the player's choice
    print "Player chooses", player_choice
    print "Computer chooses", comp_choice
    
    if difference == 1 or difference == 2:
        print "Computer wins!!"
    elif difference == 3 or difference == 4:
        print "Player wins!!"
    else:
        print "Player and Computer tie!"

"""	to play the game with raw_input remove the comment sign and
    comment out the next rpsls """
# rpsls(raw_input('Please select an input from the choices:"rock" "paper" "spock" "lizard" "scissors"'))
rpsls("rock")
rpsls("spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
