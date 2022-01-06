# Heap-BST
This project aims to implement following HEAP and BINARY SEARCH TREE algorithms based on the lecture notes and measure their runtime in order to compare with theoretical results.

## HEAP

For HEAP implementations, results that are listed below is based on these input parameters.
A=[16,4,10,14,7,9,3,2,8,1]
B= [1,8,2,3,9,7,14,10,4,16]
C= [11,6,5,0,8,2,7]
n= len(A)

###### Max_Heapify(A,n,i) & Heapify(A,n,i)
Theoretical Time Complexity: O(lgn)
maxHeapify(A,n,i): 0.2328571
maxHeapify(B,n,i): 0.2848023
maxHeapify(C,n,i): 0.2637467

###### Build_Max_Heap(A)
Theoretical Time Complexity: O(nlgn)
buildMaxHeap(A): 0.2548983
buildMaxHeap(B): 0.2332933
buildMaxHeap(C): 0.2637744

###### Heapsort(A)
Theoretical Time Complexity: O(nlgn)
heapSort(A): 0.239019
heapSort(B): 0.2403869
heapSort(C): 0.229996

###### Max_Heap_Insert(A, key, n)
key=15
Theoretical Time Complexity: O(lgn)
heapSort(A,key,n): 0.2306594
heapSort(B,key,n): 0.2282456
heapSort(C,key,n): 0.2353671

###### Heap_Extract_Max(A,n)
Theoretical Time Complexity: O(lgn)
heapSort(A,n): 0.2313397
heapSort(B,n): 0.2235909
heapSort(C,n): 0.2267199

###### Heap_Increase_Key(A,i,key)
i=n
key=15
Theoretical Time Complexity: O(lgn)
heapIncreaseKey(A,n,15): 0.2265069
heapIncreaseKey(B,n,15): 0.2867596
heapIncreaseKey(C,n,15): 0.2335927

###### Heap_Maximum(A)
Theoretical Time Complexity: O(1)
heapIncreaseKey(A,n,15): 0.234868
heapIncreaseKey(B,n,15): 0.2342425
heapIncreaseKey(C,n,15): 0.2356012

## Binary Search Tree

For first try, I inserted array A with using treeInsert method in order to build binary search tree.
In second try, B array was inserted and for the third try C array was inserted. Here’s performance
measurements for these three tries. It mostly correlates with theoretical time complexities. Also, in
order to implement binary search tree structure in Python, I implemented some other methods such as
minHelper, pathHelper, minNodeVal.

A = [12,5,18,2,9,15,19,1,3,17]
B = [4,7,8,6,2,8,7,9,1,4]
C = [5,2,0,3,7,6,7,3,2,4]

###### inorderTreeWalk(root)
Theoretical Time Complexity: O(n)
Trial A: 0.2295073
Trial B: 0.229548
Trial C: 0.2295579

###### treeSearch(root,key)
key=2
Theoretical Time Complexity: O(h), h=height of the tree
Trial A: 0.2275759
Trial B: 0.2349378
Trial C: 0.2304113

###### treeInsert(node,key)
Theoretical Time Complexity: O(h), h=height of the tree
treeInsert(root, 12): 0.226674
treeInsert(root, 5): 0.2266829
treeInsert(root, 18): 0.2266876
We see it increases when tree’s height increase.

###### predSuc(root,key)
I implemented find predecessor and find successor methods together.
Theoretical Time Complexity: O(h), h=height of the tree
key=18
predSuc(root,18): 0.2373646
predSuc(root, 15): 0.2331298
predSuc(root,9): 0.2269939

###### treeMinimum(root)
Theoretical Time Complexity: O(h), h=height of the tree
treeMinimum(root) for A: 0.2270775
treeMinimum(root) for B: 0.2310865
treeMinimum(root) for C: 0.2343081

###### treeMaximum(root)
Theoretical Time Complexity: O(h), h=height of the tree
treeMaximum(root) for A: 0.2270747
treeMaximum(root) for B: 0.2310831
treeMaximum(root) for C: 0.2343052

###### treeDelete(root,key)
Theoretical Time Complexity: O(h), h=height of the tree
treeDelete(root,2) for A: 0.2344089
treeDelete(root,2) for B: 0.2344118
treeDelete(root,2) for C: 0.2344144

###### longestPath(root)
longestPath(root) for A: 0.2345645
longestPath(root) for B: 0.2345677
longestPath(root) for C: 0.2345705

###### shortestPath(root)
shortestPath(root) for A: 0.2345146
shortestPath(root) for B: 0.2345174
shortestPath(root) for C: 0.2345511

###### pathRatio()
pathRatio(root) for A: 0.2319122
pathRatio(root) for B: 0.229822
pathRatio(root) for C: 0.2346186




