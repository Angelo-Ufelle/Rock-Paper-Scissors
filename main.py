import random

while True:
    possible_options = ["R", "P", "S"]
    computer_choice = random.choice(possible_options)

    def repeat():
        global user_choice
        user_choice = input("Enter a choice (R for rock, P for paper, S for scissors): ")
    repeat()

    while(user_choice not in possible_options):
        print("wrong option\n")
        repeat()

    print(f"\n Player {user_choice} : CPU {computer_choice} .\n")
    if user_choice == computer_choice:
        print(f"Both Players selected {user_choice}. its a tie!")

    elif user_choice == "R":
        if computer_choice == "S":
            print("Player wins!!, CPU loses")
        else:
            print("Player loses, CPU wins!!")
    elif user_choice == "P":
        if computer_choice == "R":
            print("Player wins!!, CPU loses")
        else:
            print("Player loses, CPU wins!!")
    elif user_choice == "S":
        if computer_choice == "P":
            print("Player wins!!, CPU loses")
        else:
            print("Player loses, CPU wins!!")
    play_again = input("Play again? (y/n)")

    if play_again.lower() != "y":
        break
    
        