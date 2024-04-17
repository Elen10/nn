import random

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def play_game():
    while True:
        input("Press Enter to roll the dice...")
        dice1, dice2 = roll_dice()
        total = dice1 + dice2
        print("You rolled:", total)
        
        if total == 7 or total == 11:
            print("You win!")
            return
        elif total == 2 or total == 3 or total == 12:
            print("Casino wins!")
            return
        else:
            print("Your goal is to roll", total)
            point = total
            while True:
                input("Press Enter to roll the dice...")
                dice1, dice2 = roll_dice()
                total = dice1 + dice2
                print("You rolled:", total)
                
                if total == point:
                    print("You rolled your goal! You win!")
                    return
                elif total == 7:
                    print("You rolled a 7. Casino wins!")
                    return

print("Welcome to the dice game!")
while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break
print("Thanks for playing!")