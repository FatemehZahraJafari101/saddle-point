#If we have a point in a two-dimensional array (matrix)
#that has the lowest value in its own row and the highest
#value in its own column, it is called the saddle point.
import sys

def saddle_point(matrix):
	lst = list()
	for i in range(0, len(matrix), 1):
		mr = sys.maxsize
		for j in range(0, len(matrix[i]), 1):
			mr = min(mr, matrix[i][j])
		lst.append(mr)

	for j in range(0, len(matrix[0]), 1):
		mc = -sys.maxsize - 1
		for i in range(0, len(matrix), 1):
			mc = max(mc, matrix[i][j])

		if (mc in lst):
			p = mc	
		
	return p

print(saddle_point([[ 2, 10, 4 ],
            [ 9, 13, 8 ],
            [ 15, 6, 5 ]]))

