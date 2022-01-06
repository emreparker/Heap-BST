import math
from time import process_time, perf_counter, sleep

def heapify(A, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and A[largest] < A[l]:
        largest = l
    if r < n and A[largest] < A[r]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i] # swap

        heapify(A, n, largest)
    print(f"Runtime of heapify: {perf_counter()}")


def maxHeapify(A, n, i):
    l= (2*i)
    r= (2*i)+1
    if(l<= n and A[l]>A[i]):
        largest = l
    else:
        largest=i
    if(r<= n and A[r]>A[largest]):
        largest=r
    if(largest != i):
        A[i], A[largest] = A[largest], A[i]
        maxHeapify(A,n,largest)
    print(f"Runtime of maxHeapify: {perf_counter()}")

def buildMaxHeap(A):
    n=len(A)
    for i in range (int(n/2)-1, -1, -1):
        heapify(A,n,i)
    print(f"Runtime of buildMaxHeap: {perf_counter()}")

def heapSort(A):
    n = len(A)

    for i in range(n//2 - 1, -1, -1):
        heapify(A, n, i)

    for i in range(n-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, i, 0)
    print(f"Runtime of heapSort: {perf_counter()}")


def maxParentNode(i):
    buildMaxHeap(A)
    index = int((i-1)/2)
    return A[index], index
    print(f"Runtime of maxParentNode: {perf_counter()}")

def heapIncreaseKey(A, i, key):
    if key < A[i]:
        return print("Error: New key is smaller than current key")
    A[i] = key
    if i>1 & int(maxParentNode(i)[0])<A[i]:
        A[i], A[maxParentNode(i)[1]] = A[maxParentNode(i)[1]], A[i]
        i = maxParentNode(i)
    print(f"Runtime of heapIncreaseKey: {perf_counter()}")

def heapExtractMax(A, n):
    if n < 1:
        return print("heap underflow")
    max = A[0]
    A[0] = A[n-1]
    n-=1
    heapify(A, n-1, 1)
    # max = A[1]
    # A[1] = A[n-1]
    # A[n-1] = 0
    # maxHeapify(A, n, 1)
    # n-=1
    return max
    print(f"Runtime of heapExtractMax: {perf_counter()}")

def maxHeapInsert(A, n, key):

    b = [0]
    A.extend(b)
    print(A)
    A[n] = key
    heapIncreaseKey(A, n, key)
    n += 1
    print(f"Runtime of maxHeapInsert: {perf_counter()}")

def heapMaximum(A):
    print(f"Runtime of heapMaximum: {perf_counter()}")
    return A[0]


A= [1,8,2,3,9,7,14,10,4,16]
#A= [11,6,5,0,8,2,7]
#A=[16,4,10,14,7,9,3,2,8,1]
n = len(A)
#maxHeapify(A,10,2)
#buildMaxHeap(A)
#heapSort(A)
#heapIncreaseKey(A, 8, 15)
#heapExtractMax(A, n)
# heapExtractMax(A,n)
#maxHeapInsert(A, n, 15)
#buildMaxHeap(A)
heapMaximum(A)
for i in range(n):
    print(A[i])


