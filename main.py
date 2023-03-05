# My name  : Hossien Molladarband
# My Gmail : hossienprogrammer@gmail.com

# XO game :D


# Use Matrice !
#   --           --
#  | a11  a12  a13 |
#  | a21  a22  a23 |
#  | a31  a32  a33 |
#   --           --

import os

def clear(): # terminal clear
    os.system('cls')

def help_list(): # Show how to chose numbers
    help =  [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
    ]
    return help

def show_list(x): # creat a nice board for play
    '''x = youre list'''
    try:
        i = 0
        print('---------------')
        while i <= 2:
            j = 0
            while j <= 2:
                print('¦', x[i][j], end=' ¦')
                j += 1
            print()
            print('---------------')
            i += 1
    except Exception as error:
        print(error)

def one(x): # cheak win modes
    '''x = youre list'''
    #  --           --
    # | a11  a12  a13 |
    # | a21  a22  a23 |
    # | a31  a32  a33 |
    #  --           --
    try:
        a11 = x[0][0]
        a12 = x[0][1]
        a13 = x[0][2]
        a21 = x[1][0]
        a22 = x[1][1]
        a23 = x[1][2]
        a31 = x[2][0]
        a32 = x[2][1]
        a33 = x[2][2]
        if (a11 == a12) and (a12 == a13):
            return 1
        elif (a21 == a22) and (a22 == a23):
            return 2
        elif (a31 == a32) and (a32 == a33):
            return 3
        elif (a11 == a21) and (a21 == a31):
            return 4
        elif (a12 == a22) and (a22 == a32):
            return 5
        elif (a13 == a23) and (a23 == a33):
            return 6
        else:
            return False
    except Exception as error:
        print(error)

def two(x): #cheak win modes
    '''x = youre list'''
    #  --           --
    # | a11       a13 |
    # |      a22      |
    # | a31       a33 |
    #  --           --
    try:
        a11 = x[0][0]
        a13 = x[0][2]
        a22 = x[1][1]
        a31 = x[2][0]
        a33 = x[2][2]
        if (a11 == a22) and (a22 == a33):
            return 1
        elif (a13 == a22) and (a22 == a31):
            return 2
        else:
            False
    except Exception as error:
        print(error)

def cheack_equal(x) ->bool: # cheak equal mode
    '''x = youre list'''
    try:
        a11 = x[0][0]
        a12 = x[0][1]
        a13 = x[0][2]
        a21 = x[1][0]
        a22 = x[1][1]
        a23 = x[1][2]
        a31 = x[2][0]
        a32 = x[2][1]
        a33 = x[2][2]
        if (a11 == 'X') or (a11 == 'O'):
            if (a12 == 'X') or (a12 == 'O'):
                if (a13 == 'X') or (a13 == 'O'):
                    if (a21 == 'X') or (a21 == 'O'):
                        if (a22 == 'X') or (a22 == 'O'):
                            if (a23 == 'X') or (a23 == 'O'):
                                if (a31 == 'X') or (a31 == 'O'):
                                    if (a32 == 'X') or (a32 == 'O'):
                                        if (a33 == 'X') or (a33 == 'O'):
                                            return True
    except Exception as error:
        print(error)

def add(x, n, xo):
    '''x = youre list, n = youre number, xo = X or O'''
    try:
        if n == 1:
            x[0][0] = xo
            return True
        elif n == 2:
            x[0][1] = xo
            return True
        elif n == 3:
            x[0][2] = xo
            return True
        elif n == 4:
            x[1][0] = xo
            return True
        elif n == 5:
            x[1][1] = xo
            return True
        elif n == 6:
            x[1][2] = xo
            return True
        elif n == 7:
            x[2][0] = xo
            return True
        elif n == 8:
            x[2][1] = xo
            return True
        elif n == 9:
            x[2][2] = xo
            return True
    except Exception as error:
        print(error)   
        return False 

def player1_winner(player1, player2): # when player1 is winner
    player1[2] = player1[2] + 10
    player1[3] = player1[3] + 1         
    player2[2] = player2[2] - 5
    player2[4] = player2[4] + 1
    print('Winner Winner , {} has {}points, win: {}, lose: {}, equal: {} ;)'.format(player1[1], player1[2], player1[3], player1[4], player1[5]))
    print('Loser  Loser  , {} has {}points, win: {}, lose: {}, equal: {} ;)'.format(player2[1], player2[2], player2[3], player2[4], player2[5]))

def player2_winner(player1, player2): # when player2 is winner
    player1[2] = player1[2] - 5
    player1[4] = player1[4] + 1         
    player2[2] = player2[2] + 10      
    player2[3] = player2[3] + 1 
    print('Loser  Loser  , {} has {}points, win: {}, lose: {}, equal: {} ;)'.format(player1[1], player1[2], player1[3], player1[4], player1[5]))
    print('Winner Winner , {} has {}points, win: {}, lose: {}, equal: {} ;)'.format(player2[1], player2[2], player2[3], player2[4], player2[5]))

def equal(player1, player2): # when both equal
    player1[5] = player1[5] + 1
    player2[5] = player2[5] + 1
    player1[2] = player1[2] + 1
    player2[2] = player2[2] + 1
    print('Wow :| you are equal!, {} has {}points, win: {}, lose: {}, equal: {} ;)'.format(player1[1], player1[2], player1[3], player1[4], player1[5]))
    print('Wow :| you are equal!, {} has {}points, win: {}, lose: {}, equal: {} ;)'.format(player2[1], player2[2], player2[3], player2[4], player2[5]))

#               0          1       2       3       4       5
# player = ['X' or 'O', 'name', 'point', 'win', 'lose', 'equal']
player1 = ['X', 'name', 0, 0, 0, 0]
player2 = ['O', 'name', 0, 0, 0, 0]

player1[1] = input('What is youre name ? \n')
player2[1] = input('What is youre name ? \n')
print()
print('{} use X'.format(player1[1]))
print('{} use O'.format(player2[1]))
print()
print('Use number for replace X or O')
print('win = +10 point')
print('lose = -5 point')
print('equal = +1 point')
print()
print()

play_time = int(input('How many times do you want play ? \n'))

while play_time != 0:
    play_time -= 1
    game = True
    i = 2 # for change turn
    old = []
    main = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]
    while game == True:
        if (i % 2) == 0:
            show_list(main)
            q = int(input('{} number : '.format(player1[1])))
            clear()
            if old.count(q) == 0:
                old.append(q)
                cheack = add(main, q, player1[0])
                i += 1
                if one(main) == 1:
                    player1_winner(player1, player2)
                    game = False
                elif one(main) == 2:
                    player1_winner(player1, player2)
                    game = False
                elif one(main) == 3:
                    player1_winner(player1, player2)
                    game = False
                elif one(main) == 4:
                    player1_winner(player1, player2)
                    game = False
                elif one(main) == 5:
                    player1_winner(player1, player2)
                    game = False
                elif one(main) == 6:
                    player1_winner(player1, player2)
                    game = False
                elif two(main) == 1:
                    player1_winner(player1, player2)
                    game = False
                elif two(main) == 2:
                    player1_winner(player1, player2)
                    game = False
                elif cheack_equal(main) == True:
                    equal(player1, player2)
                    game = False
                else:
                    continue
            else:
                print('Chose another number please :) ')
                print()
        else:
            show_list(main)
            q = int(input('{} number : '.format(player2[1])))
            clear()
            if old.count(q) == 0:
                old.append(q)
                cheack = add(main, q, player2[0])
                i += 1
                if one(main) == 1:
                    player2_winner(player1, player2)
                    game = False
                elif one(main) == 2:
                    player2_winner(player1, player2)
                    game = False
                elif one(main) == 3:
                    player2_winner(player1, player2)
                    game = False
                elif one(main) == 4:
                    player2_winner(player1, player2)
                    game = False
                elif one(main) == 5:
                    player2_winner(player1, player2)
                    game = False
                elif one(main) == 6:
                    player2_winner(player1, player2)
                    game = False
                elif two(main) == 1:
                    player2_winner(player1, player2)
                    game = False
                elif two(main) == 2:
                    player2_winner(player1, player2)
                    game = False
                else:
                    continue
            else:
                print('Chose another number please :) ')
                print()
        
print()
print('Have a good time ;) ')
