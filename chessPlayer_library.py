class chessBoard:

	def __init__ (self):
		board = []
		for i in range (0, 8):
			for i in range (0, 8):
				board = board + [0]
		self.board = board

	def printf (self):
		for i in range (0, 8):
			for j in range (0, 8):
				print str(self.board[8*i + j]),
			print ""
	def initialize (self):
		self.board[0] = 13
		self.board[7] = 13
		self.board[1] = 11
		self.board[6] = 11
		self.board[2] = 12
		self.board[5] = 12
		self.board[3] = 14
		self.board[4] = 15
		for i in range (8, 16):
			self.board[i] = 10;
		
		self.board[56] = 23
		self.board[57] = 21
		self.board[58] = 22
		self.board[59] = 24
		self.board[60] = 25
		self.board[61] = 22
		self.board[62] = 21
		self.board[63] = 23
		for i in range (48, 56):
			self.board[i] = 20;
	def returnB(self):
		return self.board
def printB (board):
	for i in range (0, 8):
		if i%2 == 0:
			for j in range (0, 8):
				if j%2 == 0:
					if board[8*(7-i) + j] == 0:
						print "##",
					else:
							print str(board[8*(7-i)+j])+ "",
				elif j%2 == 1:
					if board[8*(7-i) + j] == 0:
						print "__",
					else:
						print str(board[8*(7-i)+j])+ "",
			print ""
		elif i%2 == 1:
			for j in range (0,8):
				if j%2 == 0:
					if board[8*(7-i) + j] == 0:
						print "__",
					else: 
						print str(board[8*(7-i)+j])+"",
				elif j%2 == 1:
					if board[8*(7-i) + j] == 0:
						print "##",
					else:
						print str(board[8*(7-i)+j])+ "",
			print ""
	return 0			
class stack:
	def __init__(self):
		self.store = []
	def push(self, val):
		self.store = self.store + [val]
	def pop(self):
		if not (self.isempty()):
			rtv = self.store[len(self.store)-1]
			self.store = self.store[0:len(self.store)-1]
			return rtv
		else:
			return -1
	def isempty(self):
		if self.store == []:
			return True
	def returnL(self):
		return self.store
def IsPositionUnderThreat (board, pos, player):
	enemies = stack()
	enemyMoves = []
	op = genOp(player)
	for i in range (0, 63):
		if board[i]/op == 1:
			enemies.push(i)
	while (not(enemies.isempty())):
		temp = enemies.pop()
		enemyMoves = enemyMoves + GetPieceLegalMoves(board, temp)
	for i in range(0, len(enemyMoves)):
		if enemyMoves[i] == pos:
			return True
	return False	

def GetPlayerPositions(board, player):
	rtL = []
	for i in range (0, 64):
		if board[i]/player == 1:
			rtL = rtL + [i]
	return rtL

def GetPieceLegalMoves(board, pos):
	player = 0
	if board[pos]/10 == 1:
 		player = 10
	elif board[pos]/20 == 1:
		player = 20
	if board[pos] == 0:
		return 0
	elif board[pos]%player == 0:
		return Legal_pawn(board, pos, player)
	elif board[pos]%player == 5:
		return Legal_king(board, pos, player)
	elif board[pos]%player == 3:
		return Legal_rook(board, pos, player)
	elif board[pos]%player == 2:
		return Legal_bish(board, pos, player)
	elif board[pos]%player == 4:
		return Legal_queen(board, pos, player)
	elif board[pos]%player == 1:
		return Legal_knight(board, pos, player)
def amIOcc(board, pos, player):
	rtv = True
	if (pos > 63 or pos < 0):
		return False
	if board[pos]/player == 1:
		rtv = False
	return rtv
def abs (num):
	if num < 0:
		return - num
	return num

def genOp(me):
	if me == 10:
		return 20
	if me == 20:
		return 10;
def Legal_knight_helper(board, posA, posB, player):
	check = True
	check = amIOcc(board, posB, player)
	if abs(posA%8- posB%8) >= 6:
		check = False
	return check
def Legal_knight(board, pos, player):
	rtl = []
	if Legal_knight_helper(board, pos, pos - 10, player):
		rtl = rtl + [pos - 10]
        if Legal_knight_helper(board, pos, pos - 17, player):
                rtl = rtl + [pos - 17]
        if Legal_knight_helper(board, pos, pos - 15, player):
                rtl = rtl + [pos - 15]
        if Legal_knight_helper(board, pos, pos - 6, player):
                rtl = rtl + [pos - 6]
        if Legal_knight_helper(board, pos, pos + 10, player):
                rtl = rtl + [pos + 10]
        if Legal_knight_helper(board, pos, pos + 17, player):
                rtl = rtl + [pos + 17]
        if Legal_knight_helper(board, pos, pos + 15, player):
                rtl = rtl + [pos + 15]
        if Legal_knight_helper(board, pos, pos + 6, player):
                rtl = rtl + [pos + 6]
     	return rtl

def Legal_queen(board, pos, player):
	rtl = []
	rtl = rtl + Legal_bish(board, pos, player)
	rtl = rtl + Legal_rook(board, pos, player)
	return rtl

def Legal_bish(board, pos, player):
	rtl = []
	i = 9
	while 1 == 1:
		if pos + i > 63:
			break
		if abs((pos+i-9)%8 - (pos + i)%8) == 7:
			break
		if amIOcc(board, pos + i, player):
			rtl = rtl + [pos + i]
			i = i + 9
		else: break
		if board[pos + i - 9] != 0:
			break
	i = -9 
	while 1 == 1:
                if pos + i < 0:
                        break
                if abs((pos+i+9)%8 - (pos + i)%8) == 7:
                        break
                if amIOcc(board, pos + i, player):
                        rtl = rtl + [pos + i]
                        i = i - 9
		else: 
			break
		if board[pos + i + 9] != 0:
			break
             
	i = 7
        while 1 == 1:
                if pos + i > 63:
                        break
                if abs((pos+i-7)%8 - (pos + i)%8) == 7:
                        break
                if amIOcc(board, pos + i, player):
                        rtl = rtl + [pos + i]
                        i = i + 7
		else:
			break
                if board[pos + i - 7] != 0:
			break
	i = -7
        while 1 == 1:
                if pos + i < 0:
                        break
                if abs((pos+i+7)%8 - (pos + i)%8) == 7:
                        break
                if amIOcc(board, pos + i, player):
                        rtl = rtl + [pos + i]
                        i = i - 7
		else:
			break
                if board[pos + i + 7] != 0:
			break
	return rtl
def Legal_rook(board, pos, player):
	rtl = []
	i = 1;
	while 1 == 1:
		if pos + i > 63:
			break
		if (pos/8 != (pos+i)/8):
			break
		if amIOcc(board, pos + i, player):
			rtl = rtl + [pos + i]
			i = i + 1
		else:
			break
		if board [pos + i -1] != 0:
			break
	i = -1
	while 1 == 1:
		if pos + i < 0:
			break
		if pos/8 != (pos + i)/8:
			break
		if amIOcc(board, pos + i, player):
			rtl = rtl + [pos + i]
			i = i - 1
		else:
			break
		if board [pos + i + 1]!= 0:
			break
	i = 1
	while 1 == 1:
		if pos + i*8 > 63:
			break
		if amIOcc(board, pos + i*8, player):
			rtl = rtl + [pos + (i*8)]
			i = i + 1
		else:
			break
		if board [pos + i*8 - 8] != 0:
			break
	i = -1
	while 1 == 1:
		if pos + i*8 < 0:
			break
		if amIOcc(board, pos + i*8, player):
			rtl = rtl + [pos +(i*8)]
			i = i - 1	
		else:
			break
		if board [pos + (i+1)*8] != 0:
			break
	return rtl
			
def Legal_king(board, pos, player):
	rtl = []
	for i in range (7,10):	
		if amIOcc(board, pos - i, player) and abs(pos%8 - (pos - i)%8)!= 7:
			rtl = rtl + [pos - i]
        for i in range (7,10):
                if amIOcc(board, pos + i, player) and abs(pos%8 - (pos + i)%8)!= 7:
                        rtl = rtl + [pos + i]

        if amIOcc(board, pos - 1, player) and abs(pos%8 - (pos - 1)%8)!= 7:
                        rtl = rtl + [pos - 1]

        if amIOcc(board, pos + 1, player) and abs(pos%8 - (pos + 1)%8)!= 7:
                        rtl = rtl + [pos + 1]
	return rtl	


def amIOccP(board, pos, player):
        rtv = True
        if (pos > 63 or pos < 0):
                return False
        if board[pos] == 0 or board[pos]/player == 1:
                rtv = False
        return rtv
 
def Legal_pawn(board, pos, player):
	rtl = []
	if player == 10:
		if pos + 8 < 63:
			if board[pos + 8] == 0:
				rtl = rtl + [pos+8]
		if amIOccP(board, pos + 7, player)and abs(pos%8 - (pos + 7)%8) != 7:
			rtl = rtl + [pos+7]
		if amIOccP(board, pos + 9, player) and abs(pos%8 - (pos + 9)%8) != 7:
			rtl = rtl + [pos+9]
	elif player == 20:
                if pos - 8 > 0:
			if board[pos - 8] == 0:
                        	rtl = rtl + [pos - 8]
                if amIOccP(board, pos - 7, player) and abs(pos%8 - (pos - 7)%8) != 7:
                        rtl = rtl + [pos - 7]
                if amIOccP(board, pos - 9, player) and abs(pos%8 - (pos - 9)%8) != 7:
                        rtl = rtl + [pos - 9]
	return rtl

def move (board, move1, move2):
	board[move2] = board[move1]
	board[move1] = 0
	return 0


