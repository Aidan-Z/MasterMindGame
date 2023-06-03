import random
levels = 8

options = ['r', 'g', 'b', 'p', 'o', 'y']
print(f"your potential options are: {options}")
combo = random.sample(options, 4)
board = ['_' for i in combo]

while levels >=0:

    user_input = input("give 4 from letters: ").lower()
    guess = [i for i in user_input]
    print(f"you guessed: {guess}")


    for i in guess:
        if i in combo:
            x = combo.index(i)
            board[x] = i
    print(board)
    levels -= 1
    print(levels)

    if board == combo and levels >0:
        print('game over you win')
        levels -= 10
    if board != combo and levels == 0:
        print("game over")
