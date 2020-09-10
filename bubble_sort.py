# Bubble Sort // compares the first two items in a list, if any item is larger they swap places


def bubbleSort(myList):
	for i in range (0, len(myList) -1):
		for j in range (0,len(myList) -1 -i):
			if myList[j] > myList[j+1]:
				myList[j], myList[j + 1] = myList[j + 1], myList[j]
	return myList			

theList = [23,54,67,8,7,6]

print(bubbleSort(theList))	
