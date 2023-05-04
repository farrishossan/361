def stack_code():
    return """Stack implementation using list
     
    stack = []
     
    # append() function to push
    # element in the stack
    stack.append('a')
    stack.append('b')
    stack.append('c')
     
    print('Initial stack')
    print(stack)
     
    # pop() function to pop
    # element from stack in
    # LIFO order
    print('\nElements popped from stack:')
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
     
    print('\nStack after elements are popped:')
    print(stack)
    
    source: https://www.geeksforgeeks.org/stack-in-python/"""


def queue_code():
    return """Queue implementation using a list
      
    # Initializing a queue
    queue = []
      
    # Adding elements to the queue
    queue.append('a')
    queue.append('b')
    queue.append('c')
      
    print("Initial queue")
    print(queue)
      
    # Removing elements from the queue
    print("\nElements dequeued from queue")
    print(queue.pop(0))
    print(queue.pop(0))
    print(queue.pop(0))
      
    print("\nQueue after removing elements")
    print(queue)
    
    source: https://www.geeksforgeeks.org/queue-in-python/"""


def deque_code():
    return """Deque implementation Python
    
    # insert(), index(), remove(), count()
    
    import collections
     
    # initializing deque
    de = collections.deque([1, 2, 3, 3, 4, 2, 4])
     
    # using index() to print the first occurrence of 4
    print ("The number 4 first occurs at a position : ")
    print (de.index(4,2,5))
     
    # using insert() to insert the value 3 at 5th position
    de.insert(4,3)
     
    # printing modified deque
    print ("The deque after inserting 3 at 5th position is : ")
    print (de)
     
    # using count() to count the occurrences of 3
    print ("The count of 3 in deque is : ")
    print (de.count(3))
     
    # using remove() to remove the first occurrence of 3
    de.remove(3)
     
    # printing modified deque
    print ("The deque after deleting first occurrence of 3 is : ")
    print (de)
    
    source: https://www.geeksforgeeks.org/deque-in-python/"""


def linked_list_code():
    return """
    class Node:
       def __init__(self, dataval=None):
          self.dataval = dataval
          self.nextval = None

    class SLinkedList:
       def __init__(self):
          self.headval = None
    
    list1 = SLinkedList()
    list1.headval = Node("Mon")
    e2 = Node("Tue")
    e3 = Node("Wed")
    # Link first Node to second node
    list1.headval.nextval = e2
    
    # Link second Node to third node
    e2.nextval = e3
    
    source: https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm"""


def hash_table_code():
    return """
    Simple Hash table using a Python dictionary
    
    # Declare a dictionary and update value
    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    
    # update existing entry
    dict['Age'] = 8;
    
     # Add new entry               
    dict['School'] = "DPS School"; 
    print ("dict['Age']: ", dict['Age'])
    print ("dict['School']: ", dict['School'])
    
    # Delete element 
    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    del dict['Name']; # remove entry with key 'Name'
    dict.clear();     # remove all entries in dict
    del dict ;        # delete entire dictionary
    
    print ("dict['Age']: ", dict['Age'])
    print ("dict['School']: ", dict['School'])
    
    source: https://www.tutorialspoint.com/python_data_structure/python_hash_table.htm"""


def kruskals_algorithm_code():
    return """
    # Class to represent a graph
    class Graph:
     
        def __init__(self, vertices):
            self.V = vertices
            self.graph = []
     
        # Function to add an edge to graph
        def addEdge(self, u, v, w):
            self.graph.append([u, v, w])
     
        # A utility function to find set of an element i
        # (truly uses path compression technique)
        def find(self, parent, i):
            if parent[i] != i:
     
                # Reassignment of node's parent
                # to root node as
                # path compression requires
                parent[i] = self.find(parent, parent[i])
            return parent[i]
     
        # A function that does union of two sets of x and y
        # (uses union by rank)
        def union(self, parent, rank, x, y):
     
            # Attach smaller rank tree under root of
            # high rank tree (Union by Rank)
            if rank[x] < rank[y]:
                parent[x] = y
            elif rank[x] > rank[y]:
                parent[y] = x
     
            # If ranks are same, then make one as root
            # and increment its rank by one
            else:
                parent[y] = x
                rank[x] += 1
     
        # The main function to construct MST Kruskal's algorithm
        def KruskalMST(self):
     
            # This will store the resultant MST
            result = []
     
            # An index variable, used for sorted edges
            i = 0
     
            # An index variable, used for result[]
            e = 0
     
            # Sort all the edges in
            # non-decreasing order of their
            # weight
            self.graph = sorted(self.graph,
                                key=lambda item: item[2])
     
            parent = []
            rank = []
     
            # Create V subsets with single elements
            for node in range(self.V):
                parent.append(node)
                rank.append(0)
     
            # Number of edges to be taken is less than to V-1
            while e < self.V - 1:
     
                # Pick the smallest edge and increment
                # the index for next iteration
                u, v, w = self.graph[i]
                i = i + 1
                x = self.find(parent, u)
                y = self.find(parent, v)
     
                # If including this edge doesn't
                # cause cycle, then include it in result
                # and increment the index of result
                # for next edge
                if x != y:
                    e = e + 1
                    result.append([u, v, w])
                    self.union(parent, rank, x, y)
                # Else discard the edge
     
            minimumCost = 0
            print("Edges in the constructed MST")
            for u, v, weight in result:
                minimumCost += weight
                print("%d -- %d == %d" % (u, v, weight))
            print("Minimum Spanning Tree", minimumCost)
     
     
        # Driver code
    if __name__ == '__main__':
        g = Graph(4)
        g.addEdge(0, 1, 10)
        g.addEdge(0, 2, 6)
        g.addEdge(0, 3, 5)
        g.addEdge(1, 3, 15)
        g.addEdge(2, 3, 4)
     
        # Function call
        g.KruskalMST()
         
        # This code is contributed by Neelam Yadav
        # Improved by James Graça-Jones
        
        source: https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/"""

def dijkstras_algorithm_code():
    return """
    # Python program for Dijkstra's single
    # source shortest path algorithm. The program is
    # for adjacency matrix representation of the graph
      
    # Library for INT_MAX
    import sys
      
      
    class Graph():
      
        def __init__(self, vertices):
            self.V = vertices
            self.graph = [[0 for column in range(vertices)]
                          for row in range(vertices)]
      
        def printSolution(self, dist):
            print("Vertex \tDistance from Source")
            for node in range(self.V):
                print(node, "\t", dist[node])
      
        # A utility function to find the vertex with
        # minimum distance value, from the set of vertices
        # not yet included in shortest path tree
        def minDistance(self, dist, sptSet):
      
            # Initialize minimum distance for next node
            min = sys.maxsize
      
            # Search not nearest vertex not in the
            # shortest path tree
            for u in range(self.V):
                if dist[u] < min and sptSet[u] == False:
                    min = dist[u]
                    min_index = u
      
            return min_index
      
        # Function that implements Dijkstra's single source
        # shortest path algorithm for a graph represented
        # using adjacency matrix representation
        def dijkstra(self, src):
      
            dist = [sys.maxsize] * self.V
            dist[src] = 0
            sptSet = [False] * self.V
      
            for cout in range(self.V):
      
                # Pick the minimum distance vertex from
                # the set of vertices not yet processed.
                # x is always equal to src in first iteration
                x = self.minDistance(dist, sptSet)
      
                # Put the minimum distance vertex in the
                # shortest path tree
                sptSet[x] = True
      
                # Update dist value of the adjacent vertices
                # of the picked vertex only if the current
                # distance is greater than new distance and
                # the vertex in not in the shortest path tree
                for y in range(self.V):
                    if self.graph[x][y] > 0 and sptSet[y] == False and \
                            dist[y] > dist[x] + self.graph[x][y]:
                        dist[y] = dist[x] + self.graph[x][y]
      
            self.printSolution(dist)
      
          
        # Driver's code
        if __name__ == "__main__":
            g = Graph(9)
            g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
                       [4, 0, 8, 0, 0, 0, 0, 11, 0],
                       [0, 8, 0, 7, 0, 4, 0, 0, 2],
                       [0, 0, 7, 0, 9, 14, 0, 0, 0],
                       [0, 0, 0, 9, 0, 10, 0, 0, 0],
                       [0, 0, 4, 14, 10, 0, 2, 0, 0],
                       [0, 0, 0, 0, 0, 2, 0, 1, 6],
                       [8, 11, 0, 0, 0, 0, 1, 0, 7],
                       [0, 0, 2, 0, 0, 0, 6, 7, 0]
                       ]
          
            g.dijkstra(0)
          
        # This code is contributed by Divyanshu Mehta and Updated by Pranav Singh Sambyal
        
        source: https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/"""


def binary_tree_code():
    return """ # Binary Tree with operations Python
    # Create Root
    class Node:
       def __init__(self, data):
          self.left = None
          self.right = None
          self.data = data
          
    # Insert
    def insert(self, data):
        # Compare the new value with the parent node
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         elif data > self.data:
               if self.right is None:
                  self.right = Node(data)
               else:
                  self.right.insert(data)
      else:
         self.data = data
         
    # Inorder traversal
    # Left -> Root -> Right
   def inorderTraversal(self, root):
      res = []
      if root:
         res = self.inorderTraversal(root.left)
         res.append(root.data)
         res = res + self.inorderTraversal(root.right)
      return res
      
    print(root.inorderTraversal(root)) 

    source: https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm
    """

def avl_tree_code():
    return """ # AVL Tree in Python
    class Node(object):
       def __init__(self, data):
          self.data = data
          self.left = None
          self.right = None
          self.height = 1
    class AVLTree(object):
       def insert(self, root, key):
          if not root:
             return Node(key)
          elif key < root.data:
             root.left = self.insert(root.left, key)
          else:
             root.right = self.insert(root.right, key)
          root.h = 1 + max(self.getHeight(root.left),
             self.getHeight(root.right))
          b = self.getBalance(root)
          if b > 1 and key < root.left.data:
             return self.rightRotate(root)
          if b < -1 and key > root.right.data:
             return self.leftRotate(root)
          if b > 1 and key > root.left.data:
             root.left = self.lefttRotate(root.left)
             return self.rightRotate(root)
          if b < -1 and key < root.right.data:
             root.right = self.rightRotate(root.right)
             return self.leftRotate(root)
          return root
       def leftRotate(self, z):
          y = z.right
          T2 = y.left
          
    source: https://www.tutorialspoint.com/data_structures_algorithms/avl_tree_algorithm.htm
    """