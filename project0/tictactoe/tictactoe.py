# https://cs50.harvard.edu/ai/2020/projects/0/tictactoe/
# Using Minimax, implement an AI to play Tic-Tac-Toe optimally.
# Done by JemboDev (Alexander Saprygin) @ 15.10.20

"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None

MAX_VALUE = 1
MIN_VALUE = -1


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    total_x, total_o = 0, 0

    for row in board:
        total_x += row.count(X)
        total_o += row.count(O)

    if total_x > total_o:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    set_of_actions = set()

    for row_index, row in enumerate(board):
        for cell_index, cell in enumerate(row):
            if cell == EMPTY:
                set_of_actions.add((row_index, cell_index))

    return set_of_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Deep copy of the original board to modify it instead
    result_board = deepcopy(board)

    # Getting current turn
    turn = player(board)

    row, column = action[0], action[1]

    if board[row][column] != EMPTY:
        raise Exception('Invalid action!')

    result_board[row][column] = turn

    return result_board


def check_rows(board):
    """
    Returns winner by row
    """
    for row in board:
        if len(set(row)) == 1 and row[0] is not None:
            return row[0]

    return None


def check_columns(board):
    """
    Returns winner by column
    """
    # Some weird logic goes here
    # But overall it iterates through columns first
    for column_index, column in enumerate(board):
        win_set = set()
        for row_index, _ in enumerate(column):
            win_set.add(board[row_index][column_index])
        if len(win_set) == 1 and board[0][column_index] is not None:
            return board[0][column_index]

    return None


def check_diagonals(board):
    """
    Returns winner by diagonal
    """
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]
    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
        return board[0][len(board)-1]

    return None


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    row_winner = check_rows(board)
    if row_winner is not None:
        return row_winner

    column_winner = check_columns(board)
    if column_winner is not None:
        return column_winner

    return check_diagonals(board)


def is_filled(board):
    """
    Returns True if all cells have been filled
    """
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False

    return True


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or is_filled(board):
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    champ = winner(board)

    if champ == X:
        return 1

    if champ == O:
        return -1

    return 0


def max_value(board, alpha, beta):
    """
    Returns highest possible value of the given board
    """
    best_value = MIN_VALUE

    if terminal(board):
        return utility(board)

    for action in actions(board):
        best_value = max(best_value, min_value(result(board, action), alpha, beta))
        alpha = max(alpha, best_value)
        if beta <= alpha:
            break

    return best_value


def min_value(board, alpha, beta):
    """
    Returns lowest possible value of the given board
    """
    best_value = MAX_VALUE

    if terminal(board):
        return utility(board)

    for action in actions(board):
        best_value = min(best_value, max_value(result(board, action), alpha, beta))
        beta = min(beta, best_value)
        if beta <= alpha:
            break

    return best_value


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # X - maximizing player
    # O - minimizing player
    current_player = player(board)
    action_value = {}
    alpha = MIN_VALUE
    beta = MAX_VALUE

    if terminal(board):
        return None

    if current_player == X:
        for action in actions(board):
            value = min_value(result(board, action), alpha, beta)
            action_value[action] = value

        highest_value = max(list(action_value.values()))

        return list(action_value.keys())[list(action_value.values()).index(highest_value)]

    if current_player == O:
        for action in actions(board):
            value = max_value(result(board, action), alpha, beta)
            action_value[action] = value

        lowest_value = min(list(action_value.values()))

        return list(action_value.keys())[list(action_value.values()).index(lowest_value)]
