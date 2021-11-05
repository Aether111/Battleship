#Grand Battleship Simulator

#The overall purpose of this code is to play battleship

#Enjoy!

#Imports
import random as rand
import sys

#Making sure that the user is on Idle Python
try: color = sys.stdout.shell
except AttributeError: raise RuntimeError('Use Idle Python to Run')

#Color Definitions
green = 'STRING'
black = 'SYNC'
red = 'COMMENT'
orange = 'KEYWORD'
blue = 'DEFINITION'
purple = 'BUILTIN'
    
#play
#Checks if you would like the computer to play for you
def play():
    play = input('Would you like the computer to play for you? Enter 1 for yes and 2 for no:')
    while play.isnumeric() == False:
        printer('Not a number...\nYou need numbers.')
        play = input('Would you like the computer to play for you? Enter 1 for yes and 2 for no:')
    play = int(play)
    while play != 1 and play != 2:
        printer('It has to be 1 OR 2.')
        play = input('Would you like the computer to play for you? Enter 1 for yes and 2 for no:')
        while play.isnumeric() == False:
            printer('Not a number...\nYou need numbers.')
            play = input('Would you like the computer to play for you? Enter 1 for yes and 2 for no:')
        play = int(play)
    return play

#printer
#Makes the program's prints purple
def printer(s):
    color.write(s,purple)
    print('')

if play == 1:
    printer('FINDING SUBSTITUTION...')

def level():
    level = input('Would you like gameplay to be easy, medium or hard?')
    while level.isnumeric():
        printer('I am not asking for numbers!')
        level = input('Would you like gameplay to be easy, medium or hard?')
    level = level.lower()
    while level != 'easy' and level != 'medium' and level != 'hard':
        printer('Thats not a level.')
        level = input('Would you like gameplay to be easy, medium or hard?')
        while level.isnumeric():
            printer('I am not asking for numbers!')
            level = input('Would you like gameplay to be easy, medium or hard?')
        level = level.lower()
    return level

#get_size
#This function gets the width of the board
def get_size():
    w = input('What do you want the side length of your board to be?')
    while w.isnumeric() == False:
        printer('Side lengths need to be a number.')
        w = input('What do you want the side length of your board to be?')
    w = int(w)
    while w < 6 or w > 25:
        printer('You almost broke my computer!')
        w = input('What do you want the side length of your board to be?')
        while w.isnumeric() == False:
            printer('Side lengths need to be a number.')
            w = input('What do you want the side length of your board to be?')
        w = int(w)
    return w

#direction
#This function gets user to choose horizontal or vertical
def direction():
    t = input('Please input 1 for the ship to be vertical or 2 for horizontal:')
    while t.isnumeric() == False:
        printer('That was invalid.')
        t = input('Please input 1 for the ship to be vertical or 2 for horizontal:')
    t = int(t)
    while t != 1 and t != 2:
        printer('That was not 1 and it was not 2')
        t = input('Please, 1 for vertical 2 for horizontal:')
        while t.isnumeric() == False:
            printer('That is pretty annoying')
            t = input('Please, either 1 for vertical 2 for horizontal:')
        t = int(t)
    return t


#get_coord
#This function gets a coordinate
def get_coord(val,name):
    n = input('Please input the starting ' + name + ' coordinate for the ship:')
    while n.isnumeric() == False:
        printer('Your ' + name + ' input was not numeric; Please try again.')
        n = input('Please input the starting ' + name + ' coordinate for the ship:')
    n = int(n) - 1
    while n not in range(0,w - val):
        printer('That was out of range.')
        n = input('Please input the starting ' + name + ' coordinate for the ship:')
        while n.isnumeric() == False:
            printer('Your ' + name + ' input was not numeric; Please try again.')
            n = input('Please input the starting ' + name + ' coordinate for the ship:')
        n = int(n) - 1
    return n

#place_ships
#Places computer ships and player ships
def place_ships(board,random):
    if random == False:
        for p in range(5):
            printer('You have to place ' + str(ship_number[p]) + ' ships of length ' + str(p + 1))
    #5 length
    for r in range(ship_number[4]):
        if random == False:
            print_board(board)
            printer('You are placing a ship of length five')
        done = False
        t = rand.randint(1,2)
        if random == False:
            t = direction()
        if t == 1:
            while done == False:
                done = True
                x = rand.randint(0,w - 5)
                y = rand.randint(0,w - 1)
                if random == False:
                    x = get_coord(4,'x')
                    y = get_coord(0,'y')
                for p in range(5):
                    if board[x + p][y] > 0:
                        if random == False:
                            printer('Make sure ships do not collide.')
                        done = False
            for p in range(5):
                board[x + p][y] = 5
        else:
            while done == False:
                done = True
                x = rand.randint(0,w - 1)
                y = rand.randint(0,w - 5)
                if random == False:
                    x = get_coord(0,'x')
                    y = get_coord(4,'y')
                for p in range(5):
                    if board[x][y + p] > 0:
                        if random == False:
                            printer('Make sure ships do not collide.')
                        done = False
            for p in range(5):
                board[x][y + p] = 5
    #4 length        
    for r in range(ship_number[3]):
        if random == False:
            print_board(board)
            printer('You are placing a ship of length four')
        done = False
        t = rand.randint(1,2)
        if random == False:
            t = direction()
        if t == 1:
            while done == False:
                done = True
                x = rand.randint(0,w - 4)
                y = rand.randint(0,w - 1)
                if random == False:
                    x = get_coord(3,'x')
                    y = get_coord(0,'y')
                for p in range(4):
                    if board[x + p][y] > 0:
                        if random == False:
                            printer('Make sure ships do not collide.')
                        done = False
            for p in range(4):
                board[x + p][y] = 4
        else:
            while done == False:
                done = True
                x = rand.randint(0,w - 1)
                y = rand.randint(0,w - 4)
                if random == False:
                    x = get_coord(0,'x')
                    y = get_coord(3,'y')
                for p in range(4):
                    if board[x][y + p] > 0:
                        if random == False:
                            printer('Make sure ships do not collide.')
                        done = False
            for p in range(4):
                board[x][y + p] = 4
    #3 length      
    for r in range(ship_number[2]):
        if random == False:
            print_board(board)
            printer('You are placing a ship of length three')
        done = False
        t = rand.randint(1,2)
        if random == False:
            t = direction()
        if t == 1:
            while done == False:
                done = True
                x = rand.randint(0,w - 3)
                y = rand.randint(0,w - 1)
                if random == False:
                    x = get_coord(2,'x')
                    y = get_coord(0,'y')
                for p in range(3):
                    if board[x + p][y] > 0: 
                        done = False
                    if y > 0:
                        if board[x + p][y - 1] == 3:
                            done = False
                    if y < w - 1:
                        if board[x + p][y + 1] == 3:
                            done = False
                    if x + p + 1 < w - 1:
                        if board[x + p + 1][y] == 3:
                            done = False
                    if x - 1 > 0:
                        if board[x - 1][y] == 3:
                            done = False
                    if random == False and done == False:
                        printer('Make sure ships do not collide.')
            for p in range(3):
                board[x + p][y] = 3
        else:
            while done == False:
                done = True
                x = rand.randint(0,w - 1)
                y = rand.randint(0,w - 3)
                if random == False:
                    x = get_coord(0,'x')
                    y = get_coord(2,'y')
                for p in range(3):
                    if board[x][y + p] > 0:
                        done = False
                    if x > 0:
                        if board[x - 1][y + p] == 3:
                            done = False
                    if x < w - 1:
                        if board[x + 1][y + p] == 3:
                            done = False
                    if y + p + 1 < w - 1:
                        if board[x][y + p + 1] == 3:
                            done = False
                    if y - 1 > 0:
                        if board[x][y - 1] == 3:
                            done = False
                    if random == False and done == False:
                        printer('Make sure ships do not collide.')
            for p in range(3):
                board[x][y + p] = 3
    #2 length   
    for r in range(ship_number[1]):
        if random == False:
            print_board(board)
            printer('You are placing a ship of length two')
        done = False
        t = rand.randint(1,2)
        if random == False:
            t = direction()
        if t == 1:
            while done == False:
                done = True
                x = rand.randint(0,w - 2)
                y = rand.randint(0,w - 1)
                if random == False:
                    x = get_coord(1,'x')
                    y = get_coord(0,'y')
                for p in range(2):
                    if board[x + p][y] > 0:
                        if random == False:
                            printer('Make sure ships do not collide.')
                        done = False
            for p in range(2):
                board[x + p][y] = 2
        else:
            while done == False:
                done = True
                x = rand.randint(0,w - 1)
                y = rand.randint(0,w - 2)
                if random == False:
                    x = get_coord(0,'x')
                    y = get_coord(1,'y')
                for p in range(2):
                    if board[x][y + p] > 0:
                        if random == False:
                            printer('Make sure ships do not collide.')
                        done = False
            for p in range(2):
                board[x][y + p] = 2
    #1 length  
    for r in range(ship_number[0]):
        if random == False:
            print_board(board)
            printer('You are placing a ship of length one')
        x = rand.randint(0,w - 1)
        y = rand.randint(0,w - 1)
        if random == False:
            x = get_coord(0,'x')
            y = get_coord(0,'y')
        while board[x][y] > 0:
            if random == False:
                printer('Make sure ships do not collide.')
            x = rand.randint(0,w - 1)
            y = rand.randint(0,w - 1)
            if random == False:
                x = get_coord(0,'x')
                y = get_coord(0,'y')
        board[x][y] = 1
    for y_coordinate in range(w):
        for x_coordinate in range(w):
            computer_board[x_coordinate][y_coordinate] = player_hide_board[x_coordinate][y_coordinate]

#print_board
#Prints all boards in the game
def print_board(board):
    print('')
    if board == computer_board:
        printer('YOUR SHIPS...')
    elif board == player_board:
        printer('ENEMY SHIPS...')
    elif board == computer_hide_board:
        printer('HIDDEN ENEMY SHIPS...')
    print('     ',end = '')
    for n in range(w):
        if n + 1 < 10:
            space = 3
        else:
            space = 1
        if n == w - 1:
            print(str(n + 1), end = '')
            print('')
            
        else:
            print(str(n + 1) + ' ' * space,end = '')
    # Function continued
    space = 3
    for m in range(w):
        if m + 1 >= 10:
            space = 1
        color.write(str(m + 1) + ' ' * space,green)
        for n in range(w):
            current_color = blue
            if board[m][n] == '*':
                current_color = orange
            elif board[m][n] == '!':
                current_color = red
            elif board[m][n] == 'x':
                current_color = purple
            elif str(board[m][n]).isnumeric():
                if board[m][n] > 0:
                    current_color = black
            color.write(str(board[m][n]) + '   ', current_color) 
        print('')
    print('')

#player_shot
#Player takes a shot
def player_shot():
    printer("Choose a coordinate to shoot the enemy's ship.")
    r = input('Choose the row:')
    #Checks if the player wants to use cheats
    if r == 'cheats':
        printer('Here is the list of cheats!')
        printer("Reset Game\nBlow Up Ship\nNuke\nSuicide Bot Win\nShoot Ship\nMiss Shot\nCant Miss\nShow Ships\n")
        i = input('Choose one:')
        i = i.lower()
        b = 0
        while i != 'reset game' and i != 'blow up ship' and i != 'nuke' and i != 'suicide bot win' and i != 'shoot ship' and i != 'miss shot' and i != 'cant miss' and i != 'show ships':
            i = input('Choose one of the listed cheats:')
            b += 1
            while i.isnumeric():
                i = input('These cheats do not consist of numbers:')
            i = i.lower()
        if i == 'reset game':
            printer('\nGame has been reset.\n')
            reset_game()
        elif i == 'blow up ship':
            p = input('A ship of what length would you like to blow up?')
            while p.isnumeric() == False:
                p = input("That was not a number.\nDon't make me regret allowing cheats!!!:")
                b += 1
                if b == 2:
                    printer("Don't push it")
                elif b == 3:
                    printer('I hate you')
                elif b == 4:
                    printer('You are this close!!!')
                elif b == 5:
                    printer("Alright you're done!")
                    1/0
            p = int(p)
            while p > 5 or p < 1:
               p = input('Come on man!\nRead the rules:')
               b += 1 
               while p.isnumeric() == False:
                   p = input('Come on man!\nRead the rules:')
                   b += 1
                   if b == 5:
                       printer("Alright you're done!")
                       1/0
               p = int(p) 
               if b == 2:
                   printer("Don't push it")
               elif b == 3:
                   printer('I hate you')
               elif b == 4:
                   printer('You are this close!!!')
               elif b == 5:
                   printer("Alright you're done!")
                   1/0
            color.write('HOMING MISSILE LAUNCHED' + '\n',red)
            for a in range(w):
                for b in range(w):
                    if computer_hide_board[a][b] == p:
                        player_board[a][b] = '*'
                        ship_sunk(a,b,player_board,computer_hide_board,True)
                        if p == 3:
                            if a + 1 <= w - 1:
                                if computer_hide_board[a + 1][b] == p:
                                    for x in range(2):
                                        player_board[a + x + 1][b] = '*'
                                    ship_sunk(a,b,player_board,computer_hide_board,True)
                                    return
                            for x in range(2):
                                player_board[a][b + x + 1] = '*'
                            ship_sunk(a,b,player_board,computer_hide_board,True)
                            return
        elif i == 'nuke':
            printer('NUKE LAUNCHED')
            printer('EVACUATE FRIENDLY VESSELS FROM THE AREA')
            for a in range(w):
                for b in range(w):
                    if computer_hide_board[a][b] > 0:
                        player_board[a][b] = '*'
                        ship_sunk(a,b,player_board,computer_hide_board,True)
                    else:
                        player_board[a][b] = '#'
            printer('ENEMY FLEET ANNIHILATED')
        elif i == 'suicide bot win':
            printer('Commiting Suicide...')
            for a in range(w):
                for b in range(w):
                    if player_hide_board[a][b] > 0:
                        computer_board[a][b] = '*'
                        ship_sunk(a,b,computer_board,player_hide_board,False)
                    else:
                        computer_board[a][b] = '#'
        elif i == 'shoot ship':
            s = input('What size ship would you like to shoot at?')
            while s.isnumeric() == False:
                s = input('It has to be a number between 1 and 5:')
            s = int(s)
            while s > 5 or s < 1:
                s = input('Between 1 and 5:')
                while s.isnumeric == False:
                    s = input('Stop it, put a number 1 - 5:')
                s = int(s)
            for a in range(w):
                for b in range(w):
                    if computer_hide_board[a][b] == s and player_board[a][b] != '*' and player_board[a][b] != '!':
                        player_board[a][b] = '*'
                        ship_sunk(a,b,player_board,computer_hide_board,True)
                        return
        elif i == 'miss shot':
            a = rand.randint(0,w - 1)
            b = rand.randint(0,w - 1)
            while computer_hide_board[a][b] != 0 or player_board[a][b] == 'x':
                a = rand.randint(0,w - 1)
                b = rand.randint(0,w - 1)
            player_board[a][b] = 'x'
            return
        elif i == 'cant miss':
            printer('DEPLOYING RECON')
            for a in range(w):
                for b in range(w):
                    if computer_hide_board[a][b] == 0:
                        player_board[a][b] = 'x'
            print_board(player_board)
            player_shot()
        elif i == 'show ships':
            printer('ACCESSING RADAR')
            print_board(computer_hide_board)
            player_shot()
    #Continues for regular shot
    else:
        c = input('Choose the column:')
        while r.isnumeric() == False or c.isnumeric() == False:
            r = input('Row, Only integers!!!:')
            c = input('Column, Only integers!!!:')
        r = int(r) - 1
        c = int(c) - 1
        while r < 0 or c < 0 or r >= w or c >= w:
            r = input('Not valid, Choose the row:')
            c = input('Not valid, Choose the column:')
            while r.isnumeric() == False or c.isnumeric() == False:
                r = input('Row, Only integers!!!:')
                c = input('Column, Only integers!!!:')
            r = int(r) - 1
            c = int(c) - 1
        if computer_hide_board[r][c] > 0:   
            f = rand.randint(1,2)
            if f == 1:
                printer("That's a hit!")
            else:
                printer('Nice aim!')
            player_board[r][c] = '*'
            ship_sunk(r,c,player_board,computer_hide_board,True)
            print_board(player_board)
            win(player_board, computer_hide_board,True)
            player_shot()
        else:
            v = rand.randint(1,2)
            if v == 1:
                printer("Don't shoot the fish!!!")
            else:
                printer('Firing squad, correct your aim!')
            player_board[r][c] = 'x'

#random_shot
#Computer takes a random shot
def random_shot():
    printer('The enemy is taking a shot!')
    if level == 'medium':
        if intelligent_hit_shot():
            return
    r = rand.randint(0,w - 1)
    c = rand.randint(0,w - 1)
    while computer_board[r][c] == '*' or computer_board[r][c] == '!' or computer_board[r][c] == 'x':
        r = rand.randint(0,w - 1)
        c = rand.randint(0,w - 1)
    shot_check(r,c)

#player_search_shot
#When computer plays for player, it takes an intelligent search shot
def player_search_shot():
    printer('You are taking a shot!')
    if intelligent_player_hit_shot():
        return
    m = rand.randint(1,4)
    r = rand.randint(0,w - 1)
    c = rand.randint(0,w - 1)
    if m == 1:
        for a in range(w):
            for b in range(w):
                if computer_hide_board[a][b] > 0 and player_board[a][b] == '?':
                    printer('Thats a hit!')
                    player_board[a][b] = '*'
                    print_board(player_board)
                    if intelligent_player_hit_shot():
                        return
                    player_search_shot()
    while player_board[r][c] != '?':
        r = rand.randint(0,w - 1)
        c = rand.randint(0,w - 1)
    player_shot_check(r,c)

#intelligent_search_shot
#The computer searches for ships with higher accuracy
def intelligent_search_shot():
    printer('The enemy is taking a shot!')
    if intelligent_hit_shot():
        return
    m = rand.randint(1,3)
    r = rand.randint(0,w - 1)
    c = rand.randint(0,w - 1)
    if m == 1:
        for a in range(w):
            for b in range(w):
                if player_hide_board[a][b] > 0 and str(computer_board[a][b]).isnumeric():
                    printer('The enemy has shot you!')
                    computer_board[a][b] = '*'
                    print_board(computer_board)
                    if intelligent_hit_shot():
                        return
                    intelligent_search_shot()
    while str(computer_board[r][c]).isnumeric() == False:
        r = rand.randint(0,w - 1)
        c = rand.randint(0,w - 1)
    shot_check(r,c)

#intelligent_hit_shot
#If the computer has any hits that aren't a sunken ship, it will search around there
def intelligent_hit_shot():
    for a in range(w):
        for b in range(w):
            if computer_board[a][b] == '*': 
                v = rand.randint(1,4)
                if a < w - 1:
                    if computer_board[a + 1][b] == '*':
                        for x in range(3):
                            if a < w - 2 - x:
                                if str(computer_board[a + x + 2][b]).isnumeric() and computer_board[a + 2][b] != 'x' and computer_board[a + 2][b] != '!':
                                    shot_check(a + x + 2,b)
                                    return True
                                else:
                                    for y in range(3):
                                        if a > y:
                                            if str(computer_board[a - y - 1][b]).isnumeric() and computer_board[a - 1][b] != 'x' and computer_board[a - 1][b] != '!':
                                                shot_check(a - y - 1,b)
                                                return True
                if b < w - 1:
                    if computer_board[a][b + 1] == '*':
                        for x in range(3):
                            if b < w - 2 - x:
                                if str(computer_board[a][b + x + 2]).isnumeric() and computer_board[a][b + 2] != 'x' and computer_board[a][b + 2] != '!':
                                    shot_check(a,b + x + 2)
                                    return True
                                else:
                                    for y in range(3):
                                        if b > y:
                                            if str(computer_board[a][b - y - 1]).isnumeric() and computer_board[a][b - 1] != 'x' and computer_board[a][b - 1] != '!':
                                                shot_check(a,b - y - 1)
                                                return True
                                                
                done = False
                while done == False:
                    if v == 1 and a > 0:
                        if str(computer_board[a - 1][b]).isnumeric():
                            shot_check(a - 1,b)
                            done = True
                    if v == 2 and a < w - 1:
                        if str(computer_board[a + 1][b]).isnumeric():
                            shot_check(a + 1,b)
                            done = True
                    if v == 3 and b > 0:
                        if str(computer_board[a][b - 1]).isnumeric():
                            shot_check(a,b - 1)
                            done = True
                    if v == 4 and b < w - 1:
                        if str(computer_board[a][b + 1]).isnumeric():
                            shot_check(a,b + 1)
                            done = True
                    v = rand.randint(1,4)
                return  True
    return False

#intelligent_player_hit_shot
#Same as intelligent_hit_shot but this plays for the player when they want to watch the game
def intelligent_player_hit_shot():
    for a in range(w):
        for b in range(w):
            if player_board[a][b] == '*': 
                v = rand.randint(1,4)
                if a < w - 1:
                    if player_board[a + 1][b] == '*':
                        for x in range(3):
                            if a < w - 2 - x:
                                if player_board[a + x + 2][b] == '?' and player_board[a + 2][b] != '!' and player_board[a + 2][b] != 'x':
                                    player_shot_check(a + x + 2,b)
                                    return True
                                else:
                                    for y in range(3):
                                        if a > y:
                                            if player_board[a - y - 1][b] == '?' and player_board[a - 1][b] != '!' and player_board[a - 1][b] != 'x':
                                                player_shot_check(a - y - 1,b)
                                                return True
                if b < w - 1:
                    if player_board[a][b + 1] == '*':
                        for x in range(3):
                            if b < w - 2 - x:
                                if player_board[a][b + x + 2] == '?' and player_board[a][b + 2] != '!' and player_board[a][b + 2] != 'x':
                                    player_shot_check(a,b + x + 2)
                                    return True
                                else:
                                    for y in range(3):
                                        if b > y:
                                            if player_board[a][b - y - 1] == '?' and player_board[a][b - 1] != '!' and player_board[a][b - 1] != 'x':
                                                player_shot_check(a,b - y - 1)
                                                return True
                                                
                done = False
                while done == False:
                    if v == 1 and a > 0:
                        if player_board[a - 1][b] == '?':
                            player_shot_check(a - 1,b)
                            done = True
                    if v == 2 and a < w - 1:
                        if player_board[a + 1][b] == '?':
                            player_shot_check(a + 1,b)
                            done = True
                    if v == 3 and b > 0:
                        if player_board[a][b - 1] != '?':
                            player_shot_check(a,b - 1)
                            done = True
                    if v == 4 and b < w - 1:
                        if player_board[a][b + 1] == '?':
                            player_shot_check(a,b + 1)
                            done = True
                    v = rand.randint(1,4)
                return True
    return False        
                        
#shot_check
#Checks shots for the computer
def shot_check(r,c):
    if player_hide_board[r][c] > 0:
        printer('The enemy has shot you!')
        computer_board[r][c] = '*'
        ship_sunk(r,c,computer_board,player_hide_board,False)
        print_board(computer_board)
        if level == 'easy':
            win(computer_board, player_hide_board,False)
            random_shot()
        elif level == 'medium' or level == 'hard':
            win(computer_board, player_hide_board,False)
            intelligent_hit_shot()
    else:
        printer('They are naive towards our whereabouts!')
        computer_board[r][c] = 'x'

#player_shot_check
#Checks the player's shot on autonomous mode
def player_shot_check(r,c):
    if computer_hide_board[r][c] > 0:
        printer('Thats a hit!')
        player_board[r][c] = '*'
        ship_sunk(r,c,player_board,computer_hide_board,True)
        print_board(player_board)
        win(player_board, computer_hide_board,True)
        intelligent_player_hit_shot()
    else:
        printer('Were not trying to spot fish!')
        player_board[r][c] = 'x'

#ship_sunk
#Checks if ships are sunk
def ship_sunk(x,y,board,hide_board,player):
    s = hide_board[x][y]
    north = y + 1
    south = y - 1
    east = x + 1
    west = x - 1
    copy_board = [[board[b][a] for a in range(w)]for b in range(w)]
    copy_board[x][y] = '!'
    if x != 0:
        while hide_board[west][y] == s:
            if board[west][y] != '*' and board[west][y] != '!':
                return
            if west < 0:
                break
            copy_board[west][y] = '!'
            west -= 1
    if x != w - 1:
        while hide_board[east][y] == s:
            if board[east][y] != '*' and board[east][y] != '!':
                return
            copy_board[east][y] = '!'
            east += 1
            if east > w - 1:
                break
    if y != 0:
        while hide_board[x][south] == s:
            if board[x][south] != '*' and board[x][south] != '!':
                return
            if south < 0:
                break
            copy_board[x][south] = '!'
            south -= 1
    if y != w - 1:
        while hide_board[x][north] == s:
            if board[x][north] != '*' and board[x][north] != '!':
                return
            copy_board[x][north] = '!'
            north += 1
            if north > w - 1:
                break
    if player == True:
        if computer_hide_board[x][y] == 2:
            printer('You sunk their patrol boat!')
        elif computer_hide_board[x][y] == 3:
            printer('You sunk a destroyer!')
        elif computer_hide_board[x][y] == 4:
            printer('You annihilated their cruiser')
        elif computer_hide_board[x][y] == 5:
            printer('You sunk their battleship')
        r = rand.randint(0,4)
        hit_print = ["That's a lot of damage!",'You have caused major damage to their fleet!','You are getting closer to victory!',"Don't let your country down, keep fighting!",'See you on the ocean floor.']
        printer(hit_print[r])
    else:
        r = rand.randint(1,2)
        if r == 1:
            printer('The enemy sunk one of your ships!')
        else:
            printer('Did you know that these tin cans cost money?!')
        
    for y_coordinate in range(w):
        for x_coordinate in range(w):
            board[x_coordinate][y_coordinate] = copy_board[x_coordinate][y_coordinate]

#win
#Win and Lose section
def win(board,hide_board,player):
    for y in range(w):
        for x in range(w):
            if hide_board[x][y] != 0 and board[x][y] != '!':
                return
    if player == True:
        printer("Congratulations!, You've won!!!")
        print_board(computer_hide_board)
        i = input('Would you like to lead your people to victory again? Enter 1 for Yes or 2 for No:')
        if i == '1':
            reset_game()
        elif i == '2':
            printer('How sad. How could you abdicate?')
            exit()
        else:
            printer('Another wrong input could make you forfeit your title, be careful.')
            i = input('Would you like to lead your people to victory again? Enter 1 for Yes or 2 for No:')
            if i == '1':
                reset_game()
            elif i == '2':
                printer('How sad. How could you abdicate?')
                exit()
            else:
                while True:
                    printer('Please make your way to the exit.')
                    exit()
    else:
        print_board(computer_board)
        printer("You are the worst admiral ever!\nYou don't get the option to return to battle!")
        raise GeneratorExit 

#reset_game
#Resets the game when called
def reset_game():
    for y in range(w):
        for x in range(w):
            computer_hide_board[x][y] = 0
            player_board[x][y] = '?'
            computer_board[x][y] = '?'
            player_hide_board[x][y] = 0
    play_game()

#play_game
#For game play
def play_game():

    print_board(player_board)

    place_ships(computer_hide_board,True)

    i = input('Input 1 to randomly place your ships or enter 2 to put them manually:')
    while i.isnumeric() == False:
        printer('Numbers Only')
        i = input('Input 1 to randomly place your ships or enter 2 to put them manually:')
    i = int(i)
    while i != 1 and i != 2:
        printer('1 or 2')
        i = input('Input 1 to randomly place your ships or enter 2 to put them manually:')
        while i.isnumeric() == False:
            printer('Numbers Only')
            i = input('Input 1 to randomly place your ships or enter 2 to put them manually:')
        i = int(i)
    if i == 1:
        printer('Randomly Placing Ships...')
        place_ships(player_hide_board,True)
        
    else:
        place_ships(player_hide_board,False)

    print_board(player_hide_board)

    while True:
        if play == 1:
            print_board(player_board)

            player_search_shot()
        else:
            print_board(player_board)
            
            player_shot()

        win(computer_board, player_hide_board,False)
        
        print_board(player_board)

        win(player_board, computer_hide_board,True)

        if level == 'hard':
            intelligent_search_shot()
        else:
            random_shot()

        print_board(computer_board)

        win(computer_board, player_hide_board,False)

#Beginning of play
play = play()

level = level()

w = get_size()

k = w //2

ship_number = [round(k * 0),round(k * 0.2),round(k * 0.4),round(k * 0.2),round(k * 0.2)]

player_board = [['?' for x in range(w)]for y in range(w)]

computer_hide_board = [[0 for x in range(w)]for y in range(w)]

computer_board = [[0 for x in range(w)]for y in range(w)]

player_hide_board = [[0 for x in range(w)]for y in range(w)]

space = 1

play_game()

