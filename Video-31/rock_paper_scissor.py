import random


def display_choice(choice):
    """Display ASCII art for the choice"""
    if choice == 0:  # Rock
        print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)
    elif choice == 1:  # Paper
        print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)
    elif choice == 2:  # Scissors
        print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)


def determine_winner(user, computer):
    """Determine the winner based on choices"""
    if user == computer:
        return "draw"
    # Winning combinations: (0 beats 2), (1 beats 0), (2 beats 1)
    if (user - computer) % 3 == 1:
        return "user"
    else:
        return "computer"


def get_user_choice():
    """Get and validate user input"""
    while True:
        try:
            choice = int(input("Enter your choice (0 for Rock, 1 for Paper, 2 for Scissors): "))
            if 0 <= choice <= 2:
                return choice
            print("Please enter 0, 1, or 2.")
        except ValueError:
            print("Please enter a valid number (0, 1, or 2).")


def play_game():
    """Main game function"""
    print("Welcome to Rock-Paper-Scissors!")
    print("Rules: Rock crushes scissors, scissors cut paper, paper covers rock.")

    user_choice = get_user_choice()
    computer_choice = random.randint(0, 2)

    print("\nYour choice:")
    display_choice(user_choice)

    print("Computer chose:")
    display_choice(computer_choice)

    result = determine_winner(user_choice, computer_choice)

    if result == "draw":
        print("It's a draw!")
    elif result == "user":
        print("You win! 🎉")
    else:
        print("You lose! 😢")


# Start the game
play_game()