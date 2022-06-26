import random

user_action = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock" , "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYout chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! Yout Win!")
        else:
             print("Paper covers rock! Yout lose.")

elif user_action == "paper":
    if computer_action =="rock":
        print("Paper covers rock! You win!")
    else:
            print("Scissors cuts paper! Yout lose.")

elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You Win!")
    else:
            print("Rock smashes scissors! You lose.")
