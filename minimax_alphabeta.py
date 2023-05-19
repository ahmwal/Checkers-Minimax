from auxil import *

def randomPlayer(state, p):
    possibleMoves = getPossibleMoves(p, state)
    mv = random.randint(0, len(possibleMoves)-1)
    return possibleMoves[mv]

def minimax(state, max, alpha, beta, currentDepth, maxdepth):
    possibleMoves = getPossibleMoves(max, state)
    if (currentDepth == maxdepth or checkWin(max, state) or possibleMoves == []):
        _, _, h = getBoardValue(max, state)
        return h, state
    
    if(max == "B"):
        bestValue = -math.inf
        moveValue = 0
        bestMove = []
        for m in possibleMoves:      
            moveValue, _ = minimax(m, "W", alpha, beta, currentDepth+1, maxdepth)
            if (moveValue >= bestValue):
                bestValue = moveValue
                bestMove = copy.deepcopy(m)
                
            if (moveValue < beta):
                beta = moveValue
            
            if (alpha >= beta): 
                break
            
        return moveValue, bestMove
                
    if(max == "W"):
        bestValue = math.inf
        moveValue = 0
        bestMove = []
        for mv in possibleMoves:
            moveValue, _ = minimax(mv, "B", alpha, beta, currentDepth+1, maxdepth)
            if (moveValue <= bestValue):
                bestValue = moveValue
                bestMove = copy.deepcopy(mv)
                
            if (moveValue > alpha):
                alpha = moveValue
                
            if (alpha >= beta):
                break
                   
        return moveValue, bestMove