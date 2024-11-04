import random

def game(): 
    print ("welcome to rock , paper , scissor ")
    print("0 = paper , 1 = rock , 2 = scissor ")
    player_win =0
    bot_win = 0
    draw =0
    
    
    while True:
        x = int (input("please input a number "))
        y = (0,1,2)

        def get_random():
            return random.choice(y)
        if  x  not in y:
            print ("input is invalid")
        else:
            choices = {0: "Paper", 1: "Rock", 2: "Scissors"}
            print(f"You chose: {choices[x]}")
            print(f"Computer chose: {choices[get_random()]}")

        if x == get_random():
            print("It's a tie!")
            draw +=1
        elif (x == 0 and get_random() == 1) or (x == 1 and get_random() == 2) or (x == 2 and get_random() == 0):
            print("You win!")
            player_win +=1

        else:
            print("You lose!")
            bot_win +=1

    
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again not in ["yes", "y"]:
            print("Thanks for playing! Goodbye!")
            print(f"player win: {player_win}, bot win: {bot_win}, draw: {draw}")
            break
game()