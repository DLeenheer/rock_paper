print("Welcome to Rock, Paper, Scissors, with a twist!")
print("We will play 3 rounds of rock, paper, scissors today, loser has to perform an agreed upon task (e.g., run a mile)")
player_1_choice = input("Player 1 enter a choice (rock, paper, or scissors): ")
player_2_choice = input("Player 2 enter a choice (rock, paper, or scissors): ")
print("Player 1 chose " + player_1_choice + "and Player 2 chose " + player_2_choice + "!")
#this current version is just to complete the CS101 course project requirements, in the 'real world' I would adjust the above to account for misspelled entries, upper case entries, etc.
#I would also add the actual names of Player 1 and Player 2 to the program for the print messages

def play_game(player_1_choice, player_2_choice):
    count = 0
    while count < 3:
        if player_1_choice == player_2_choice:
            print("Both players selected {p1}. It's a tie, go again.".format(p1 = player_1_choice))
            break
        elif player_1_choice == "rock":
            if player_2_choice == "scissors":
                count += 1
                print("Rock smashes scissors! Player 1 wins the round!")
            else:
                count += 1
                print("Paper covers rock, Player 2 wins the round!")
        elif player_1_choice == "paper":
            if player_2_choice == "rock":
                count += 1
                print("Paper covers rock! Player 1 wins the round!")
            else:
                count += 1
                print("Scissors cut paper, Player 2 wins the round!")
        elif player_1_choice == "scissors":
            if player_2_choice == "paper":
                count +=1
                print("Scissors cut paper! Player 1 wins the round!")
            else:
                count += 1
                print("Rock smashes scissors, Player 2 wins the round!")
        else: print("Player in the lead wins! Loser has to do the task, better luck next time!")                                     
play_game(player_1_choice, player_2_choice) 
print("feel free to play again, new task this time!")

