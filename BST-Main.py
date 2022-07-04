#Sean Macmillan 10542221 | Keiren Moores 10537063
"""code from Pearson Education, Inc p104 """


def printTree(root, element="element", left="left", right="right"):                                 ##  https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
    def display(root, element=element, left=left, right=right):                                     ##  AUTHOR: Original: J.V.     Edit: BcK
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if getattr(root, right) is None and getattr(root, left) is None:
            line = '%s' % getattr(root, element)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if getattr(root, right) is None:
            lines, n, p, x = display(getattr(root, left))
            s = '%s' % getattr(root, element)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if getattr(root, left) is None:
            lines, n, p, x = display(getattr(root, right))
            s = '%s' % getattr(root, element)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display(getattr(root, left))
        right, m, q, y = display(getattr(root, right))
        s = '%s' % getattr(root, element)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
    
    lines = []
    if root != None:
        lines, *_ = display(root, element, left, right)
    print("\t== Binary Tree shape ==")
    print()
    if lines == []:
        print("\t  No tree found")
    for line in lines:
        print("\t", line)
    print()

class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __repr__(self):
      printTree(self.getRoot())
      return ""

    # Return True if the element is in the tree
    def search(self, e):
        current = self.root # Start from the root

        while current != None:
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else: # element matches current.element
                return current # Element is found

        return None

    # Insert element e into the binary search tree
    # Return True if the element is inserted successfully
    def insert(self, e):
        if self.root == None:
          self.root = self.createNewNode(e) # Create a new root
        else:
          # Locate the parent node
          parent = None
          current = self.root
          while current != None:
            if e < current.element:
              parent = current
              current = current.left
            elif e > current.element:
              parent = current
              current = current.right
            else:
              return False # Duplicate node? not inserted

          # Create the new node and attach it to the parent node
          if e < parent.element:
            parent.left = self.createNewNode(e)
            parent.left.parent = parent
          else:
            parent.right = self.createNewNode(e)
            parent.right.parent = parent

        self.size += 1 # Increase tree size
        return True # Element inserted

    #delete a specified node for the tree
    def deleteNode(self, e):
        n = self.search(e)
        self.deleteNodeHelper(n)

    #returns False if node is not in the tree
    def deleteNodeHelper(self, n):
        if n != None:
            parent = n.parent
            if n.left == None and n.right == None: #n is a leaf node
                if parent.left == n:
                    parent.left = None
                if parent.right == n:
                    parent.right = None
                return True
            elif n.left != None and n.right == None: #n has a left child
                nxt = n.left
                while nxt.right != None:
                    nxt = nxt.right
                n.element, nxt.element = nxt.element, n.element
                self.deleteNodeHelper(nxt)
            else: #n has a right child or two children
                nxt = n.left
                while nxt.right != None:
                    nxt = nxt.right
                n.element, nxt.element = nxt.element, n.element
                self.deleteNodeHelper(nxt)
            
        else:
            return False #deletion unsuccesful


    # Create a new TreeNode for element e
    def createNewNode(self, e):
      return TreeNode(e)
    
    # Return the size of the tree
    def getSize(self):
      return self.size

#pre post and in order functions

    # Inorder traversal from the root
    def inorder(self):
      self.inorderHelper(self.root)

    # Inorder traversal from a subtree
    def inorderHelper(self, r):
      if r != None:
        self.inorderHelper(r.left)
        print(r.element, end = " ")
        self.inorderHelper(r.right)

    # Postorder traversal from the root
    def postorder(self):
      self.postorderHelper(self.root)

    # Postorder traversal from a subtree
    def postorderHelper(self, root):
      if root != None:
        self.postorderHelper(root.left)
        self.postorderHelper(root.right)
        print(root.element, end = " ")

    # Preorder traversal from the root
    def preorder(self):
      self.preorderHelper(self.root)

    # Preorder traversal from a subtree
    def preorderHelper(self, root):
      if root != None:
        print(root.element, end = " ")
        self.preorderHelper(root.left)
        self.preorderHelper(root.right)



# modified for counting leaf nodes
    # Inorder traversal from the root - All leaf nodes
    def leafNodes(self):
      self.leafHelper(self.root)

    # Inorder traversal from a subtree - All leaf nodes
    def leafHelper(self, r):
        if r != None:
            self.leafHelper(r.left)
            if r.left == None and r.right == None:
                print(r.element, end = " ")
            self.leafHelper(r.right)

# modified for counting non-leaf nodes
    # Inorder traversal from the root - All non-leaf nodes
    def nonLeafNodes(self):
        self.nonLeafHelper(self.root)

    # Inorder traversal from a subtree - All non-leaf nodes
    def nonLeafHelper(self, r):
        if r != None:
            self.nonLeafHelper(r.left)
            if r.left != None or r.right != None:
                print(r.element, end = " ")
            self.nonLeafHelper(r.right)

# modified to calculate the depth of the tree
    def depthCacl(self):
      self.depthCaclHelper(self.root, 0, [])

    # calculate the depth from a given subtree
    def depthCaclHelper(self, root, count, depthArray):
        count += 1
        if root != None:
            self.depthCaclHelper(root.left, count, depthArray)
            self.depthCaclHelper(root.right, count, depthArray)
            if root.left == None and root.right == None:
                depthArray.append(count)
            return selectionSort(depthArray)[len(depthArray)-1] -1

    def depthFinderHelper(self, e):
        return self.depthFinder(e, self.root, 0, [])[0]

#find the depth of a specified node. I tried many ways to do this beter. Trust me when I say i spent almost 2 hours on this. I have no idea why it took so long
    def depthFinder(self, e, root, count, depths):
        count += 1
        if root != None:
            self.depthFinder(e, root.left, count, depths)
            self.depthFinder(e, root.right, count, depths)
            if root == e:
                depths += [count - 1]
        return depths
      

#modified to output an array : subTree
    def findSubTree(self, root, subTree):
        if root != None:
            #print(root.element, end = " ")
            subTree.append(root.element)
            self.findSubTree(root.left, subTree)
            self.findSubTree(root.right, subTree)
        return subTree
    
    # Return true if the tree is empty
    def isEmpty(self):
      return self.size == 0

    # Remove all elements from the tree
    def clear(self):
      self.root = None
      self.size = 0

    # Return the root of the tree
    def getRoot(self):
      return self.root

class TreeNode:
    def __init__(self, e):
      self.element = e
      self.left = None # Point to the left node, default None
      self.right = None # Point to the right node, default None
      self.parent = None # pointer to this node's parent

    ####################### Main test binary tree


#sorting ------------------
sortedA = []
def balanceSort(A):
    if len(A) > 1:
        leftA = A[:len(A)//2]
        rightA = A[len(A)//2:]
        middle = A[len(A)//2]

        sortedA.append(middle)    

        balanceSort(leftA)
        balanceSort(rightA)
    elif len(A) == 1:
        sortedA.append(A[0])
        

def selectionSort(a):

    for x in range(len(a)):
        minN = x
        for i in range(x + 1, len(a)):

            if a[minN] > a[i]: # find the minimum element
                minN = i

        a[x], a[minN] = a[minN], a[x] # swap current element with minimum element
        
    return a

''' removed
def randomA():
    a = []
    for i in range(0, 10):
        n = random.randint(0,100)
        a.append(n)
    return a        
'''

#main========================================================================================================**

intTree = BinaryTree()

def manualEntry():
    values = []
    print("Manual entry of values. \n type a value and press enter. Press enter again to Exit")
    while True:
        inp = input("enter a value: ")
        if inp == "":
            break
        else:
            try: values.append(int(inp))
            except: print("please enter integer values")
    print("Values are: ", values)
    return values
        

def Start(a = [54, 80, 64, 19, 34, 78, 22, 13, 20, 102, 91, 44, 84, 50, 46, 47, 49, 45 ]):

    global intTree
    global sortedA
    intTree.clear()
    a = list(dict.fromkeys(a)) # quickly convert a from list to dictionary to list, this will remove all duplicates before sorting
    balanceSort(selectionSort(a))
    numbers = sortedA
    print ("\n\nCreating BST:")
    for e in numbers:
      intTree.insert(e)

    print(intTree)

    sortedA = []

def subMenu():
    print('Sub-menu')
    while True:
        print('\n[1] Print the pre-order, in-order, and post-order of the BST, in sequence.')
        print('[2] Print all leaf nodes of the BST, and all non-leaf nodes (separately).')
        print('[3] Print the total number of nodes of a sub-tree.')
        print('[4] Print the depth of a node in the BST.')
        print('[5] Print the depth of a subtree rooted at a particular node.')
        print('[6] Insert a new integer key into the BST.')
        print('[7] Delete an integer key from the BST.')
        print('[8] Exit.')
        choice = input('> ').lower()

        if choice == '1':
            print("Preorder traversal:")
            intTree.preorder()
            print("\n\nPostorder traversal:")
            intTree.postorder()
            print("\n\nInorder traversal:")
            intTree.inorder()
            print()

        elif choice == '2':
            print("Leaf Nodes: ")
            intTree.leafNodes()
            print("\nNon-Leaf Nodes: ")
            intTree.nonLeafNodes()

        elif choice == '3':
            inp = input("\n\nEnter a subtree to display: ")
            print("Subtree: ", end = " ")
            try: searchElm = intTree.search(int(inp))
            except: #error catch
                searchElm = None
                print("Wrong input entered")
            if searchElm != None:
                subTree = intTree.findSubTree(searchElm,[])
                print(subTree)
                print("\nSubtree root: ", subTree[0], "\nSubtree size: ", len(subTree))

                newTree = BinaryTree()
                for x in subTree:
                    newTree.insert(x)
                printTree(newTree.getRoot())  
                

        elif choice == '4':
            inp = input("\n\nEnter a value find depth of: ")
            try: searchElm = intTree.search(int(inp))
            except: searchElm = None #error catch
            if searchElm != None:
                depth = intTree.depthFinderHelper(searchElm)
                print("Node: ", inp, " has depth: ", depth)

        elif choice == '5':
            while True:
                inp = input("\n\nCalculate the depth from a given root: ")
                try: depth = intTree.depthCaclHelper(intTree.search(int(inp)), 0, [])
                except: print("error: please enter an integer value") #error catch
                else: break
                finally: print()
            print("\nSubtree root: ", inp, "\nSubtree depth: ", depth)

        elif choice == '6':
            errorFlag = False
            inp = input("\n\nEnter an integer element to add: ")
            try: int(inp)
            except: errorFlag = True #error catch
            if errorFlag == False:
                if intTree.insert(int(inp)): print("Insertion succesful")
                else: print("Insertion unsuccesful")
            else: print("Value was not a valid key")

        elif choice == '7':
            errorFlag = False
            inp = input("\n\nEnter an integer element to delete: ")
            try: searchElm = intTree.search(int(inp))
            except: searchElm = None #error catch
            if searchElm != None:
                try:    
                    intTree.deleteNode(int(inp))
                    print("Deletion successful")
                except:
                    print("Deletion unsuccessful")
                    print("Value was not a valid key")
            else:
                print("Deletion unsuccessful")
                print("Please enter key in BST")

        elif choice == '8':
            print("Returning...")
            break

print('BST Manipulation')
while True:
    print('\n[1] Pre-load a sequence of integers to build a BST.')
    print('[2] Manually enter integer values/keys, one by one, to build a BST.')
    print('[3] Exit.')
    choice = input('> ').lower()
      
    if choice == "1":
        Start()
        subMenu()

    elif choice == '2':
        v = manualEntry()
        Start(v)
        subMenu()

    elif choice == '3':
        break
    
print("Exiting program...")
