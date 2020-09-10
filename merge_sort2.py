# MergeSort // Recursive method, divide and conquer. Very efficient for large data sets. Fast.
#Splits a list in chunks of a single item, sorts them and merges them together in pairs, sorts them until a single 
#sorted list is reached



def merge_sort(A):
	merge_sort2(A, 0, len(A) -1)
	return A

def merge_sort2(A, first, last):
	if first < last:
		middle = (first + last) // 2
		merge_sort2(A, first,middle)
		merge_sort2(A, middle + 1, last)
		merge(A, first, middle, last)

def merge(A, first, middle , last):
	L = A[first:middle]
	R = A[middle: last + 1]
	L.append(999999999)
	R.append(999999999)
	i = j = 0
	for k in range (first, last +1):
		if L[i] <= R[j]:
			A[k] = L[i]
			i += 1
		else: 
			A[k] = R[j]	
			j += 1