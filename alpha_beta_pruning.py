'''
The following is a Python implementation of the Alpha-Beta pruning search 
algorithm.
'''
import math
#initialize values of MAX and MIN
MAX, MIN = float(math.inf), float(-math.inf)


def minimax(depth, nodeIdx, maxPlayer, vals, alpha, beta):
    '''
    Once the leaf node is reached, it returns the value of the node. 
    '''
    if depth == 3:
        return vals[nodeIdx]
    if maxPlayer:
        best = MIN
        #Traverse through left and right child of each parent node
        for i in range(0,2):
            val = minimax(depth+1, nodeIdx * 2 + i, False, vals, alpha, beta)
            
            best = max(best, val)
            
            alpha = max(alpha, best)
            
            '''
            Here is where the pruning occurs, since if the value of alpha exceeds the value
            of beta, there is no need to traverse the rest of the node and that path is done away with.
            ''' 
            if beta <= alpha:
                break
            
        return best
    
    else: 
        #if we're traversing upwards the search tree as minPlayer
        best = MAX
        #Traverse through left and right child of each parent node
        for i in range(0,2):
            val = minimax(depth+1, nodeIdx*2+i, True, vals, alpha, beta)
            
            best = min(best, val)
            
            beta = min(val, beta)
            
            if beta <= alpha:
                break
            
        return best

if __name__ == "__main__":
    vals = [3,12,8,2,6,-1,14,5,2]
    print("The optimal value of this search tree is:", minimax(0,0,True, vals, MIN, MAX))