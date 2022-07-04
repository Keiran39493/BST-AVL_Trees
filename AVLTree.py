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
        print("inserting ", e)
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
              print("node duplicate\n--------------------")
              return False # Duplicate node? not inserted
              

          # Create the new node and attach it to the parent node
          if e < parent.element:
            parent.left = self.createNewNode(e)
            parent.left.parent = parent
            self.inspectInsertion(parent.left)
          else:
            parent.right = self.createNewNode(e)
            parent.right.parent = parent
            self.inspectInsertion(parent.right)

        self.size += 1 # Increase tree size
        print("success\n--------------------")
        return True # Element inserted
        

#delete a specified node for the tree
    def deleteNode(self, e):
        n = self.search(e)
        self.deleteNodeHelper(n)
    
    #returns None if node is not in the tree
    def deleteNodeHelper(self, n):
        if n != None:
            parent = n.parent
            if n.left == None and n.right == None: #n is a leaf node
                if parent.left == n:
                    parent.left = None
                if parent.right == n:
                    parent.right = None
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

        
        #set heights
        if n.parent != None:
            n.parent.height = max(self.getHeight(n.parent.left), self.getHeight(n.parent.right)) + 1
            self.inspectDeletion(n)    

        

    ''' removed
#set heights of all nodes in the tree
    def calcNodeHeights(self):
      self.calcNodeHeightsHelper(self.root)

    def calcNodeHeightsHelper(self, r):
      if r != None:
        L = 0
        R = 0
        self.calcNodeHeightsHelper(r.left)
        self.calcNodeHeightsHelper(r.right)
        if r.left != None:
          L = r.left.height
        if r.right != None:
          R = r.right.height
        r.height = max(L,R) + 1
        print(".", end = '')
      else:
        print("|", end = "")
    '''

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



    #inspect insertion
    def inspectInsertion(self, node, path = []):
        if node.parent == None:
            return
        path = [node] + path

        lHeight = self.getHeight(node.parent.left)
        rHeight = self.getHeight(node.parent.right)

        if abs(lHeight - rHeight) > 1:
            path = [node.parent] + path
            self.balance(path[0], path[1], path[2])
            return
        
        newHeight = node.height + 1
        if newHeight > node.parent.height:
            node.parent.height = newHeight

        self.inspectInsertion(node.parent, path)

    #inspect deletion
    def inspectDeletion(self, node):
        if node != None:

            lHeight = self.getHeight(node.left)
            rHeight = self.getHeight(node.right)
            
            if abs(lHeight - rHeight) > 1:
                z = node
                y = self.taller(z)
                x = self.taller(y)

                self.balance(z, y, x)
            self.inspectDeletion(node.parent)
            

    #determines how to balance a subtree. z is the imbalanced node, x & y are the nodes required to get to z
    def balance(self, z, y, x):
        if y == z.left and x == y.left:
            self.rightRotation(z)
        elif y == z.left and x == y.right:
            self.leftRotation(y)
            self.rightRotation(z)
        elif y == z.right and x == y.right:
            self.leftRotation(z)
        elif y == z.right and x == y.left:
            self.rightRotation(y)
            self.leftRotation(z)
        else:
            print("An error has occured in rebalancing!\nplease confirm tree structure")
    
    #left Rotation
    def leftRotation(self, root):
        print("rotating left")
        #initialising left stucture
        anchor = root.parent
        y = root.right
        t2 = y.left
        #rotating tree
        y.left = root
        root.parent = y
        root.right = t2
        if t2 != None:
            t2.parent = root
        y.parent = anchor
        if y.parent != None:
            if y.parent.left == root:
                y.parent.left = y
            else:
                y.parent.right = y
        elif y.parent == None:
            self.root = y

        #updating heights
        root.height = max(self.getHeight(root.left),self.getHeight(root.right)) + 1
        y.height = max(self.getHeight(y.left),self.getHeight(y.right)) + 1

    #right Rotation
    def rightRotation(self, root):
        
        print("rotating right")
        #initialising left stucture
        anchor = root.parent
        y = root.left
        t3 = y.right
        #rotating tree
        y.right = root
        root.parent = y
        root.left = t3
        if t3 != None:
            t3.parent = root
        y.parent = anchor
        if y.parent != None:
            if y.parent.right == root:
                y.parent.right = y
            else:
                y.parent.left = y
        elif y.parent == None:
            self.root = y

        #updating heights
        root.height = max(self.getHeight(root.left),self.getHeight(root.right)) + 1
        y.height = max(self.getHeight(y.left),self.getHeight(y.right)) + 1

    def taller(self, root):
        l = self.getHeight(root.left)
        r = self.getHeight(root.right)
        if l >= r:
            return root.left
        else:
            return root.right

    def getHeight(self, node):
        if node != None:
            return node.height
        else:
            return 0
    
    # Create a new TreeNode for element e
    def createNewNode(self, e):
      return TreeNode(e)
    
    # Return the size of the tree
    def getSize(self):
      return self.size
    
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

    #modified to output an array : subTree
    def findSubTree(self, root, subTree):
        if root != None:
            self.findSubTree(root.left, subTree)
            subTree.append(root)
            self.findSubTree(root.right, subTree)
        return subTree

class TreeNode:
    def __init__(self, e):
      self.element = e
      self.left = None # Point to the left node, default None
      self.right = None # Point to the right node, default None
      self.parent = None # pointer to this node's parent, default None
      self.height = 1
      

#sorting========================================================================================================**
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


def Start(a = [55, 81, 65, 20, 35, 79, 23, 14, 21, 103, 92, 45, 85, 51, 47, 48, 50, 46]):

    global intTree
    intTree.clear() #this seems to not work? havent touched the original functions at all. Same with BST program...
    numbers = a
    print('\nCreating AVL: ')
    for e in numbers:
        intTree.insert(e)
    print(intTree)



def subMenu():
    print('\nSub-menu')
    while True:
        print('[1] Display the AVL tree, showing the height and balance factor for each node. ')
        print('[2] Print the pre-order, in-order, and post-order traversal sequences of the AVL tree. ')
        print('[3] Print all leaf nodes of the AVL tree, and all non-leaf nodes (separately). ')
        print('[4] Insert a new integer key into the AVL tree. ')
        print('[5] Delete an integer key from the AVL tree. ')
        print('[6] Exit. ')
        choice = input('> ').lower()

        if choice == '1': #print the tree
            print('Printing AVL Tree: ')
            print(intTree)
            #print the nodes, in order, with their height and balance factor
            subTree = intTree.findSubTree(intTree.getRoot(), [])
            for x in subTree:
                print("Tree node: ", x.element, "\n    -Height: ", x.height, "\n    -Balance Factor: ", (intTree.getHeight(x.left) - intTree.getHeight(x.right)))
            
        elif choice == '2':
            print("Preorder traversal:")
            intTree.preorder()
            print("\n\nPostorder traversal:")
            intTree.postorder()
            print("\n\nInorder traversal:")
            intTree.inorder()
            print("\n")
            
        elif choice == '3':
            print("Leaf Nodes: ")
            intTree.leafNodes()
            print("\nNon-Leaf Nodes: ")
            intTree.nonLeafNodes()
            print("\n")
            
        elif choice == '4':
            errorFlag = False
            inp = input("\n\nEnter an integer element to add: ")
            try: int(inp)
            except: errorFlag = True
            if errorFlag == False:
                if intTree.insert(int(inp)): print("Insertion succesful")
                else: print("Insertion unsuccesful")
            else: print("Value was not a valid key")
            
        elif choice == '5':
            errorFlag = False
            inp = input("\n\nEnter an integer element to delete: ")
            searchElm = None
            try: searchElm = intTree.search(int(inp))
            except: errorFlag = True 
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
                
        elif choice == '6':
            print("Returning...")
            break

print('AVL Tree')
while True:
    print('\n[1] Pre-load a sequence of integers to build an AVL tree. ')
    print('[2] Manually enter integer values/keys, one by one, to build an AVL tree.')
    print('[3] Exit.')
    choice = input('> ').lower()

    if choice == '1':
        Start()
        subMenu()
        
    if choice == '2':
        v = manualEntry()
        Start(v)
        subMenu()
        
    if choice == '3':
        break
    
print("Exiting program...")





