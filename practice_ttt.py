# write your code here
s = list(input("Enter cells: "))
print('---------')
i = 0
while i < 7:
    print('|', s[i], s[i + 1], s[i + 2],'|')
    i += 3
print('---------')

def check_bingo():
    win = 0
    winner = ""
    for i in range(0, 9, 3):
        if s[i] == s[i + 1] == s[i + 2]:
            win += 1
            winner = s[i]
    for i in range(3):
        if s[i] == s[i + 3] == s[i + 6]:
            win += 1
            winner = s[i]
    for i in range(1, 2):
        if s[4 - 2 * i] == s[4] == s[4 + 2 * i]:
            win += 1
            winner = s[4]
    return win, winner

def check_error(win):
    count_O = 0
    count_X = 0
    space = 0
    for i in range(9):
        if s[i] == 'O':
            count_O += 1
        elif s[i] == 'X':
            count_X += 1
    if (count_O - count_X) ** 2 >= 4:
        print("Impossible")
    elif win == 0:
        for i in range(9):
            if s[i] == "_":
                space += 1
                print("Game not finished")
                return 1
        if space == 0:
            print("Draw")
            return 1
    return 0
            
def tic_tac_toe():
    win, winner = check_bingo()
    if (win > 1):
        print("Impossible")
    elif check_error(win) == 0 and winner != "" and win == 1:
        print(winner, "wins")
        
tic_tac_toe()
