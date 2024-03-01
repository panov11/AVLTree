# username - matanamit, jonathanp1
# id1      - 206866980
# name1    - Matan Amit
# id2      - 206580102
# name2    - jonathan panov

"""A class represnting a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type key: int or None
    @type value: any
    @param value: data of your node
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1

    """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child (if self is virtual)
    """

    def get_left(self):
        if self.key is None:
            return None
        if self.left is None:
            virtual = AVLNode(None, None)
            self.left = virtual
            virtual.parent = self
            return virtual
        return self.left

    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child (if self is virtual)
    """

    def get_right(self):
        if self.key is None:
            return None
        if self.right is None:
            virtual = AVLNode(None, None)
            self.right = virtual
            virtual.parent = self
            return virtual
        return self.right

    """returns the parent 

    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """

    def get_parent(self):
        if self.parent == None:
            return None
        return self.parent

    """returns the key

    @rtype: int or None
    @returns: the key of self, None if the node is virtual
    """

    def get_key(self):
        if self.is_real_node():
            return self.key
        else:
            return None

    """returns the value

    @rtype: any
    @returns: the value of self, None if the node is virtual
    """

    def get_value(self):
        if self.key == None:
            return None
        return self.value

    """returns the height

    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """

    def get_height(self):
        if not self.is_real_node():
            return -1
        return self.height

    """sets left child

    @type node: AVLNode
    @param node: a node
    """

    def set_left(self, node):
        self.left = node
        return None

    """sets right child

    @type node: AVLNode
    @param node: a node
    """

    def set_right(self, node):
        self.right = node
        return None

    """sets parent

    @type node: AVLNode
    @param node: a node
    """

    def set_parent(self, node):
        self.parent = node
        return None

    """sets key

    @type key: int or None
    @param key: key
    """

    def set_key(self, key):
        self.key = key
        return None

    """sets value

    @type value: any
    @param value: data
    """

    def set_value(self, value):
        self.value = value
        return None

    """sets the height of the node

    @type h: int
    @param h: the height
    """

    def set_height(self, h):
        self.height = h
        return None

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """
    def is_real_node(self):
        return self.key is not None

    #return the parent of the deleted node O(logn)
    def Delete_Node_Only(self,tree):
        #in case deleting the root
        if self.key == tree.root.key:
            #childless root
            if self.left is None and self.right is None:
                tree.root=None
                return AVLNode(None,None)
            #root with right child
            if self.left is None and self.right is not None:
                tree.root=self.right
                self.right.parent=None
                self.right=None
                return tree.root
            #root with left child
            if self.right is None and self.left is not None:
                tree.root=self.left
                self.left.parent=None
                self.left=None
                return tree.root


        parent = self.parent
        """case node is leaf"""
        if self.left == None and self.right == None:
            if parent.right == self:
                parent.right = None
            else:
                parent.left = None
        """case node has only one child, the right one"""
        if self.left == None and self.right != None:
            if parent.right == self:
                parent.right = self.right
                self.right.parent = parent
            else:
                parent.left = self.right
                self.right.parent = parent
        """case node has only one child, the left one"""
        if self.right == None and self.left != None:
            if parent.left == self:
                parent.left = self.left
                self.left.parent = parent
            else:
                parent.right = self.left
                self.left.parent = parent
        """case node has two children"""
        if self.right != None and self.left != None:
            node_successor = tree.Successor(self)

            if node_successor is self.right:

                if node_successor.right is None and node_successor.left is None:

                    node_successor.parent=self.parent
                    node_successor.left=self.left
                    if self.parent is not None :
                        if self.parent.left is self:
                            self.parent.left=node_successor
                        else:
                            self.parent.right=node_successor
                    else:

                        tree.root=node_successor
                elif node_successor.left is None:
                    node_successor.left=tree.root.left
                    tree.root.left.parent=node_successor
                    node_successor.parent=None
                    tree.root=node_successor
            else:

                parent_succ = node_successor.parent

                parent_succ.left = node_successor.right
                if parent_succ.left != None:
                    parent_succ.left.parent = parent_succ

                node_successor.left = self.left
                self.left.parent = node_successor
                node_successor.right = self.right
                self.right.parent = node_successor



                if parent is not None:
                    if parent.left == self:
                        parent.left = node_successor
                    else:
                        parent.right = node_successor
                        node_successor.parent = parent
                    node_successor.parent.set_height(node_successor.parent.get_height() - 1)
                    return parent_succ
                else:
                    node_successor.parent=parent
                    tree.root=node_successor
                    parent=node_successor



        if parent is not None:
            parent.set_height(parent.get_height() - 1)

        return parent

    #calculate balnce factor of node O(1)
    def Balance_Factor(self):
        if self is None or not self.is_real_node():
            return 0
        left_height = self.left.get_height() if self.left is not None else -1
        right_height = self.right.get_height() if self.right is not None else -1
        return left_height - right_height

    #update the height of node O(1)
    def update_height(self):
        work=False
        if self is not None and self.key is not None:
            left_height = self.left.get_height() if self.left else -1
            right_height = self.right.get_height() if self.right else -1
            check=self.height
            self.set_height(1 + max(left_height, right_height))
            if check!=self.height:
                work=True
        return work



"""
A class implementing the ADT Dictionary, using an AVL tree.
"""


class AVLTree(object):
    """
    Constructor, you are allowed to add more fields.

    """

    def __init__(self):
        self.root = None
        self.tree_size = 0
        # add your fields here

    """searches for a AVLNode in the dictionary corresponding to the key

    @type key: int
    @param key: a key to be searched
    @rtype: AVLNode
    @returns: the AVLNode corresponding to key or None if key is not found.
    """
    #O(logn)
    def search(self, key):
        node = self.root


        while node != None:
            if node.get_key() == key:
                return node
            elif node.get_key() > key:
                node = node.get_left()
            else:
                node = node.get_right()

        return None

    """inserts val at position i in the dictionary

    @type key: int
    @pre: key currently does not appear in the dictionary
    @param key: key of item that is to be inserted to self
    @type val: any
    @param val: the value of the item
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """
    #O(logn)
    def insert(self, key, val):
        check=False
        if key is None:
            return None
        #in case of inserting to a tree with root only
        if self.root is not None and self.root.left is None and self.root.right is None:
            if self.root.key is not None:
                if key<self.root.key:
                    a=AVLNode(key,val)
                    a.set_height(0)
                    self.root.set_left(a)
                    a.set_parent(self.root)
                    self.root.set_height(1)
                    return 1
                else:
                    a = AVLNode(key, val)
                    a.set_height(0)
                    self.root.set_right(a)
                    a.set_parent(self.root)
                    self.root.set_height(1)
                    return 1



        self.tree_size+=1
        parent = None
        node = self.root
        counter=0
        #going to the right place to insert
        while node is not None and node.is_real_node():
            parent = node
            if key < node.get_key():
                node = node.get_left()
            else:
                node = node.get_right()



        new_node = AVLNode(key, val)
        new_node.set_height(0)
        new_node.set_parent(parent)

        if parent is None:
            self.root = new_node
            return 0

        height1 = parent.get_height()  # height of parent befor insert
        #inserting
        if key < parent.get_key():
            parent.set_left(new_node)
            if not parent.is_real_node():
                parent.set_left(None)  # remove the virtual node
                new_node.set_parent(parent.get_parent())  # set the correct parent
                parent = parent.get_parent()  # update parent reference
        else:
            parent.set_right(new_node)
            if not parent.is_real_node():
                parent.set_right(None)
                new_node.set_parent(parent.get_parent())
                parent = parent.get_parent()

        node = parent

        """go up to the root until rotate"""
        while node is not None:
            BF = node.Balance_Factor()
            worked=node.update_height()
            if worked==True:
                counter+=1
            height2=node.get_height()
            #balancing the tree
            if abs(BF) < 2 and height1 == height2:
                return 0+counter

            elif abs(BF) < 2 and height1 != height2:

                height1 = height2
                node = node.get_parent()
                if node is not None:
                    node.set_height(node.get_height() + 1)
                    counter+=1
            else:
                if BF == -2 and node.get_right().Balance_Factor() == -1:

                    self.LeftRotation(node)
                    if worked is True:
                        return counter-1
                    return counter

                elif BF == -2 and node.get_right().Balance_Factor() == 1:

                    self.RightRotation(node.get_right())
                    self.LeftRotation(node)
                    if worked is True:
                        return counter-2
                    return counter

                if BF == 2 and node.get_left().Balance_Factor() == 1:


                    self.RightRotation(node)
                    if worked is True:
                        return counter-1
                    return counter

                elif BF == 2 and node.get_left().Balance_Factor() == -1:

                    self.LeftRotation(node.get_left())
                    self.RightRotation(node)
                    if worked is True:
                        return counter-2
                    return counter

        return 0+counter

    """deletes node from the dictionary

    @type node: AVLNode
    @pre: node is a real pointer to a node in self
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """
    #O(logn)
    def delete(self, node):
        counter = 0
        suc=self.Successor(node)
        if node.get_parent() is None:
            height1=node.get_height()
        else:
            height1 = node.get_parent().get_height()

        parent = node.Delete_Node_Only(self)
        if parent is self.root:
            if parent.update_height():
                counter+=1
        if parent is None:
            parent=suc

        node1 = parent
        """go up to the root and rotate if need"""
        while node1 != None:
            BF = node1.Balance_Factor()
            node1.update_height()
            height2 = node1.get_height()
            if abs(BF) < 2 and height1 == height2:
                if self.root.get_key() == node.get_key():
                    self.root=node1
                return counter
            elif abs(BF) < 2 and height1 != height2:
                height1 = height2
                node1 = node1.get_parent()
            else:
                if BF == -2 and ((node1.get_right().Balance_Factor() == -1) or node1.get_right().Balance_Factor() == 0):
                    self.LeftRotation(node1)
                    counter += 1
                    node1 = node1.get_parent()
                elif BF == -2 and node1.get_right().Balance_Factor() == 1:
                    self.RightRotation(node1.get_right())
                    self.LeftRotation(node1)
                    counter += 2
                    node1 = node1.get_parent()
                if BF == 2 and ((node1.get_left().Balance_Factor() == 1) or node1.get_left().Balance_Factor() == 0):
                    self.RightRotation(node1)
                    counter += 1
                    node1 = node1.get_parent()
                elif BF == 2 and node1.get_left().Balance_Factor() == -1:
                    self.LeftRotation(node1.get_left())
                    self.RightRotation(node1)
                    counter += 2
                    node1 = node1.get_parent()

        self.tree_size = self.tree_size - 1
        return counter

    """returns an array representing dictionary 

    @rtype: list
    @returns: a sorted list according to key of touples (key, value) representing the data structure
    """
    #O(n)
    def avl_to_array(self):
        arr = []

        def rec_val_arrey(node, array):
            if node is None:
                return
            rec_val_arrey(node.left, array)
            array.append((node.key, node.value))
            rec_val_arrey(node.right, array)

        rec_val_arrey(self.root, arr)
        return arr

    """returns the number of items in dictionary 

    @rtype: int
    @returns: the number of items in dictionary 
    """
    #O(n)
    def size(self):
        arr=self.avl_to_array()
        if len(arr)==1:
            if arr[0][0] is None:
                return 0
        return len(arr)
    #O(1)
    def set_size(self, size):
        self.tree_size=size

    """splits the dictionary at the i'th index

    @type node: AVLNode
    @pre: node is in self
    @param node: The intended node in the dictionary according to whom we split
    @rtype: list
    @returns: a list [left, right], where left is an AVLTree representing the keys in the 
    dictionary smaller than node.key, right is an AVLTree representing the keys in the 
    dictionary larger than node.key.
    """
    #O(logn)
    def split(self,node):
        check=node.get_key()
        x=self.search(node.get_key())
        # creating new sub left tree T1 (T1<x)
        T1 = AVLTree()
        T1.root = x.get_left()
        T1.set_size(T1.size())
        T1.root.set_parent(AVLNode(None,None))
        # creating new sub right tree T2 (T2>x)
        T2 = AVLTree()
        T2.root = x.get_right()
        T2.set_size(T2.size())
        T2.root.set_parent(AVLNode(None,None))
        x.set_left(AVLNode(None,None))
        x.set_right(AVLNode(None,None))
        node1 = x
        parent = x.parent
        grand = x.parent
        if grand is None:
            grand=x
            parent=x
        while grand.is_real_node:
            grand = parent.parent
            if parent.left == node1:
                parent.set_left(AVLNode(None,None))
                T3 = AVLTree()
                T3.root = parent.right
                T3.root.set_parent(AVLNode(None, None))

                if parent.right is None:
                    T3.root=AVLNode(None,None)
                T3.set_size(T3.size())
                parent.set_right(AVLNode(None,None))
                b1=parent.get_key()
                c=parent.get_value()
                a= T2.join(T3,b1,c)

            else:
                parent.set_right(AVLNode(None,None))
                T4 = AVLTree()
                T4.root = parent.get_left()
                T4.set_size(T4.size())
                T4.root.set_parent(AVLNode(None,None))
                parent.set_left(AVLNode(None,None))
                if parent.key==node.key:
                    b=T4.join(T1,None,None)
                else:
                    b=T4.join(T1,parent.get_key(),parent.get_value())
                T1.root = T4.root

            node1 = node1.parent
            parent = parent.parent
            if grand is None:
                break
        return [T1, T2]


    """joins self with key and another AVLTree

    @type tree2: AVLTree 
    @param tree2: a dictionary to be joined with self
    @type key: int 
    @param key: The key separting self with tree2
    @type val: any 
    @param val: The value attached to key
    @pre: all keys in self are smaller than key and all keys in tree2 are larger than key
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """
    #O(logn)
    def join(self, tree2, key, val):
        t2=tree2
        x=AVLNode(key,val)
        tree1 = self
        t1node = tree1.root
        t2node = t2.root
        t1size = tree1.size()
        t2size = t2.size()

        if t2size == 0:
            if key is not None and val is not None:
                tree1.insert(key, val)
                self.set_size(t1size + t2size + 1)
                return tree1.root.get_height() +1
            return tree1.root.get_height()

        if t1size == 0:
            self.root=t2.root
            self.insert(key, val)
            self.set_size(t1size + t2size + 1)
            return tree2.root.get_height() +1

        if t2size == 1 and t1size==1:
            t2.insert(key, val)
            t2.insert(t1node.get_key(), t1node.get_value())
            tree1.root = tree2.root
            self.set_size(t1size + t2size + 1)
            return 1

        if t2size == 1:
            tree1.insert(key, val)

            tree1.insert(t2node.key, t2node.value)

            tree1.set_size(t1size + t2size + 1)
            return tree1.root.get_height() +1

        if t1size == 1:
            t2.insert(key, val)
            t2.insert(t1node.get_key(), t1node.get_value())
            tree1.root = tree2.root
            self.set_size(t1size + t2size + 1)
            return tree2.root.get_height() +1

        t1height = t1node.get_height()
        t2height = t2node.get_height()


        if t1height < t2height:
            while (t2node.is_real_node() and t2node.get_height() > t1height):
                t2node = t2node.left
            bigger = t2
            parent = t2node.parent
            x.set_parent(parent)
            parent.set_left(x)

        if t1height > t2height:
            while (t1node.is_real_node() and t1node.get_height() > t2height):
                t1node = t1node.right
            bigger = tree1
            parent = t1node.parent
            x.set_parent(parent)
            parent.set_right(x)


        if t1height == t2height:
            bigger = tree1
            x.set_parent(AVLNode(None,None))
            tree1.root = x

        x.set_left(t1node)
        x.set_right(t2node)
        t1node.set_parent(x)
        t2node.set_parent(x)
        x.update_height()
        node = x
        height1=node.get_height()
        """go up to the root until roatrate"""
        while node is not None:
            BF = node.Balance_Factor()
            worked = node.update_height()
            height2 = node.get_height()
            if abs(BF) < 2 and height1 == height2:
                break
            elif abs(BF) < 2 and height1 != height2:
                height1 = height2
                node = node.get_parent()
            else:
                if BF == -2 and node.get_right().Balance_Factor() == -1:
                    self.LeftRotation(node)

                elif BF == -2 and node.get_right().Balance_Factor() == 1:
                    self.RightRotation(node.get_right())
                    self.LeftRotation(node)

                if BF == 2 and node.get_left().Balance_Factor() == 1:
                    self.RightRotation(node)

                elif BF == 2 and node.get_left().Balance_Factor() == -1:
                    self.LeftRotation(node.get_left())
                    self.RightRotation(node)

        if bigger is tree2:
            saveT1Root = self.root
            self.root = t2.root
            if saveT1Root.get_key() > self.root.key:
                self.root = saveT1Root

        self.set_size(t1size + t2size + 1)
        return abs(t2height - t1height) +1


    """returns the root of the tree representing the dictionary

    @rtype: AVLNode
    @returns: the root, None if the dictionary is empty
    """
    #O(1)
    def get_root(self):
        if self.size() == 0:
            return None
        return self.root
    #do right rotation with a given tree and node
    #O(1)
    def RightRotation(self, node):

        P = node.parent
        B = node.left
        node.left = B.right
        if B.right is not None:
            B.right.parent = node
        B.right = node
        node.parent = B
        B.parent = P
        """update pointer of parent"""
        if P.key is not None:

            if P.left == node:
                P.left = B
            else:
                P.right = B
        else:
            self.root = B

        node.update_height()
        B.update_height()
    #do left rotation with given tree and node
    #O(1)
    def LeftRotation(self, node):
        P = node.parent
        B = node.right
        node.right = B.left
        if B.left is not None:
            B.left.parent = node
        B.left = node
        node.parent = B
        B.parent = P
        """update pointer of parent"""
        if P is not None:
            if P.left == node:
                P.left = B
            else:
                P.right = B
        else:
            self.root = B

        node.update_height()
        B.update_height()
    #find the smallest key of sub tree of node in the tree self
    #O(logn)
    def Min(self, node):
        while node.left != None:
            node = node.left
        return node

    #find the successor of given node
    #O(logn)
    def Successor(self, node):
        if node.right != None:
            return self.Min(node.right)
        parent = node.parent
        while parent != None and node == parent.right:
            node = parent
            parent = node.parent
        return parent



