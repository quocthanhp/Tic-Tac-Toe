"""
Tic Tac Toe Player
"""

import copy
import math
import sys

X = "X"
O = "O"
EMPTY = None
N = 3


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],]
def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX = 0
    countO = 0
    for i in range(N):
        countX = countX + board[i].count(X)
        countO = countO + board[i].count(O)
    
    if ((countX == 0 and countO == 0) or countX == countO):
        return X
    elif (countX > countO):
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(N):
        for j in range(N):
            if (board[i][j] is EMPTY):
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    (i, j) = action

    
    # invalid action
    if (i < 0 or j < 0 or i > N or j > N or board[i][j] is not EMPTY):
        raise ValueError((i, j))
    
    # resulting board
    resulting = copy.deepcopy(board)
    resulting[i][j] = player(board)
    return resulting
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # horizontal and vertical 
    for i in range(N):
        if board[i].count(X) == N or [board[j][i] for j in range(N)].count(X) == N:
            return X
        elif board[i].count(O) == N or [board[j][i] for j in range(N)].count(O) == N:
            return O

    # diagonal
    if [board[i][i] for i in range(N)].count(X) == N:
        return X

    if [board[i][i] for i in range(N)].count(O) == N:
        return O
    
    if [board[i][N-i-1] for i in range(N)].count(X) == N:
        return X
    
    if [board[i][N-i-1] for i in range(N)].count(O) == N:
        return O

    return None
        

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # there is winner
    if winner(board) is not None:
        return True

    # game is running
    for i in range(N):
        for j in range(N):
            if (board[i][j] is EMPTY):
                return False

    return True

p
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):    
        return None

    elif player(board) == X:
        val = -sys.maxsize - 1
        alpha = -sys.maxsize - 1
        beta = sys.maxsize

        for a in actions(board):
            alpha = minvalue(result(board, a), alpha, beta)
            if (alpha > val):
                val = alpha
                action = a
        return action
    
    elif player(board) == O:
        val = sys.maxsize
        alpha = -sys.maxsize - 1
        beta = sys.maxsize

        for a in actions(board):
            beta = maxvalue(result(board, a), alpha, beta)
            if (beta < val):
                val = beta
                action = a
        return action
        
        
def maxvalue(board, alpha, beta):
    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        alpha = max(alpha, minvalue(result(board, action), alpha, beta))
        if (alpha >= beta):
            return beta
    
    return alpha


def minvalue(board, alpha, beta):
    if terminal(board):
        return utility(board)

    for a in actions(board):
        beta = min(beta, maxvalue(result(board, a), alpha, beta))
        if (beta <= alpha):
            return alpha
    
    return beta