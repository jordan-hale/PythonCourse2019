#Homework 5

#You should use the following as the starter definition for a Node class
class Node:
    def __init__(self, _value=None, _next=None):
#warns user of a bad input
        if type(_value) != int:
            print("Must input an integer")
        else:
            self.value = _value
            self.next = _next
    def __str__(self):
        return str(self.value)
#gives the node the self value
    def nodevalue(self):
        return self.value
#resets the node's value
    def newnodevalue(self, _value):
        self.value = _value
#signifies the next node
    def nextnode(self):
        return self.next
#sets a new next node
    def newnextnode(self, _next):
        self.next = _next

class LinkedList:
#Takes a number and sets it as the value at the head of the List
    def __init__(self, value):
#warns user of a bad input
        if type(value) != int:
            print("Must input an integer")
        else:
#sets the value applied using the Node class as the head of self
            self.head = Node(value)
        #Computation complexity and judgment: O(1) since executes in constant time...good
#Returns the length of the list
    def length(self):
#creates a headnode variable as the head
        headnode = self.head
#sets the length to zero initially
        n = 0
        while headnode != None:
#adds 1 to the list's length and sets headnode equal to the nextnode (to move along the list) each time loop is executed
            n = n + 1
            headnode = headnode.nextnode()
#returns the final n
        return n
        #Computation complexity and judgment: O(n) since operations grow linearly...good enough
#Takes a number and adds it to the end of the list
    def addNode(self, new_value):
#warns user of a bad input
        if type(new_value) != int:
            print("Must input an integer")
        else:
#sets the new value applied using the Node class as the newnode
            newnode = Node(new_value)
#creates a headnode variable as the head
            headnode = self.head
            while headnode != None:
#creates a new nextnode using the value of newnode if there is no nextnode (the added value)
                if headnode.nextnode() is None:
                    headnode.newnextnode(newnode)
                    return
#sets headnode equal to the nextnode if there is a nextnode (in order to get to the end of the list, since value is added to the end)
                else:
                    headnode = headnode.nextnode()
        #Computation complexity and judgment: O(n) since operations grow linearily...as good as possible
#Takes a number and adds it after the after_node
    def addNodeAfter(self, new_value, after_node):
#warns user of a bad input
        if type(new_value) != int:
            print("Must input an integer")
        else:
#creates a headnode variable as the head
            headnode = self.head
#sets the new value applied using the Node class as the newnode
            newnode = Node(new_value)
            while headnode != None:
#creates a new nextnode using the value of newnode if headnode's value equals after_node and if there is no nextnode (with headnode being the relevant node)
                if headnode.nodevalue() == after_node:
                    if headnode.nextnode() is None:
                        headnode.newnextnode(newnode)
#creates a new nextnode for the newnode using the value of headnode's nextnode and creates a new nextnode for headnode using the value of newnode if there is a nextnode
#(sets new value between headnode and nextnode)
                    else:
                        newnode.newnextnode(headnode.nextnode())
                        headnode.newnextnode(newnode)
                    return
#sets headnode equal to the nextnode if headnode's value does not equal after_node (to move down the list)
                else:
                    headnode = headnode.nextnode()
        #Computation complexity and judgment: O(n) since operations grow linearly...as good as possible
#Takes a value and adds before the before_node
    def addNodeBefore(self, new_value, before_node):
#warns user of a bad input
        if type(new_value) != int:
            print("Must input an integer")
        else:
#creates a headnode variable as the head
            headnode = self.head
#sets the new value applied using the Node class as the newnode
            newnode = Node(new_value)
#sets a new nextnode for the newnode using the value of headnode and sets the head as newnode if headnode's value equals before_node (with headnode being the relevant node)
            if headnode.nodevalue() == before_node:
                newnode.newnextnode(headnode)
                self.head = newnode
            else:
                n = 0
                while headnode != None:
                    if headnode.nodevalue() == before_node:
                        break
                    else:
#sets headnode equal to the nextnode and adds 1 to the length if headnode's value does not equal before_node
                        headnode = headnode.nextnode()
                        n = n + 1
#resets headnode as the head (with the newnode now being the headnode)
                headnode = self.head
#for each index in the list before the tail, headnode equals the nextnode (moving down the list)
                for i in range(n-1):
                    headnode = headnode.nextnode()
#creates a nextnode for the newnode using the value of headnode's nextnode
                newnode.newnextnode(headnode.nextnode())
#creates a nextnode for headnode using the value of the newnode (eventually applied to the matching node)
                headnode.newnextnode(newnode)
        #Computation complexity and judgment: O(n) since operations grow linearly...as good as possible
#Removes a node from the list
    def removeNode(self, node_to_remove):
#creates a headnode variable as the head
        headnode = self.head
#sets headnode equal to the nextnode and creates a new nextnode for headnode using the value of headnode's nextnode if the node_to_remove's value equals headnode's value
#(skipping ovr the former headnode)
        if node_to_remove.nodevalue() == headnode.nodevalue():
            headnode = headnode.nextnode()
            headnode.newnextnode(headnode.nextnode())
#sets the head equal to headnode
            self.head = headnode
        else:
            n = 0
            afternode = None
            while headnode != None:
#sets afternode equal to headnode's nextnode if headnode's value equals the node_to_remove's value
                if headnode.nodevalue() == node_to_remove.nodevalue():
                    afternode = headnode.nextnode()
                    break
                else:
#sets headnode equal to the next node (moving down the line) and adds 1 to the length if headnode's value does not equal the node_to_remove's value
                    headnode = headnode.nextnode()
                    n = n + 1
#resets the headnode variable as the head (the former nextnode)
            headnode = self.head
#for each index in the list before the tail, headnode equals the nextnode
            for j in range(n-1):
                headnode = headnode.nextnode()
#creates a new nextnode for headnode using the afternode's value (value after the headnode's nextnode)
            headnode.newnextnode(afternode)
        #Computation complexity and judgment: O(n) since operations grow linearly...good enough
#Takes a value, removes all nodes with that value
    def removeNodesByValue(self, value):
#creates a headnode variable as the head
        headnode = self.head
#sets the new value applied using the Node class as the newnode
        newnode = Node(value)
        while headnode != None:
#recursively applies removeNode applied to newnode
            self.removeNode(newnode)
#sets headnode equal to the nextnode (shifting each index after removal)
            headnode = headnode.nextnode()
        #Computation complexity and judgment: O(n) since operations grow linearly...as good as possible
#Reverses the order of the linked list
    def reverse(self):
#creates an empty variable before
        before = None
#creates a headnode variable as the head
        headnode = self.head
        while headnode != None:
#sets nextnode equal to the next node after headnode
            nextnode = headnode.next
#sets the next node after headnode equal to before
            headnode.next = before
#sets before equal to headnode
            before = headnode
#sets headnode equal to nextnode
            headnode = nextnode
#sets the head equal to before (finishing the reversal of positions)
        self.head = before
        #Computation complexity and judgment: O(n) since operations grow linearly...as good as possible
#Displays the list in some reasonable way
    def printlist(self):
#creates a headnode variable as the head
        headnode = self.head
        while headnode != None:
#prints headnode's value
            print(headnode.nodevalue())
#sets headnode equal to headnode's nextnode (moving through each value)
            headnode = headnode.nextnode()
        #Computation complexity and judgment: O(n) since operations grow linearly...good enough

#Tests
node1 = Node(7)
node1.nodevalue()
node2 = Node(3)
node2.nodevalue()
node2.newnodevalue(8)
node2.nodevalue()
node1.newnextnode(node2)
node1.nextnode().nodevalue()
node3 = Node("Howdy")
list1 = LinkedList(6)
list2 = LinkedList("Doody")
list1.addNode(4)
list1.addNode(2)
list1.addNode("Hmmm")
list1.length()
list1.printlist()
list1.addNodeAfter(4, 2)
list1.addNodeAfter("Okay", 4)
list1.addNodeBefore(5, 4)
list1.addNodeBefore("Cool", 5)
list1.printlist()
list1.removeNode(Node(5))
list1.removeNodesByValue(4)
list1.length()
list1.printlist()
list1.reverse()
list1.printlist()

#I'M STILL A LITTLE CONFUSED ABOUT COMPUTATIONAL COMPLEXITY...BUT I STILL TRIED TO MAKE MY CODE AS "EFFICIENT" AS POSSIBLE
