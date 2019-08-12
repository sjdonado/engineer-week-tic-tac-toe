import random as rand

# Global variables
limit = 548.0
limit_percent = 0.36
n = 3
board = [None, None, None, None, None, None, None, None, None]
winner = None
turn = bool(rand.getrandbits(1))
    
def setup():
    size(600, 600)
    background(255, 255, 255)
    noFill()

def draw():
    draw_board()
    
def mouseReleased():
    print("MOUSE X: {}, Y: {}".format(mouseX, mouseY))
    if winner == None:
        (x_index, y_index, index) = get_index(mouseX, mouseY)
        print("x_index: {} y_index: {} index: {}".format(x_index, y_index, index))
        if board[index] == None:
            turn = False
            drawTurn(turn, x_index, y_index)
            # board[index] = turn

def draw_board():
    # y
    line(200, 26, 200, 574)
    line(400, 26, 400, 574)
    # x
    line(26, 200, 574, 200)
    line(26, 400, 574, 400)
    
def get_index(x, y):
    if x / limit <= limit_percent:
        x_index = 0
        index = 0
    elif x / limit <= limit_percent * 2:
        x_index = 1
        index = 1
    else:
        x_index = 2
        index = 2

    if y / limit <= limit_percent:
        y_index = 0
    elif y / limit <= limit_percent * 2:
        y_index = 1
        index += 3
    else:
        y_index = 2
        index += 6

    return (x_index, y_index, index)
    
def drawTurn(turn, x_index, y_index):
    base = 26
    x_bias = 2 if x_index == 0 else 6 if x_index == 1 else 9
    y_bias = 2 if y_index == 0 else 6 if y_index == 1 else 9
    x = base * x_bias
    y = base * y_bias
    print("x -> {} y -> {}".format(x, y))
    if turn:
        circle(x * 2, y * 2, 100)
    else:
        line(x * 2 - base, y * 2 - base, x * 2.2, y * 2.2)
        line(x * 2 - base, y * 2.2, x * 2.2, y * 2 - base)
        # line(x * 2, y, x, y * 2)
