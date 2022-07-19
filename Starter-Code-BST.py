class BST:
    ###################
    # Start Problem 1 #
    ###################
    
    #Consider puting a member variable here. Remember, to access this variable later you
    #will refer to it in this format: BST.my_variable

    class Node:
        
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    # Problem 1 Continued #
    def get_size(self):
        #return your member variable
        pass

    def standardize_name(self, name):
        #This function formats names
        #to be Last, First
        
        #PLEASE DON'T CHANGE THIS FUNCTION
        
        name = name.lower()
        name = name.title()

        final_product = name

        coma_index = name.find(",")
        if coma_index == -1:
            split_name = name.split(" ")
            last_name = split_name.pop()
            final_product = last_name + ","
            for name in split_name:
                final_product = final_product + " " + name

        return final_product

    # Problem 1 Continued #
    def insert(self, data):
        #At some point in this function be sure to increment your member variable
        data = self.standardize_name(data)

        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    # Problem 1 Continued #
    def _insert(self, data, node):
        #At some point(s) in this function be sure to increment your member variable

        if data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert recursively on the left sub-tree.
                self._insert(data, node.left)
        elif data > node.data:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert recursively on the right sub-tree.
                self._insert(data, node.right)
    
    def __contains__(self, data):
        """ 
        Checks if data is in the BST.  This function
        supports the ability to use the 'in' keyword:

        if 5 in my_bst:
            ("5 is in the bst")

        """
        data = self.standardize_name(data)
        return self._contains(data, self.root)  # Start at the root

    ###################
    # Start Problem 2 #
    ###################
    def _contains(self, data, node):
        #Searches tree for given "data"  and is intended to be
        #called the first time by the __contains__ function.
        pass
    ###################
    #  End Problem 2  #
    ###################

    def __iter__(self):
        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)

    def delete(self, data):
        if self.root is not None:
            data = self.standardize_name(data)
            self._delete(data, self.root)

    # Problem 1 Continued #
    def _delete(self, data, node, parent = None):
        #At some point(s) in this function be sure to decrement your member variable

        #If name not found
        if node is None:
            return 
        #If we've found the name we're looking for
        elif node.data == data:
            #If the name we're looking for is a leaf node
            if node.left is None and node.right is None:
                if node == self.root:
                    self.root = None
                elif parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
            #If the name we're looking for only has a right child
            elif node.left is None:
                if node == self.root:
                    self.root = node.right
                elif parent.left == node:
                    parent.left = node.right
                else:
                    parent.right = node.right
            #If the name we're looking for only has a left child
            elif node.right is None:
                if node == self.root:
                    self.root = node.left
                elif parent.left == node:
                    parent.left = node.left
                else:
                    parent.right = node.left
            #If the name we're looking for has both left and right children
            else:
                #We need to find the next in line to take the place of the current node
                #The next in line is the name in the roster directly after the current node
                #in alphabetic order
                replacement_node = node.right       #Start with subtree to the right of current node
                replacement_data = node.right.data  #Save the data of the right child
                while replacement_node.left:
                    replacement_node = replacement_node.left   #keep moving left till you reach the leaf
                    replacement_data = replacement_node.data   #Eventually updates "replacement_data" to be the data of the leaf
                node.data = replacement_data                   #Current node's data is now replaced with the leaf's data
                #This results in deleting the leaf node:
                self._delete(replacement_data, node.right, node)
        #If haven't found the name we're looking for and it comes before the current node
        elif node.data > data:
            #We keep looking to the left
            self._delete(data, node.left, node)
        #If haven't found the name we're looking for and it comes after the current node
        else:
            #We keep looking to the right
            self._delete(data, node.right, node)

###################
# Problem 1 Tests #
###################
print("\n=========== PROBLEM 1 TESTS ===========")
roster = BST()
print(f"Size: {roster.get_size()}") #Should be 0
roster.insert("Rebecca Jones")
roster.insert("Brad Smith")
roster.insert("Jessica Gardner")
roster.insert("Owen Kennedy")
roster.insert("John Doe")
roster.insert("Dan Zimmer")
roster.insert("Steve Harley")
roster.insert("Caleb Levitt")
roster.insert("Eli Anderson")
print(f"Size: {roster.get_size()}") #Should be 9

#The current tree:                              _________Jones, Rebecca_________
#                                              /                                \
#                              Gardner, Jessica                                  Smith, Brad
#                             /                \                                /           \
#                    Doe, John                  Harley, Steve      Kennedy, Owen             Zimmer, Dan
#                   /                                                           \
#       Eli Anderson                                                             Levitt, Caleb

#Test if size adjusts correctly when deleting a leaf
roster.delete("Dan Zimmer")
print(f"Size: {roster.get_size()}") #Should be 8

#Test if size adjusts correctly when deleting a node that only has left child
roster.delete("John Doe")
print(f"Size: {roster.get_size()}") #Should be 7

#Test if size adjusts correctly when deleting a node that only has right child
roster.delete("Owen Kennedy")
print(f"Size: {roster.get_size()}") #Should be 6

#Test if size adjusts correctly when deleting a node that has two children
roster.delete("Jessica Gardner")
print(f"Size: {roster.get_size()}") #Should be 5

#Test if size adjusts correctly when deleting the root
roster.delete("Rebecca Jones")
print(f"Size: {roster.get_size()}") #Should be 4

#Test if size is unchanged when trying to delete a name that's not in the roster
roster.delete("John Wayne")
print(f"Size: {roster.get_size()}") #Should still be 4



###################
# Problem 2 Tests #
###################

print("\n=========== PROBLEM 2 TESTS ===========")

#The current tree:                              __________Levitt, Caleb________
#                                              /                                \
#                                 Harley, Steve                                  Smith, Brad
#                               /
#                   Eli Anderson

is_found = "Brad Smith" in roster
print(f"Found Name: {is_found}") #Should be True

is_found = "John Wayne" in roster
print(f"Found Name: {is_found}") #Should be False
