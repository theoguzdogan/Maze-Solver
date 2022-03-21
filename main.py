import random

class coord:
	def __init__(self,x,y):
		self.x = x
		self.y = y

def get_values():
	line_row = input().split()
	line= int(line_row[0])
	row= int(line_row[1])
	matrix = []
	for i in range(line):
		matrix.append(input().split())

## Turns matrix elements into integers. If impossible, prints invalid and exits.
	for y in range(len(matrix)):
		for x in range(len(matrix[y])):
			try:
				matrix[y][x]=int(matrix[y][x])
			except:
				print("invalid")
				exit()

## Checks if all the matrix elements are whether 1 or 0, if not prints invalid and exits.
	for y in matrix:
		for x in y:
			if not (x==0 or x==1):
				print("invalid")
				exit()
			else:
				continue

	return matrix


def is_exit(matrix):
	row = len(matrix[0])-1
	line = len(matrix)-1
	cursor = coord(row,line)
	shadow = coord(cursor.x, cursor.y)
	deadlock_counter = 0
	move_counter = 0

	## If the starting point or final point is 1 in matrix, prints false and exits.
	if (matrix[0][0]==1) or (matrix[-1][-1]):
		print("false")
		exit()

	while True:
		'''
		active_matrix=matrix
		active_matrix[cursor.y][cursor.x]="*"
		for i in active_matrix:
			print(i)
		'''
		move_counter+=1
		print("#%i > X: %i Y: %i" % (move_counter, cursor.x, cursor.y))
		## If cursor is at the starting point, prints true and exits.
		if ((cursor.x==0) and (cursor.y==0)):
			print("true")
			exit()

		## If cursor is in deadlock, prints false and exits.
		if deadlock_counter>(row*line*10):
			print("false")
			exit()

		## Checks the nearest positions of cursor.
		if not(cursor.x==row):
			right = matrix[cursor.y][cursor.x+1]
		if cursor.x==row:
			right = None

		if not(cursor.x==0):
			left = matrix[cursor.y][cursor.x-1]
		if cursor.x==0:
			left = None

		if not(cursor.y==0):
			up = matrix[cursor.y-1][cursor.x]
		if cursor.y==0:
			up = None

		if not(cursor.y==line):
			down = matrix[cursor.y+1][cursor.x]
		if cursor.y==line:
			down = None

		## Movement in random order
		order = random.randint(1,24)

		if order==1:
			##1
			if left==0 and ((shadow.x!=(cursor.x-1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x-=1
				continue

			##2
			if up==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y-1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y-=1
				continue

			##3
			if right==0 and ((shadow.x!=(cursor.x+1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x+=1
				continue

			##4
			if down==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y+1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y+=1
				continue

			else:
				deadlock_counter+=1
				shadow2 = coord(cursor.x, cursor.y)
				cursor.x = shadow.x
				cursor.y = shadow.y
				shadow.x = shadow2.x
				shadow.y = shadow2.y
				continue

		if order==2:
			##1
			if left==0 and ((shadow.x!=(cursor.x-1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x-=1
				continue

			##2
			if up==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y-1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y-=1
				continue

			##4
			if down==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y+1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y+=1
				continue

			##3
			if right==0 and ((shadow.x!=(cursor.x+1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x+=1
				continue

			else:
				deadlock_counter+=1
				shadow2 = coord(cursor.x, cursor.y)
				cursor.x = shadow.x
				cursor.y = shadow.y
				shadow.x = shadow2.x
				shadow.y = shadow2.y
				continue

		if order==3:
			##1
			if left==0 and ((shadow.x!=(cursor.x-1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x-=1
				continue
			##4
			if down==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y+1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y+=1
				continue
			##2
			if up==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y-1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y-=1
				continue
			##3
			if right==0 and ((shadow.x!=(cursor.x+1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x+=1
				continue

			else:
				deadlock_counter+=1
				shadow2 = coord(cursor.x, cursor.y)
				cursor.x = shadow.x
				cursor.y = shadow.y
				shadow.x = shadow2.x
				shadow.y = shadow2.y
				continue

		if order==4:
			##4
			if down==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y+1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y+=1
				continue
			##1
			if left==0 and ((shadow.x!=(cursor.x-1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x-=1
				continue
			##2
			if up==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y-1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y-=1
				continue
			##3
			if right==0 and ((shadow.x!=(cursor.x+1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x+=1
				continue

			else:
				deadlock_counter+=1
				shadow2 = coord(cursor.x, cursor.y)
				cursor.x = shadow.x
				cursor.y = shadow.y
				shadow.x = shadow2.x
				shadow.y = shadow2.y
				continue

		if order==5:
			##1
			if left==0 and ((shadow.x!=(cursor.x-1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x-=1
				continue
			##3
			if right==0 and ((shadow.x!=(cursor.x+1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x+=1
				continue
			##2
			if up==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y-1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y-=1
				continue
			##4
			if down==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y+1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y+=1
				continue

			else:
				deadlock_counter+=1
				shadow2 = coord(cursor.x, cursor.y)
				cursor.x = shadow.x
				cursor.y = shadow.y
				shadow.x = shadow2.x
				shadow.y = shadow2.y
				continue

		if order==6:
			##1
			if left==0 and ((shadow.x!=(cursor.x-1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x-=1
				continue
			##3
			if right==0 and ((shadow.x!=(cursor.x+1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x+=1
				continue
			##4
			if down==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y+1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y+=1
				continue
			##2
			if up==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y-1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y-=1
				continue

			else:
				deadlock_counter+=1
				shadow2 = coord(cursor.x, cursor.y)
				cursor.x = shadow.x
				cursor.y = shadow.y
				shadow.x = shadow2.x
				shadow.y = shadow2.y
				continue

		if order==7:
			##1
			if left==0 and ((shadow.x!=(cursor.x-1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x-=1
				continue
			##4
			if down==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y+1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y+=1
				continue
			##3
			if right==0 and ((shadow.x!=(cursor.x+1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x+=1
				continue
			##2
			if up==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y-1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y-=1
				continue

			else:
				deadlock_counter+=1
				shadow2 = coord(cursor.x, cursor.y)
				cursor.x = shadow.x
				cursor.y = shadow.y
				shadow.x = shadow2.x
				shadow.y = shadow2.y
				continue

		if order==8:
			##4
			if down==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y+1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y+=1
				continue
			##1
			if left==0 and ((shadow.x!=(cursor.x-1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x-=1
				continue
			##3
			if right==0 and ((shadow.x!=(cursor.x+1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x+=1
				continue
			##2
			if up==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y-1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y-=1
				continue

			else:
				deadlock_counter+=1
				shadow2 = coord(cursor.x, cursor.y)
				cursor.x = shadow.x
				cursor.y = shadow.y
				shadow.x = shadow2.x
				shadow.y = shadow2.y
				continue

		if order==9:
			##3
			if right==0 and ((shadow.x!=(cursor.x+1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x+=1
				continue
			##1
			if left==0 and ((shadow.x!=(cursor.x-1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x-=1
				continue
			##2
			if up==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y-1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y-=1
				continue
			##4
			if down==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y+1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y+=1
				continue

			else:
				deadlock_counter+=1
				shadow2 = coord(cursor.x, cursor.y)
				cursor.x = shadow.x
				cursor.y = shadow.y
				shadow.x = shadow2.x
				shadow.y = shadow2.y
				continue

		if order==10:
			##3
			if right==0 and ((shadow.x!=(cursor.x+1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x+=1
				continue
			##1
			if left==0 and ((shadow.x!=(cursor.x-1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x-=1
				continue
			##4
			if down==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y+1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y+=1
				continue
			##2
			if up==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y-1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y-=1
				continue

			else:
				deadlock_counter+=1
				shadow2 = coord(cursor.x, cursor.y)
				cursor.x = shadow.x
				cursor.y = shadow.y
				shadow.x = shadow2.x
				shadow.y = shadow2.y
				continue

		if order==11:
			##3
			if right==0 and ((shadow.x!=(cursor.x+1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x+=1
				continue
			##4
			if down==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y+1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y+=1
				continue
			##1
			if left==0 and ((shadow.x!=(cursor.x-1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x-=1
				continue
			##2
			if up==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y-1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y-=1
				continue

			else:
				deadlock_counter+=1
				shadow2 = coord(cursor.x, cursor.y)
				cursor.x = shadow.x
				cursor.y = shadow.y
				shadow.x = shadow2.x
				shadow.y = shadow2.y
				continue

		if order==12:
			##4
			if down==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y+1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y+=1
				continue
			##3
			if right==0 and ((shadow.x!=(cursor.x+1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x+=1
				continue
			##1
			if left==0 and ((shadow.x!=(cursor.x-1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x-=1
				continue
			##2
			if up==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y-1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y-=1
				continue

			else:
				deadlock_counter+=1
				shadow2 = coord(cursor.x, cursor.y)
				cursor.x = shadow.x
				cursor.y = shadow.y
				shadow.x = shadow2.x
				shadow.y = shadow2.y
				continue

		if order==13:
			##2
			if up==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y-1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y-=1
				continue
			##1
			if left==0 and ((shadow.x!=(cursor.x-1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x-=1
				continue
			##3
			if right==0 and ((shadow.x!=(cursor.x+1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x+=1
				continue
			##4
			if down==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y+1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y+=1
				continue

			else:
				deadlock_counter+=1
				shadow2 = coord(cursor.x, cursor.y)
				cursor.x = shadow.x
				cursor.y = shadow.y
				shadow.x = shadow2.x
				shadow.y = shadow2.y
				continue

		if order==14:
			##2
			if up==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y-1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y-=1
				continue
			##1
			if left==0 and ((shadow.x!=(cursor.x-1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x-=1
				continue
			##4
			if down==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y+1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y+=1
				continue
			##3
			if right==0 and ((shadow.x!=(cursor.x+1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x+=1
				continue


			else:
				deadlock_counter+=1
				shadow2 = coord(cursor.x, cursor.y)
				cursor.x = shadow.x
				cursor.y = shadow.y
				shadow.x = shadow2.x
				shadow.y = shadow2.y
				continue

		if order==15:
			##2
			if up==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y-1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y-=1
				continue
			##4
			if down==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y+1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y+=1
				continue
			##1
			if left==0 and ((shadow.x!=(cursor.x-1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x-=1
				continue
			##3
			if right==0 and ((shadow.x!=(cursor.x+1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x+=1
				continue


			else:
				deadlock_counter+=1
				shadow2 = coord(cursor.x, cursor.y)
				cursor.x = shadow.x
				cursor.y = shadow.y
				shadow.x = shadow2.x
				shadow.y = shadow2.y
				continue

		if order==16:
			##4
			if down==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y+1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y+=1
				continue
			##2
			if up==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y-1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y-=1
				continue
			##1
			if left==0 and ((shadow.x!=(cursor.x-1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x-=1
				continue
			##3
			if right==0 and ((shadow.x!=(cursor.x+1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x+=1
				continue


			else:
				deadlock_counter+=1
				shadow2 = coord(cursor.x, cursor.y)
				cursor.x = shadow.x
				cursor.y = shadow.y
				shadow.x = shadow2.x
				shadow.y = shadow2.y
				continue

		if order==17:
			##2
			if up==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y-1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y-=1
				continue
			##3
			if right==0 and ((shadow.x!=(cursor.x+1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x+=1
				continue
			##1
			if left==0 and ((shadow.x!=(cursor.x-1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x-=1
				continue
			##4
			if down==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y+1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y+=1
				continue

			else:
				deadlock_counter+=1
				shadow2 = coord(cursor.x, cursor.y)
				cursor.x = shadow.x
				cursor.y = shadow.y
				shadow.x = shadow2.x
				shadow.y = shadow2.y
				continue

		if order==18:
			##2
			if up==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y-1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y-=1
				continue
			##3
			if right==0 and ((shadow.x!=(cursor.x+1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x+=1
				continue
			##4
			if down==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y+1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y+=1
				continue
			##1
			if left==0 and ((shadow.x!=(cursor.x-1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x-=1
				continue

			else:
				deadlock_counter+=1
				shadow2 = coord(cursor.x, cursor.y)
				cursor.x = shadow.x
				cursor.y = shadow.y
				shadow.x = shadow2.x
				shadow.y = shadow2.y
				continue

		if order==19:
			##2
			if up==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y-1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y-=1
				continue
			##4
			if down==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y+1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y+=1
				continue
			##3
			if right==0 and ((shadow.x!=(cursor.x+1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x+=1
				continue
			##1
			if left==0 and ((shadow.x!=(cursor.x-1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x-=1
				continue

			else:
				deadlock_counter+=1
				shadow2 = coord(cursor.x, cursor.y)
				cursor.x = shadow.x
				cursor.y = shadow.y
				shadow.x = shadow2.x
				shadow.y = shadow2.y
				continue

		if order==20:
			##4
			if down==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y+1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y+=1
				continue
			##2
			if up==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y-1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y-=1
				continue
			##3
			if right==0 and ((shadow.x!=(cursor.x+1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x+=1
				continue
			##1
			if left==0 and ((shadow.x!=(cursor.x-1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x-=1
				continue

			else:
				deadlock_counter+=1
				shadow2 = coord(cursor.x, cursor.y)
				cursor.x = shadow.x
				cursor.y = shadow.y
				shadow.x = shadow2.x
				shadow.y = shadow2.y
				continue

		if order==21:
			##3
			if right==0 and ((shadow.x!=(cursor.x+1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x+=1
				continue
			##2
			if up==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y-1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y-=1
				continue
			##1
			if left==0 and ((shadow.x!=(cursor.x-1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x-=1
				continue
			##4
			if down==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y+1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y+=1
				continue

			else:
				deadlock_counter+=1
				shadow2 = coord(cursor.x, cursor.y)
				cursor.x = shadow.x
				cursor.y = shadow.y
				shadow.x = shadow2.x
				shadow.y = shadow2.y
				continue

		if order==22:
			##3
			if right==0 and ((shadow.x!=(cursor.x+1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x+=1
				continue
			##2
			if up==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y-1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y-=1
				continue
			##4
			if down==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y+1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y+=1
				continue
			##1
			if left==0 and ((shadow.x!=(cursor.x-1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x-=1
				continue

			else:
				deadlock_counter+=1
				shadow2 = coord(cursor.x, cursor.y)
				cursor.x = shadow.x
				cursor.y = shadow.y
				shadow.x = shadow2.x
				shadow.y = shadow2.y
				continue

		if order==23:
			##3
			if right==0 and ((shadow.x!=(cursor.x+1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x+=1
				continue
			##4
			if down==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y+1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y+=1
				continue
			##2
			if up==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y-1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y-=1
				continue
			##1
			if left==0 and ((shadow.x!=(cursor.x-1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x-=1
				continue

			else:
				deadlock_counter+=1
				shadow2 = coord(cursor.x, cursor.y)
				cursor.x = shadow.x
				cursor.y = shadow.y
				shadow.x = shadow2.x
				shadow.y = shadow2.y
				continue

		if order==24:
			##4
			if down==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y+1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y+=1
				continue
			##3
			if right==0 and ((shadow.x!=(cursor.x+1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x+=1
				continue
			##2
			if up==0 and ((shadow.x!=(cursor.x)) or (shadow.y!=cursor.y-1)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.y-=1
				continue
			##1
			if left==0 and ((shadow.x!=(cursor.x-1)) or (shadow.y!=cursor.y)):
				## Keeps the earlier position of cursor.
				shadow.x = cursor.x
				shadow.y = cursor.y
				cursor.x-=1
				continue

			else:
				deadlock_counter+=1
				shadow2 = coord(cursor.x, cursor.y)
				cursor.x = shadow.x
				cursor.y = shadow.y
				shadow.x = shadow2.x
				shadow.y = shadow2.y
				continue


matrix = get_values()
is_exit(matrix)