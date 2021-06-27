### function definitions ###

#  see if user wants to play game
def play_game(play_game_flag):   
    while True:
        play = input('Type "play" to play the game, "exit" to quit: ')
        
        if play == "play":
            return True
        elif play == "exit":
            quit()
        else:
            continue
    
#  check if user repeats a previous letter
def same_letter_twice(user_guess, previous_guess_list):
    if user_guess in previous_guess_list:
        print("You've already guessed this letter")
        return True
    else:
        previous_guess_list.append(user_guess)

#  make sure user enters a lowercase alphabet letter        
def check_lower_case(user_guess): 
    if not(97 <= ord(user_guess) <= 122): 
        print("Please enter a lowercase English letter")
        return True

#  check if user enters single character only    
def check_single_input(user_guess):
    if len(user_guess) != 1:
        print("You should input a single letter")
        return True

###  end functions ###

from random import choice

previous_guess_list = list()


print("H A N G M A N")

answer_list = ['python', 'java', 'kotlin', 'javascript']
answer = choice(answer_list)
hidden_answer = ["-" for _ in range(len(answer))]
attempts_counter = 8
play_game_flag = True

while play_game_flag == True:
    play_game_flag = play_game(play_game_flag)
    
    while attempts_counter != 0:
        print()
        print("".join(hidden_answer))
        user_guess = input("Input a letter: ")
    
        index_list = [int(x) for x, z in enumerate(answer) if z == user_guess]
    
        if check_single_input(user_guess) == True:
            continue    
    
        if same_letter_twice(user_guess, previous_guess_list) == True:
            continue
    
        if check_lower_case(user_guess) == True:
            continue
        
        if len(index_list) > 0:
            for x in index_list:
                if hidden_answer[x] == "-":
                    hidden_answer[x] = user_guess
                else:
                    print("No improvements")
                    attempts_counter -= 1
                    break
                if "-" not in hidden_answer:
                    print(hidden_answer)
                    print("You guessed the word!")
                    print("You survived!")
                    quit()
        else:
            print("That letter doesn't appear in the word")
            attempts_counter -= 1
        
    print("You lost!")
