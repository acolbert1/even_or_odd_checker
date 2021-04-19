def even_or_odd_checker():
    initial_input = user_greeting()

    replay_yes = ["yes", "y"]
    replay_no = ["no", "n"]

    try:
        user_input = int(initial_input)
        print("The number youve inputted is ", user_input)
        if user_input % 2 == 0:
            print("This number is even")
        else:
            print("This number is odd")
        if user_input <= 0 or user_input > 1000:
            print("Please enter a number between 1 and 1000")
        replay = input("Would you like to play another round? ").lower()
        
        
        if replay not in replay_yes and replay not in replay_no:
                
                print("Please enter Yes, Y, No, or N.")
                while replay not in replay_yes and replay not in replay_no:
                    replay = input("that wasnt a valid entry Please enter Yes, Y, No, or N.  ").lower()

        if replay in replay_yes:
            print("lets play again")
            even_or_odd_checker()
        if replay in replay_no:
            print("Thanks for playing")
        
            
    except ValueError:
        print("This is not a number please try again.")
        even_or_odd_checker()

def user_greeting():
    initial_input = input("Welcome to the game. Please enter a number between 1 and 1000: ")
    return initial_input

even_or_odd_checker()

