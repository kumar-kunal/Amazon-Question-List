'''
Given a read only array of n + 1 integers between 1 and n, find one number that repeats in linear time using less than O(n) space and traversing the stream sequentially O(1) times.

Sample Input:

[3 4 1 4 1]
Sample Output:

1
If there are multiple possible answers ( like in the sample case above ), output any one.

If there is no duplicate, output -1

'''

'''

Divide the whole array in sub-array of size sqrt(N).

If count of element present in any sub-array will be greater than sqrt(n),
We wll use hashing in that.

'''

A=[3,4,1,4,1]

def find_duplicate_in_array(A):
	size = len(A)
	sub_array_size = sqrt(size)

	count_element = [0 for _ in range(sub_array_size+1)]

	for i in range(size):
		count_element[int(A[i]/sub_array_size)] += 1
	print(count_element)

find_duplicate_in_array(A)

