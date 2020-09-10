# QuickSort Algorithm

#Pivot : Items all items in the list are compared to. Often first item is selected as pivot, but it's a good idea
#to split the list in half 
# Recursive method thac calls itself on smaller and smaller sets of data
# Performance depends on piot selection

def quick_sort(A):
	quick_sort2(A, 0, len(A) - 1)
	return A 

def quick_sort2(A, low, hi):
	if low < hi:
	   p = partition(A, low, hi)   # returns the pivot
	   quick_sort2(A, low, p - 1)  #items left
	   quick_sort2(A, p + 1, hi)   # items right

def get_pivot(A, low, hi):
	mid = (hi + low) // 2
	pivot = hi
	if A[low] < A[mid]:
		if A[mid] < A[hi]:
			pivot = mid
	elif A[low]	< A[hi]:
		pivot = low
	return pivot

def partition(A, low, hi):
	pivotIndex = get_pivot(A, low, hi)
	pivotValue = A[pivotIndex]
	A[pivotIndex], A[low] = A[low], A[pivotIndex]
	border = low

	for i in range(low, hi + 1):
		if A[i] < pivotValue:
			border += 1
			A[i], A[border] = A[border], A[i]
	A[low], A[border] = A[border], A[low]
	return (border)