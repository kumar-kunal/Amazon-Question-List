'''
Rotate Matrix 
link:: https://www.interviewbit.com/problems/rotate-matrix/

Description::
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

You need to do this in place.

Note that if you end up using an additional array, you will only receive partial score.

Example:

If the array is

[
    [1, 2],
    [3, 4]
]
Then the rotated array becomes:

[
    [2, 4],
    [1, 3]
]
'''


'''

Rotate element ring-wise.

'''
matrix = [ [1,2], [3,4]]

def rotate_matrix(matrix):
	N=len(matrix)
	for row in range(N//2):
		for col in range(row, N-row-1):
			temp = matrix[row][col]
			matrix[row][col] = matrix[col][N-1-row]
			matrix[col][N-1-row] =  matrix[N-1-row][N-1-col]
			matrix[N-1-row][N-1-col] = matrix[N-1-col][row]
			matrix[N-1-col][row] = temp
	print(matrix)


rotate_matrix(matrix)
