import random


def get_computer_choice():
    """Computer randomly chooses rock, paper, or scissors"""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def determine_winner(player, computer):
    """Determine who wins the game"""
    if player == computer:
        return "It's a tie!"

    # Player wins
    if (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        return "You win! 🎉"

    # Computer wins
    return "Computer wins! 💻"


def play_game():
    """Main game loop"""
    print("🎮 Rock Paper Scissors Game!")
    print("-" * 30)

    player_score = 0
    computer_score = 0

    while True:
        print("\nChoose: rock, paper, or scissors (or 'quit' to exit)")
        player_choice = input("Your choice: ").lower()

        if player_choice == "quit":
            print(f"\nFinal Score - You: {player_score}, Computer: {computer_score}")
            print("Thanks for playing!")
            break

        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()

        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)

        # Update scores
        if "You win" in result:
            player_score += 1
        elif "Computer wins" in result:
            computer_score += 1

        print(f"Score - You: {player_score}, Computer: {computer_score}")


if __name__ == "__main__":
    play_game()
