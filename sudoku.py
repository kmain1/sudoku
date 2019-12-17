from random import sample
import subprocess as sp
import copy

board=[[]]
correct_board=[[]]
def play():
    tmp = sp.call('clear',shell=True)

    global board
    global correct_board
    quit=False


    # init all to "."
    rows, cols = (10, 10) 
    board = [["."]*cols]*rows 

    # gets a unique solved board
    solve_board()
    correct_board=copy.deepcopy(board)
    # remove some values
    obscure()

    # start playing
    while(board_solved()==False and quit==False):
        print_board(board)
        move = input("Select a move.\nEX:A1:7\nEnter quit to exit.\n")
        if move=="quit":
            quit=True
            tmp = sp.call('clear',shell=True)
        else:
            try_move(move)
        tmp = sp.call('clear',shell=True)
    
    if(board_solved):
        print_board(board)
        input("Congratulations!  [ENTER]")

def solve_board():
    global board
    base  = 3
    side  = base*base

    def pattern(r,c): return (base*(r%base)+r//base+c)%side
    def shuffle(s): return sample(s,len(s)) 

    rBase = range(base) 
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,base*base+1))

    board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

    return board

def obscure():
    global board
    base = 3
    side = base*base
    squares = side*side
    empties = squares * 3//4
    for p in sample(range(squares),empties):
        board[p//side][p%side] = "."

    numSize = len(str(side))

def board_solved():
    global board
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j]==".":
                return False
    return True

def print_board(board):
    print("   1 2 3   4 5 6   7 8 9 ")
    print(" +-----------------------+")
    print_board_line(0, board)
    print_board_line(1, board)
    print_board_line(2, board)
    print(" |-------+-------+-------|")
    print_board_line(3, board)
    print_board_line(4, board)
    print_board_line(5, board)
    print(" |-------+-------+-------|")
    print_board_line(6, board)
    print_board_line(7, board)
    print_board_line(8, board)
    print(" +-----------------------+")

def print_board_line(row, board):
    letter="."
    if row==0:
        letter="A"
    elif row==1:
        letter="B"
    elif row==2:
        letter="C"
    elif row==3:
        letter="D"
    elif row==4:
        letter="E"
    elif row==5:
        letter="F"
    elif row==6:
        letter="G"
    elif row==7:
        letter="H"
    elif row==8:
        letter="I"
    print("{}| {} {} {} | {} {} {} | {} {} {} |".format(letter, board[row][0], board[row][1], board[row][2], board[row][3], board[row][4], board[row][5], board[row][6], board[row][7], board[row][8]))

def verify_move(move):
    try:
        move=move.split(":")
        space=move[0]
        value=move[1]
        letter=space[:1]
        pos=space[-1:]
        possible_letters=["A","B","C","D","E","F","G","H","I"]
        possible_num=["0","1","2","3","4","5","6","7","8","9"]
        if(letter in possible_letters):
            if(value in possible_num):
                if(pos in possible_num):
                    # vaiable option
                    return True
        return False

    except:
        return False

def correct_move(move):
    global board
    global correct_board
    move=move.split(":")
    space=move[0]
    move_value=move[1]
    letter=space[:1]
    pos=space[-1:]

    if(letter=="A"):
        row=0
    elif(letter=="B"):
        row=1
    elif(letter=="C"):
        row=2
    elif(letter=="D"):
        row=3
    elif(letter=="E"):
        row=4
    elif(letter=="F"):
        row=5
    elif(letter=="G"):
        row=6
    elif(letter=="H"):
        row=7
    elif(letter=="I"):
        row=8
    else: return False

    if(int(move_value)==correct_board[row][int(pos)-1]):
        board[row][int(pos)-1]=move_value
        return True
    return False
        
def try_move(move):
    if(verify_move(move)):
        # place move on board
        if(correct_move(move)):
            input("Correct!  [ENTER]")
        else:
            input("Incorrect.  [ENTER]")

    else:
        res=input("Invalid move... [ENTER]")

if __name__ == "__main__":
    # execute only if run as a script
    play()