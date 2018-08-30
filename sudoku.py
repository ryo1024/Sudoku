class Sudoku (object):
	"""docstring for Sudoku """
	empty = [[0 for _ in range(9)] for _ in range(9)]

	def __init__(self, sheet = empty):
		self.sheet = sheet
#   Abstraction 

	def show(self):
		for x in self.sheet:
			print(x)
		return
	def show_prob(self):
		for x in self.sheet:
			lst = []
			for y in x:
				lst += [y.probabilit]
			print(lst)


# Return Sudoku objects with list of Ind_cells according to 9 lines of user input 
	def sheet_input():
		q = []
		for _ in range(9):
			a = [int(x) for x in input()]
			q += [a]
		p = Sudoku(q)
		return Ind_cell.numtocell(p)
# Return the number in given index
	def search(self, row, column):
		return self.sheet[row][column]
# Return the row in given index
	def search_row(self, index):
		return self.sheet[index]
# Change the number in given index
	def update(self, row, column, number):
		self.sheet[row][column] = number
		return self
# Return Sudoku object consists of 9 columns
	def columns(self):
		p = []
		for x in range(9):
			q = []
			for y in range(9):
				q += [self.search(y, x)]
			p += [q]
		return Sudoku(p)
# Return Sudoku object consists of list of 9 cells
	def cells(self):
		p = []
		for y in [0,3,6]:
			q = []
			for z in [0,3,6]:
				q = []
				for x in range(z, z+3):
					q += self.search_row(x)[y:y+3]
				p += [q]
		return Sudoku(p)
# Used in method
	"""def zero_count(self):
		lst = []
		for row in self.sheet:
			count = 0
			for x in row:
				if x.number == 0:
					count += 1
			lst += [count]
		return lst

	def fofi_check(self):
		lst = []
		for row in self.sheet:
			num = 45 - sum([x.number for x in row])
			lst += [num]
		return lst"""


class Ind_cell(object):
	def __init__(self, number, Sudok, rown, columnn, celln):
		self.number = number
		self.Sudok = Sudok
		self.row = []
		self.column = []
		self.cell = [] 
		self.rown = rown
		self.columnn = columnn
		self.celln = celln
		self.probabilit = []

	def infoupdate(self):
		self.row = self.Sudok.search_row(self.rown)
		self.column = self.Sudok.columns().search_row(self.columnn)
		self.cell = self.Sudok.cells().search_row(self.celln)

	def cellnum(rown, columnn):
		celln = 0
		if 0 <= rown <= 2:
			celln += 0
		elif 3 <= rown <= 5:
			celln += 1
		elif 6 <= rown <= 8:
			celln += 2
		if 0 <= columnn <= 2:
			celln += 0
		elif 3 <= columnn <= 5:
			celln += 3
		elif 6 <= columnn <= 8:
			celln += 6
		return celln

	def numtocell(Sudok):
		for x in range(9):
			for y in range(9):
				Sudok.sheet[x][y] = Ind_cell(Sudok.search(x,y), Sudok, x, y, Ind_cell.cellnum(x, y))
		return Sudok

	"""def celltonum(Sudok):
		lst = []
		for x in range(9):
			lst2 = []
			for y in range(9):
				lst2 += [Sudok.search(x,y).number]
			lst += [lst2]
		return Sudoku(lst)"""

	def probability(self):
		lst = list(range(1,10))
		if self.number != 0:
			self.probabilit = []
			return []
		for x in self.column:
			try:
				lst.remove(x.number)
			except ValueError:
				pass
		for x in self.cell:
			try:
				lst.remove(x.number)
			except ValueError:
				pass
		for x in self.row:
			try:
				lst.remove(x.number)
			except ValueError:
				pass
		self.probabilit = lst
		return lst

	def hard_probability(self):
		lst = list(range(1,10))
		if self.number != 0:
			self.probabilit = []
			return []
		for x in self.column:
			try:
				lst.remove(x.number)
			except ValueError:
				pass
		for x in self.cell:
			try:
				lst.remove(x.number)
			except ValueError:
				pass
		for x in self.row:
			try:
				lst.remove(x.number)
			except ValueError:
				pass

		self.probabilit = lst
		two_two(self.row)
		print(self.probabilit)
		two_two(self.column)
		print(self.probabilit)
		two_two(self.cell)
		print(self.probabilit)
		samecell(self.cell)
		print(self.probabilit)
		return lst



	def __repr__(self):
		return str(self.number)
	def __str__(self):
		return str(self.number)

"""def replace_num(row, numold, numnew):
	for x in range(9):
		if row[x].number == numold:
			row[x].number = numnew
	return row[x]"""

def unique(lst):
	dic = {}
	for p in lst:
		dic[str(p)] = 0
	for p in lst:
		dic[str(p)] += 1
	for p in lst:
		if dic[str(p)] == 1:
			return p
	return False


"""def mathod_a(Sudok):
	for x in range(9):
		if Sudok.zero_count()[x] == 1:
			replace_num(Sudok.search_row(x), 0, Sudok.fofi_check()[x])

	return Sudok"""

def mathod_b(Sudok):
	for x in range(9):
		for y in range(9):
			print(Sudok.search(x,y).probabilit)
			if len(Sudok.search(x,y).probabilit) == 1:
				print("b", Sudok.search(x,y).probabilit,Sudok.search(x,y).rown,Sudok.search(x,y).columnn)
				Sudok.search(x,y).number = Sudok.search(x,y).probabilit[0]
				Sudok.search(x,y).probabilit = []
			Sudok.search(x,y).hard_probability()
	return Sudok

def mathod_c(Sudok):
	for p in Sudok.sheet:
		lst = []
		for q in p:
			if q.number == 0:
				lst += q.probabilit
		for q in p:
			if unique(lst) in q.probabilit:
				print("c", q.probabilit, q.rown, q.columnn)
				q.number = unique(lst)
				q.probabilit = []
			update2(Sudok)

	return Sudok

def mathod_d(Sudok):
	pass


#HELPER FUNCTIONS  FOR PROBABILIT

def two_two(p):
	for q in p:
		if len(q.probabilit) == 2:
			for w in p:
				if w is not q:
					if w.probabilit == q.probabilit:
						for z in p:
							if z is not w and z is not q:
								try:
									z.probabilit.remove(w.probabilit[0])
									z.probabilit.remove(w.probabilit[1])
								except ValueError:
									pass

def samecell(cell):
	for x in range(1,10):
		lst = []
		for p in cell:
			if x in p.probabilit:
				lst += [p.rown]
		if lst != [] and sum(lst) == lst[0] * len(lst):
			for q in p.row:
				try:
					q.probabilit.remove(x)
				except ValueError:
					pass




def update(Sudok):
	for p in Sudok.sheet:
		for q in p:
			q.infoupdate()


def update2(Sudok):
	for p in Sudok.sheet:
		for q in p:
			q.hard_probability()

def update2_new(Sudok):
	for p in Sudok.sheet:
		for q in p:
			q.probability()
	for p in Sudok.sheet:
		two_two(p)
	for q  in Sudok.columns().sheet:
		two_two(q)
	for z in Sudok.cells().sheet:
		two_two(z)
		samecell(z)


def solve(Sudok):
	update(Sudok)
	update2(Sudok)
	Sudok.show()
	print(0)
	for _ in range(3):
		#mathod_a(Sudok)
		#mathod_a(Sudok.columns())
		#mathod_a(Sudok.cells())
		mathod_b(Sudok)
		Sudok.show()
		print(0)
		mathod_c(Sudok)
		Sudok.show()
		print(0)
		mathod_c(Sudok.columns())
		Sudok.show()
		print(0)
		mathod_c(Sudok.cells())
		Sudok.show()
		print(0)
		update(Sudok)
		update2(Sudok)
	return Sudok


		

