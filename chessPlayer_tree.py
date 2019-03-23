from chessPlayer_library import *
class tree:

	def __init__ (self, board):
		self.store = [board, [], []]
	def add(self, x):
		self.store[1] = self.store[1] + [x]
		return True
	def Print_DepthFirst(self):
		return self.pr(self.store, 0)
	def prr(self, indents):
		return self.pr(self.store, indents)					
	def pr(self, thislist, indents):		
		spacing = ""
		for i in range (0, indents):
			spacing = spacing + "    "
		print spacing, thislist[0]
		for i in range (0, len(thislist[1])):
			try:
				thislist[1][i].prr(indents + 1)
			except:
				jj= 8
				print jj
		return -1
	def get(self):
		return self.store				
	def Get_LevelOrder(self):#now it shows levels as numbers in integers before each level
		q = queue()
		q.push(self.store)
		bag = [0]
		return self.Help(q, bag, 1)
	def Help(self, q, bag, num):
		jiji = q.getL()
		if jiji != 0:
			for i in range (0,jiji):
				jimmy = q.pop()
				bag = bag + [jimmy]
				try:
					for j in range(0, len(jimmy.store[1])):
						q.push(jimmy.store[1][j])
				except:
					for j in range(0, len(jimmy[1])):
						q.push(jimmy[1][j])
			bag = bag + [num]
			if num + 1 <= 4:
				return self.Help(q, bag, num + 1)
		return bag
 
        def Get_LevelOrder2(self):#now it shows levels as numbers in integers before each level
                q = queue()
                q.push(self.store)
                bag = [0]
                return self.Help2(q, bag, 1)
        def Help2(self, q, bag, num):
                jiji = q.getL()
                if jiji != 0:
                        for i in range (0,jiji):
                                jimmy = q.pop()
                                bag = bag + [jimmy]
                                try:
                                        for j in range(0, len(jimmy.store[1])):
                                                q.push(jimmy.store[1][j])
                                except:
                                        for j in range(0, len(jimmy[1])):
                                                q.push(jimmy[1][j])
                        bag = bag + [num]
                        if num + 1 <= 2:
                                return self.Help2(q, bag, num + 1)
                return bag

		
############################################################################		

class queue:
	def __init__(self):
		self.q = []
		self.length = 0
	def copy(self):
		rtval = queue()
		for i in range (0, self.length):
			rtval.push(self.q[i])
		return rtval
	def push(self, a):
		self.q = self.q + [a]
		self.length = self.length + 1
		return 0
	def pop(self):
		if len(self.q) != 0:
			self.length = self.length - 1
			tim = self.q[0]
			self.q = self.q[1:len(self.q)]
			return tim
		else:
			return -1
	def getL(self):
		return self.length
	def isemp(self):
		if self.getL == 0:
			return 0
		else:
			return -1
	def printf(self):
		print self.q
		return 0			





#mathew = tree(5)
#matthew = tree(6)
#Jimmy = tree(2)
#noah = tree(9)
#water = tree(6)
#head = tree(90)
#head.add(mathew)
#head.add(matthew)
#mathew.add(Jimmy)
#mathew.add(noah)
#noah.add(water)

#jiji = head.Get_LevelOrder()
#print jiji
#jiji[3].store[0] = "wewew"
#jiji = head.Get_LevelOrder()
#print jiji

	


