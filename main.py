#!/usr/bin/python
import random as rand

def print_board(n, board):
  items = [(' ' if item == None else 'o' if item else 'x') for item in board]
  draw = """
   {} | {} | {}
  -----------
   {} | {} | {}
  -----------
   {} | {} | {}
  """.format(*items)
  print("\n {} \n".format(draw))

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

def main():
  # n * n
  n = 3
  print("**** Tic tac toe (Made by sjdonado) ****")
  board = [None, None, None, None, None, None, None, None, None]
  turn = bool(rand.getrandbits(1))
  winner = None
  while(any(item == None for item in board) and winner == None):
    print_board(n, board)
    last_turn = turn
    turn = not last_turn
    print("=> Turno para {}".format('Jugador 1' if turn == True else 'PC'))
    if turn :
      while True:
        index = int(input("Ingrese posición: "))
        if index >= 0 and (index < n * n) and board[index] == None:
          break
    else:
      (turn_index, turn_steps) = next_move(n, board, turn)
      (adversary_index, adversary_steps) = next_move(n, board, not turn)
      if turn_steps <= adversary_steps:
        index = turn_index
      else:
        index = adversary_index

    board[index] = turn
    winner = verify_winner(n, board)

  print_board(n, board)
  print("RESULTADO: {}".format('Empate' if winner == None else 'Ganador: Jugador 1' if winner else 'Ganador: PC'))

if __name__ == "__main__":
  main()