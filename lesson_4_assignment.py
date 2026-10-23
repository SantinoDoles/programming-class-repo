from random import randrange

def main():
    play_again = "y"
    while play_again == "y":
        user_weapon = get_user_weapon()
        opponent_weapon = get_opponent_weapon()

        determine_winner(user_weapon, opponent_weapon)

        play_again = input("Want to play again (y/n): ")
        print("Completed by, Santino Doles")

def get_user_weapon():
            print("SELECT YOUR WEAPON (1-3)")
            print("--------------------------")
            print("1. ROCK")
            print("2. PAPER")
            print("3. SCISSORS")

            weapon = int(input("Enter Your Weapon: "))
            return weapon

def get_opponent_weapon():
       weapon = randrange(1, 4)
       return weapon

def determine_winner(user_weapon, opponent_weapon):
     if user_weapon == opponent_weapon:
              print("It's a tie!")
     elif user_weapon == 1 and opponent_weapon == 3:
              print("You win, rock crushes scissors!")
     elif user_weapon == 2 and opponent_weapon == 1:
              print("You win, paper covers rock!")
     elif user_weapon == 3 and opponent_weapon == 2:
              print("You win, scissors cuts paper!")
     else:
              print("You lose!")
if __name__ == "__main__":
        main()
