## Insertion-Sort(A)

def insertion_sort(A):
	for j in range(len(A)):
		key = A[j]
		## Insert A[j] into the sorted sequence A[1...j-1].
		i = j - 1
		while i >= 0 and A[i] > key:
			A[i + 1] = A[i]
			i = i - 1
		A[i + 1] = key


str_A = input('Enter array: ').split(' ')
A = [int(num) for num in str_A]
	
print("unsorted(A): " + str(A))
insertion_sort(A)
print("sorted(A): " + str(A))
	
		