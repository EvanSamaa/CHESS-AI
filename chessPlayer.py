from chessPlayer_library import *
from chessPlayer_tree import *
def GameBotRand ():
	Proxy = chessBoard() 
	Proxy.initialize()
	board = Proxy.returnB()
	done = False
	turn = 0
	while not done:
		printB(board)
		player = (turn%2)*10+10
		illegal = 0
		move1 = 0
		move2 = 0
		secondtry = False #tell me whether to send the error statement
		while illegal < 2:
			if secondtry == True:#extra
				print "you just did something wrong, smart up"
			illegal = 0 
			if player == 10:
				#move1 = raw_input("white player enter pos1 >")
				#move2 = raw_input("white player enter pos2 >")
				raw_input("The bot 10 is gove to make a move!")
				illegal = 2
				moves = bot(board, player)
				#moves = chessPlayer(board, genOp(player))[1]
				
			if player == 20:
				raw_input("The bot 20 is going to make a move!")
				illegal = 2
                                import time#timerrrrr
                                start = time.time()
                                moves = chessPlayer(board,(player))
				moves = moves[1]
                                end = time.time()
                                print end - start#timerrrrr
                                #testT(k)
			move1 = moves[0]
			move2 = moves[1]
			#move2 = int(move2)
			#move1 = int(move1)
			posPlayer = GetPlayerPositions(board, player)
			for i in posPlayer:
				if move1 > 63:
					break
				if move1 == i:
					illegal = illegal + 1
					break
			if move1 < 63 and move1 >= 0:
				legalMove = GetPieceLegalMoves(board, move1)
			if type(legalMove) != int:
				for i in legalMove:
					if i == move2:
						illegal = illegal + 1
						break
			if illegal < 2:#so extra
				secondtry = True
		move(board, move1, move2)
		if checkstate(board) != 2:
			done = True
		turn = turn + 1	

def bot(board, player):
	acum = []
	
	pos = GetPlayerPositions(board, player)
	for i in pos:
		LM = GetPieceLegalMoves(board, i)
		for k in LM:
			acum = acum + [[i, k]]
	
	i = 0
	while (i < len(acum)):
		if IsPositionUnderThreat(board, acum[i][0],player):
			acum = acum[0:i-1] + acum[i+1:]
		i = i + 1
	from random import randint
	move = randint(0, len(acum) - 1)
	return acum[move]
def chessPlayer(board, player): 
	status = False
	move = 0
	node = 0
	candidateMoves = []
	start = 0 
	positions = GetPlayerPositions(board, player)
        pos = GetPlayerPositions(board, player)
        for i in pos:
        	LM = GetPieceLegalMoves(board, i)
                for k in LM:
                         candidateMoves = candidateMoves + [[i, k]]
	if positions == [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]:
		return [status, [51, 43], candidateMoves, []]
	elif positions == [43, 48, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]: 
		return [status, [58, 44], candidateMoves, []]
	elif positions == [43, 44, 48, 49, 50, 52, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63]:
		return [status, [59, 51], candidateMoves, []]
	elif positions == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
		return [status, [11, 19], candidateMoves, []]
	elif positions == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 19]:
		return [status, [2,20], candidateMoves, []]			
	elif positions == [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 19, 20]:
		return [status, [3,11], candidateMoves, []]
	else:
		node = botTree(board, player)
		rtv = evaltree(node, player)
		move = rtv[0]
		status = True
		candidateMoves = [candidateMoves, rtv[2]]
		node = node.Get_LevelOrder2()	
	return [status, move, candidateMoves, node]
def botTree(board, player):
	head = tree(board)
	botTree_DivergePieces(board, player, head, 1, 4)
	return head

def botTree_DivergePieces(board, player, head, depth, setDepth):
	pos = GetPlayerPositions(board, player)
	if depth < setDepth:
		for i in pos: 
			botTree_GenTree(board, i, head, depth, setDepth )
	return 0	
def botTree_GenTree(board, pos, Head, depth, setDepth):
	if depth <= setDepth:
		player = (board[pos] - board[pos]%10)
		keys = GetPieceLegalMoves(board, pos)
		for i in keys:
			proxy = list(board)
			move(proxy, pos, i)
			node = tree(proxy)
			node.store[2] = [pos, i]
			Head.add(node)	
			botTree_DivergePieces(proxy, genOp(player), node, depth + 1, setDepth)
def evaltree (node, player):
	valOfNode = []
	moves = []
	for i in range (0, len(node.store[1])):
		valOfNode = valOfNode + [alphabeta(node.store[1][i], 2, -1000000, 1000000, player, player), ]
		moves = moves + [node.store[1][i].store[2]]
	maxval = valOfNode[0]
	maxi = 0
	board = node.store[0]
	for i in range(1, len(valOfNode)):
		proxy = list(board)
		move(proxy, moves[i][0], moves[i][1])
		queen = getQueen(proxy, player)
		if not IsPositionUnderThreat(proxy, queen, player): 
			if valOfNode[i] > maxval:
				maxi = i	
				maxval = valOfNode[i]
	if maxval == valOfNode[0]:
		from random import randint
		maxi = randint(0, len(valOfNode)-1)	
	return [moves[maxi], moves, valOfNode]
def getQueen(proxy, player):
        for j in range (0, 63):
 		if proxy[j]%player == 4:
                	return j
	return -1	
def alphabeta (node, depth, alpha, beta, me, player):
	if depth == 6 or node.store[1] == []:
		return genValueOfBoard(node.store[0], me)
			
	if player == me:
		v = -100000
		for i in node.store[1]:
			k = alphabeta(i, depth + 1, alpha, beta, me, genOp(player))
			if k > v:
				v = k
			if alpha < v:
				alpha = v
			if beta <= alpha:
				break
		return v
	else:
		v = 100000	
		for i in node.store[1]:
			k = alphabeta(i, depth + 1, alpha, beta, me, player)
                        if k < v:
                                v = k
                        if beta > v:
                                beta = v
                        if beta <= alpha:
                                break
		return v
			

def genValueOfBoard (board, player):
        myPieces = GetPlayerPositions(board, player)
        sumMe = sumUp(board, myPieces)
	yourPieces = GetPlayerPositions (board, genOp(player))
	sumYou = sumUp(board, yourPieces)
	killCount = sumMe - sumYou
	KeyPlayers = []
	for i in myPieces:
		if board[i]%10 > 1 and board[i]%10 < 5:
			KeyPlayers = KeyPlayers + [i]
	pos = getQueen(board, player)
	if pos == -1:
		killCount = killCount - 500
	for i in KeyPlayers:
		killCount = killCount + len(GetPieceLegalMoves(board, i))
	return killCount
	
def sumUp(board, pieces):
	counter = 0
	for i in pieces:
		val = board[i]%10
#		counter = counter + ((board[i]%10)+1)
		if val == 1:
			counter = counter + 1
		elif val == 2 or val == 1:
			counter = counter + 3
		elif val == 3:
			counter = counter + 5
		elif val == 4:
			counter = counter + 9
		elif val == 5:
			counter = counter + 20
	counter = counter * 100	
	return counter
	
def checkstate(board):
	count = 0
	for i in range(0, 63):
		if board[i] == 15 or board[i] == 25:
			count = count + 1
	return count

GameBotRand()
