import random as rand

# Global variables
limit = 548.0
limit_percent = 0.36
n = 3
board = [None] * n * n
winner = None
turn = bool(rand.getrandbits(1))
    
def setup():
    size(600, 600)
    background(255, 255, 255)
    noFill()

def draw():
    if  winner == None and any(item == None for item in board):
        if turn == False:
            (turn_index, turn_steps) = next_move(n, board, turn)
            (adversary_index, adversary_steps) = next_move(n, board, not turn)
            if turn_steps <= adversary_steps:
                index = turn_index
            else:
                index = adversary_index
            if index != None:
                set_turn(turn, index)
        draw_board()
    else:
        textSize(32)
        text('Empate' if winner == None else 'Ganador: Jugador 1' if winner else 'Ganador: PC', limit / 2 - 80, limit / 2 + 32)
        fill(0, 0, 0)
    
def mouseReleased():
    print("MOUSE X: {}, Y: {}".format(mouseX, mouseY))    
    if winner == None and any(item == None for item in board) and turn == True:
        index = get_index(mouseX, mouseY)
        print("index: {}".format(index))
        if board[index] == None:
            set_turn(turn, index)
            
def draw_board():
    # y
    line(200, 26, 200, 574)
    line(400, 26, 400, 574)
    # x
    line(26, 200, 574, 200)
    line(26, 400, 574, 400)
    
def get_index(x, y):
    index = 0 if x / limit <= limit_percent else 1 if x / limit <= limit_percent * 2 else 2
    index += 0 if y / limit <= limit_percent else 3 if y / limit <= limit_percent * 2 else 6
    return index

def drawTurn(turn, index):
    base = 26
    margin = limit_percent * 2
    x_bias = 18 + margin if index == 2 or index == 5 or index == 8 else 12 - margin if index == 1 or index == 4 or index == 7 else 4
    y_bias = 4 if index <= 2 else 12 - margin if index <= 5 else 18 + margin
    x = base * x_bias
    y = base * y_bias
    print("x -> {} y -> {}".format(x, y))
    if turn:
        circle(x, y, 100)
    else:
        line(x - base * 2, y - base * 2, x + base * 2, y + base * 2)
        line(x - base * 2, y + base * 2, x + base * 2, y - base * 2)
            
def set_turn(player_turn, index):
    global turn, winner
    drawTurn(player_turn, index)
    board[index] = player_turn
    winner = verify_winner(n, board)
    turn = not turn
    
def verify_winner(n, board):
    # Verify main diag
    if board[0] == board[4] == board[8]:
        return board[0]
    # Verify sec diag
    if board[2] == board[4] == board[6]:
        return board[2]
    # Verify rows
    for index in range(0, n * n, 3):
        if board[index + 0] == board[index + 1] == board[index + 2]:
            return board[index + 0]
    # Verify columns
    for index in range(n):
        if board[index + 0] == board[index + 3] == board[index + 6]:
            return board[index + 0]

def lower_steps_move(n, movements, turn):
    selected_steps = n * n
    selected_index = None
    for moves, index in movements:
        (winner, steps) = moves
        if steps <= selected_steps and winner == turn:
            selected_steps = steps
            selected_index = index
    return (selected_index, selected_steps)

def next_move(n, board, turn):
    next_movements = []
    for index in range(n * n):
        if board[index] == None:
            next_board = board[:]
            next_board[index] = turn
            next_movements.append((generate_moves(n, next_board, not turn), index))
        
    (index, steps) = lower_steps_move(n, next_movements, turn)
    if index == None:
        return lower_steps_move(n, next_movements, None)
    
    return (index, steps)

def generate_moves(n, board, turn, steps = 0):
    winner = verify_winner(n, board)
    if any(item == None for item in board) and winner == None:
        for index in range(n * n):
            if board[index] == None:
                board[index] = turn
                return generate_moves(n, board, not turn, steps + 1)
    return (winner, steps)
        
