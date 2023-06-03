import random

options = ['R', 'G', 'B', 'P', 'O', 'Y']
print(f"Color Options:\n{options}\n")

combo = random.sample(options, 4) #random 4 colors

level = 1 #player attempts left
def check(guess): #function, takes in 'guess' (list of users 4 letter input)
    count = 0 #variable to store correct letters in guess vs -> combo
    board = ['_' for i in combo]

    for i in guess: #for letters in user guess
        if i in combo: #if letter in guess

            x = combo.index(i) #get index of correct letter (exp: combo=rgby, guess=rfff, x=0 )
            board[x] = i #change '-' with correct letter

            count += 1  # for each correct letter add 1 to letters
    print(f"{count} of the letters you guessed are in the code")
    return board


while level <=8: #while still have attempts left

    print(f"Level: {level}")

    # print(combo)
    user_input = input("Guess 4 individual letters: ").upper() #user input letters
    guess = [i for i in user_input] #convert to list 'guess'

    game_board = check(guess)


    # switch order of these
    if game_board == combo:
        print(game_board)
        print(combo)
        print('YOU WIN')
        level += 10
    elif game_board != combo and level > 0:
        level += 1
    elif game_board != combo and level == 0:
        print('GAME OVER')
