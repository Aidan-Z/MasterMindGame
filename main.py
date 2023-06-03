import random

options = ['R', 'G', 'B', 'P', 'O', 'Y']
print(f"Color Options:\n{options}\n")

combo = random.sample(options, 4)

level = 1
def check(guess):
    count = 0
    board = ['_' for i in combo]

    for i in guess:
        if i in combo:

            x = combo.index(i)
            board[x] = i

            count += 1
    print(f"{count}/4 letters are in code")
    return board


while level <=8:
    print(f"Level: {level}")
    user_input = input("Guess 4 individual letters: ").upper()
    guess = [i for i in user_input]
    game_board = check(guess)

    if game_board == combo:
        print('YOU WIN')
        level += 10
    elif game_board != combo and level > 0:
        level += 1
    elif game_board != combo and level == 0:
        print('GAME OVER')
