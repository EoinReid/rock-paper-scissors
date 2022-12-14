# rock-paper-scissors
# Let user enter rock, paper or scissors move
# compare to computer move
# print winning move
import sys, random # import sys in order to use sys.exit(), and random to use randint()

# declare user variables for input, and to keep count of their wins, loses and draws.
user_input = ""
user_wins = 0
user_loses = 0
user_draws = 0

# functions
def user_make_a_move(user_input):
    move = { 
        "r":"rock",
        "p":"paper",
        "s":"scissors",
        "q":"quit",
        }
    user_move = move[user_input]
    return user_move

def computer_make_a_move():
    move = ["rock", "paper", "scissors"]
    computer_move = random.choice(move)
    return computer_move

# Rock-Paper-Scissors application

try:
    while user_input != "q": # as long as the user does not enter q
        print("ROCK, PAPER, SCISSORS..")
        print(str(user_wins) + " wins. " + str(user_loses) + " loses. " + str(user_draws) + " draws.") # scoreboard
        user_input = input("Enter a move: (r)ock (p)aper (s)cissors or (q)uit ")
        # create a dictionary that creates a key for each of the 4 user input possilities r, p, s and q so I can take the letter the user input and take a value based on it. e.g r = rock
        # also randomly generting an int 1 - 3 and assigning a value from this dictionary to randomly generate the computers move.
    
        user_move = user_make_a_move(user_input)
        computer_move = computer_make_a_move()
        
        if user_move == "quit":
                sys.exit(0)
        elif user_move == "rock" and computer_move == "scissors":
            print("You win! Rock beats scissors!")
            user_wins += 1
        elif user_move == "paper" and computer_move == "rock":
            print("You win! Paper beats scissors!")

            user_wins += 1
        elif user_move == "scissors" and computer_move == "paper":
            print("You win! Scissors beats papers!")

            user_wins += 1
        elif user_move == computer_move:
            print("Aw no, its a draw!")
            user_draws += 1
        else:
            print("RIP, you lose.")
            user_loses += 1
except SystemExit:
    print("Thanks for playing, goodbye!")
except:
    print("An error has occured, please try again.")

