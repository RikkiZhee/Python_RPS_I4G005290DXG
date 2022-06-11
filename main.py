import random

Player = input("Enter a choice (R, P , S): ")
possible_actions = ["rock", "paper", "scissors"]
CPU = random.choice(possible_actions)
print(f"\nYou chose {Player}, computer chose {CPU}.\n")

if Player == CPU:
    print(f"Both players selected {Player}. It's a tie!")
elif Player == "R":
    if CPU == "S":
        print("You win!")
    else:
        print(" You lose.")
elif Player == "P":
    if CPU == "R":
        print(" You win!")
    else:
        print(" You lose.")
elif Player == "S":
    if CPU == "S":
        print(" You win!")
    else:
        print(" You lose.")

while True:
    Player = input("Enter a choice (R, P, S): ")
    possible_actions = ["R", "P", "S"]
    CPU = random.choice(possible_actions)
    print(f"\nYou chose {Player}, computer chose {CPU}.\n")

    if Player == CPU:
        print(f"Both players selected {Player}. It's a tie!")
    elif Player == "R":
        if CPU == "S":
            print("You win!")
        else:
            print(" You lose.")
    elif Player == "P":
        if CPU == "R":
            print(" You win!")
        else:
            print("You lose.")
    elif Player == "scissors":
        if CPU == "paper":
            print("You win!")
        else:
            print("You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
