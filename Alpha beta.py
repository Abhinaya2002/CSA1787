def alphabeta(self,node,depth,white, alpha,beta):
    ch = Chessgen()
    if(depth == 0 or self.is_end(node)):
        return self.stockfish_evaluation(node.board)


    if (white):
        value = Cp(-10000)
        for child in ch.chessgen(node):
            value = max(value, self.alphabeta(child,depth-1,False, alpha,beta))
            alpha = max(alpha, value)
            if (alpha >= beta):
                print("Pruned white")
                break
        return value

    else:
        value = Cp(10000)
        for child in ch.chessgen(node):
            value = min(value, self.alphabeta(child,depth-1,True, alpha,beta))
            beta = min(beta,value)
            if(beta <= alpha):
                print("Pruned black")
                break
        return value
