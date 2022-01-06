import sys
from time import process_time, perf_counter, sleep


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def inorderTreeWalk(root):
    if root is not None:
        inorderTreeWalk(root.left)
        print(str(root.key) + "->", end=' ')
        inorderTreeWalk(root.right)
        for i in range(0,len(A)):
            traversalArr.append(root.key)
    print(f"Runtime of inorderTreeWalk: {perf_counter()}")


def treeSearch(root, key):
    if root is None or key == root.key:
        print(f"Runtime of treeSearch: {perf_counter()}")
        return root
    if key < root.key:
        print(f"Runtime of treeSearch: {perf_counter()}")
        return treeSearch(root.left, key)
    else:
        print(f"Runtime of treeSearch: {perf_counter()}")
        return treeSearch(root.right, key)



def treeInsert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = treeInsert(node.left, key)
    else:
        node.right = treeInsert(node.right, key)
    print(f"Runtime of treeInsert: {perf_counter()}")
    return node

def nodeMinVal(node):
    current = node
    while(current.left is not None):
        current = current.left
    print(f"Runtime of nodeMinVal: {perf_counter()}")
    return current

def predSuc(root, key):
    if root is None:
        return
    if root.key == key:
        if root.left is not None:
            swp = root.left
            while(swp.right):
                swp = swp.right
            predSuc.pre = swp

        if root.right is not None:
            swp = root.right
            while(swp.left):
                swp = swp.left
            predSuc.suc = swp
        return

    if root.key > key:
        predSuc.suc=root
        predSuc(root.left, key)
    else:
        predSuc.pre = root
        predSuc(root.right, key)
    print(f"Runtime of predSuc: {perf_counter()}")

def treeMinimum(root):
    while root.left is not None:
        root = root.left
    print(f"Runtime of treeMinimum: {perf_counter()}")
    return root

def treeMaximum(root):
    while root.right is not None:
        root = root.right
    print(f"Runtime of treeMaximum: {perf_counter()}")
    return root

def treeDelete(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = treeDelete(root.left, key)
    elif(key > root.key):
        root.right = treeDelete(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root == None
            return temp

        elif root.right is None:
            temp = root.left
            root == None
            return temp
        temp = nodeMinVal(root.right)
        root.key = temp.key
        root.right = treeDelete(root.right, temp.key)
    print(f"Runtime of treeDelete: {perf_counter()}")
    return root

def argmax(rightLine , leftLine):
    if rightLine > leftLine:
        return rightLine
    else :
        return leftLine

def longestPath(root):
  if root is None:
    return []
  rightLine = [root.key] + longestPath(root.right)
  leftLine = [root.key] + longestPath(root.left)
  print(f"Runtime of longestPath: {perf_counter()}")
  return pathHelper(rightLine, leftLine)

def pathHelper(rightLine, leftLine):
  return rightLine if len(rightLine) > len(leftLine) else leftLine


def minHelper(rightLine, leftLine):
  return rightLine if len(rightLine) <= len(leftLine) else leftLine

def shortestPath(root):
    if root is None:
        return
    if root.right is None:
        return []
    if root.left is None:
        return []
    rightLine = [root.key] + shortestPath(root.right)
    leftLine = [root.key] + shortestPath(root.left)
    print(f"Runtime of shortestPath: {perf_counter()}")
    return minHelper(rightLine, leftLine)

def pathRatio():
    ratio = (len(shortestPath(root))+1) / len(longestPath(root))
    print(f"Runtime of pathRatio: {perf_counter()}")
    return ratio

rightLine = []
leftLine = []
ret=0
root = None
node = None
traversalArr = []
step = sys.maxsize*2+1
A = [12,5,18,2,9,15,19,1,3,17]
# A= [4,7,8,6,2,8,7,9,1,4]
# A= [5,2,0,3,7,6,7,3,2,4]
for i in range(0, len(A)):
    root = treeInsert(root, A[i])


key=15
predSuc.pre = None
predSuc.suc = None
predSuc(root, key)

if predSuc.pre is not None:
    print(predSuc.pre.key)
else:
    print("")

if predSuc.suc is not None:
    print(predSuc.suc.key)
else:
    print("")

print(len(longestPath(root)))
#treeSearch(root, 2)
treeMaximum(root)
treeMinimum(root)
print("Inorder traversal: ", end=' ')
inorderTreeWalk(root)
print("\nDelete 10")
root = treeDelete(root, 10)
print("Inorder traversal: ", end=' ')
inorderTreeWalk(root)
print(len(shortestPath(root))+1)
print(pathRatio())
