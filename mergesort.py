

def mergeSort(list):
 # Determine whether the list is broken into
 # individual pieces.
 if len(list) < 2:
 	return list

 # Find the middle of the list.
 middle = len(list)//2
 # Break the list into two pieces.
 left = mergeSort(list[:middle])
 right = mergeSort(list[middle:])

 # Merge the two sorted pieces into a larger piece.
 print("Left side: ", left)
 print("Right side: ", right)
 merged = merge(left, right)
 print("Merged ", merged)
 return merged

def merge(left, right):
 # When the left side or the right side is empty,
 # it means that this is an individual item and is
 # already sorted.
 if not len(left):
 	return left
 if not len(right):
 	return right









# Option 2


def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              # The value from the left half has been used
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

	