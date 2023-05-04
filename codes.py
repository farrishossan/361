def binary_search_code():
    return """def binarySearch(arr, l, r, x):
    while l <= r:

        mid = l + (r - l) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element
    # was not present
    return -1
    
    source: https://www.geeksforgeeks.org/binary-search/#"""


def linear_search_code():
    return """def search(arr, N, x):
 
    for i in range(0, N):
        if (arr[i] == x):
            return i
    return -1
    source: https://www.geeksforgeeks.org/linear-search/
    """

def depth_first_search_code():
    return """from collections import defaultdict
 
    # This class represents a directed graph using
    # adjacency list representation
     
     
    class Graph:
     
        # Constructor
        def __init__(self):
     
            # default dictionary to store graph
            self.graph = defaultdict(list)
     
        # function to add an edge to graph
        def addEdge(self, u, v):
            self.graph[u].append(v)
     
        # A function used by DFS
        def DFSUtil(self, v, visited):
     
            visited.add(v)
            print(v, end=' ')
    
            for neighbour in self.graph[v]:
                if neighbour not in visited:
                    self.DFSUtil(neighbour, visited)
     
        # The function to do DFS traversal. It uses
        # recursive DFSUtil()
        def DFS(self, v):
     
            # Create a set to store visited vertices
            visited = set()
     
            # Call the recursive helper function
            # to print DFS traversal
            self.DFSUtil(v, visited)
        
    source:https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/?ref=gcse"""


def breadth_first_search_code():
    return """from collections import defaultdict
 
 
    # This class represents a directed graph
    # using adjacency list representation
    class Graph:
     
        # Constructor
        def __init__(self):
     
            # Default dictionary to store graph
            self.graph = defaultdict(list)
     
        def addEdge(self, u, v):
            self.graph[u].append(v)
     
        # Function to print a BFS of graph
        def BFS(self, s):
     
            # Mark all the vertices as not visited
            visited = [False] * (max(self.graph) + 1)
     
            # Create a queue for BFS
            queue = []
     
            # Mark the source node as
            # visited and enqueue it
            queue.append(s)
            visited[s] = True
     
            while queue:
     
                # Dequeue a vertex from
                # queue and print it
                s = queue.pop(0)
                print(s, end=" ")
     
                # Get all adjacent vertices of the
                # dequeued vertex s. If a adjacent
                # has not been visited, then mark it
                # visited and enqueue it
                for i in self.graph[s]:
                    if visited[i] == False:
                        queue.append(i)
                        visited[i] = True
                    
    source: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/"""


def insertion_sort_code():
    return """def insertionSortRecursive(arr,n):
    # base case
    if n<=1:
        return
      
    # Sort first n-1 elements
    insertionSortRecursive(arr,n-1)
    '''Insert last element at its correct position
        in sorted array.'''
    last = arr[n-1]
    j = n-2
      
      # Move elements of arr[0..i-1], that are
      # greater than key, to one position ahead
      # of their current position 
    while (j>=0 and arr[j]>last):
        arr[j+1] = arr[j]
        j = j-1
  
    arr[j+1]=last
    
    source: https://www.geeksforgeeks.org/recursive-insertion-sort """


def heap_sort_code():
    return """def heapify(arr, N, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < N and arr[largest] < arr[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < N and arr[largest] < arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
 
        # Heapify the root.
        heapify(arr, N, largest)
 
    # The main function to sort an array of given size
    def heapSort(arr):
        N = len(arr)
     
        # Build a maxheap.
        for i in range(N//2 - 1, -1, -1):
            heapify(arr, N, i)
     
        for i in range(N-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # swap
            heapify(arr, i, 0)
            
    source:https://www.geeksforgeeks.org/heap-sort"""

def selection_sort_code():
    return """# Return minimum index
    def minIndex( a , i , j ):
        if i == j:
            return i
             
        # Find minimum of remaining elements
        k = minIndex(a, i + 1, j)
         
        # Return minimum of current
        # and remaining.
        return (i if a[i] < a[k] else k)
         
    # Recursive selection sort. n is
    # size of a[] and index is index of
    # starting element.
    def recurSelectionSort(a, n, index = 0):
     
        # Return when starting and
        # size are same
        if index == n:
            return -1
             
        # calling minimum index function
        # for minimum index
        k = minIndex(a, index, n-1)
         
        # Swapping when index and minimum
        # index are not same
        if k != index:
            a[k], a[index] = a[index], a[k]
             
        # Recursively calling selection
        # sort function
        recurSelectionSort(a, n, index + 1)
        
    source: https://www.geeksforgeeks.org/recursive-selection-sort"""


def merge_sort_code():
    return """def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            
    source: https://www.geeksforgeeks.org/merge-sort/"""


def quick_sort_code():
    return """def partition(arr, low, high):
    i = (low - 1)         # index of smaller element
    pivot = arr[high]     # pivot
  
    for j in range(low, high):
  
        # If current element is smaller 
        # than or equal to pivot
        if arr[j] <= pivot:
          
            # increment index of
            # smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)
  
    # The main function that implements QuickSort
    # arr[] --> Array to be sorted,
    # low --> Starting index,
    # high --> Ending index
      
    # Function to do Quick sort
    def quickSort(arr, low, high):
        if low < high:
      
            # pi is partitioning index, arr[p] is now
            # at right place
            pi = partition(arr, low, high)
      
            # Separately sort elements before
            # partition and after partition
            quickSort(arr, low, pi-1)
            quickSort(arr, pi + 1, high)
            
    source:https://www.geeksforgeeks.org/iterative-quick-sort/"""


def huffman_code():
    return """# A Huffman Tree Node
import heapq
 
 
class node:
    def __init__(self, freq, symbol, left=None, right=None):
        # frequency of symbol
        self.freq = freq
 
        # symbol name (character)
        self.symbol = symbol
 
        # node left of current node
        self.left = left
 
        # node right of current node
        self.right = right
 
        # tree direction (0/1)
        self.huff = ''
 
    def __lt__(self, nxt):
        return self.freq < nxt.freq
 
 
    # utility function to print huffman
    # codes for all symbols in the newly
    # created Huffman tree
    def printNodes(node, val=''):
     
        # huffman code for current node
        newVal = val + str(node.huff)
     
        # if node is not an edge node
        # then traverse inside it
        if(node.left):
            printNodes(node.left, newVal)
        if(node.right):
            printNodes(node.right, newVal)
     
            # if node is edge node then
            # display its huffman code
        if(not node.left and not node.right):
            print(f"{node.symbol} -> {newVal}")
     
     
    # characters for huffman tree
    chars = ['a', 'b', 'c', 'd', 'e', 'f']
     
    # frequency of characters
    freq = [5, 9, 12, 13, 16, 45]
     
    # list containing unused nodes
    nodes = []
     
    # converting characters and frequencies
    # into huffman tree nodes
    for x in range(len(chars)):
        heapq.heappush(nodes, node(freq[x], chars[x]))
     
    while len(nodes) > 1:
     
        # sort all the nodes in ascending order
        # based on their frequency
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
     
        # assign directional value to these nodes
        left.huff = 0
        right.huff = 1
     
        # combine the 2 smallest nodes to create
        # new node as their parent
        newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)
     
        heapq.heappush(nodes, newNode)
     
    # Huffman Tree is ready!
    printNodes(nodes[0])

    source: https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3"""