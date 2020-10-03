#Python3 program to implement a linked list structure
#List Node structure 
class Node:
    #Function to initialize the node object
    def __init__(self, value):
        self.value = value  #Assign data
        self.next = None    #Initialize the next data as null
#Linked list structure
class LinkedLst:
    #function initialize a head node
    #Head node is often empty the linked list at this point has not been created yet
    def __init__(self):
        self.head = None

    #Fucntion to traverse a linked list and print out each element in the linked list
    def printNode(self):
        temp = self.head
        listNode = []
        while temp: 
            listNode.append(temp.value)
            temp = temp.next
        print(listNode) 
    #Function to reverse a linked list
    #Input: 1 -> 2 -> 3 -> 4 -> 10 -> 6
    #Output: 6 -> 10 -> 4 -> 3 -> 2 -> 1
    def reverseList(self):
        #the current element that we look at
        current = self.head
        #previous node to look at
        prev = None

        #looping through the linked list
        while current: 
            #getting the next node of the current node
            nextNode = current.next
            #setting the next node of the current to be the previous node (pointing the arrow backward)
            current.next = prev
            #move up in the linked lsit
            #let the previous node be the current node
            prev = current
            #current node to be the next node.
            current = nextNode
        #adding the reversed node into the tree. 
        self.head = prev

    #Function to delete a node in the linked list: 
    #The function will recieve a node value that needed to be deleted and then delete that node out of the linked list
    #Input: 1 -> 2 -> 3 -> 4 -> 10 -> 6 ,val = 10
    #Time complexity: Best case: O(1) if the head of the list or tail of the list is the node to be removed, this way, the deletion could happen immediately without the traversal.
                    #Average case: O(n) if the element to be removed is inside the list, so we will have to loop through the linked, with n being the length of the list. Worse case: O(n)
    #Output: 1 -> 2 -> 3 -> 4 -> 6
    def removeNode(self, val):
        #base case: 
        if not val: 
            return self.head.next

        #create a dummy node to look at all the previous element of a current node
        prev = Node(0)

        #conenct this dummy node to linekd list
        prev.next = self.head
        #traverse through the linked list and look for the element that we tries to remove
        while prev.next:
            if prev.next.value == val:
                prev.next = prev.next.next
            else: 
                prev = prev.next

        return self.head.next

    #Function to remove a group of node that are in a list in a linked list
    #Input: 1 -> 2 -> 3 -> 4 -> 10 -> 6 ,val = [1,2,3]
    #Output: 4 -> 10 -> 6 
    def removeGroupNode(self, nodes):
        #base case: 
        if not nodes:
            return self.head.next 
        
        #Dummy node to store the value that are previous to the current element
        previous = Node(0)
        #Connect the dummy node to the linked list
        previous.next = self.head
        #traverse through the linked list and look for any elements that are contained in the node
        while previous.next: 
            #if the next node of the dummy node is contained in the array, we will remove it
            if previous.next.value in nodes: 
                previous.next = previous.next.next
            #skip it and move to the next node
            else: 
                previous  = previous.next

        return self.head.next

    #Function to insert a node into the linked list: (Insertion into the tail)
    #Input: 1 -> 2 -> 3 -> 4 -> 10 -> 6, target = 5
    #Output: 1 -> 2 -> 3 -> 4 -> 10 -> 6 -> 5
    #Time complexity: O(n) with n being the length of the linked list, we will always have to go through the end of the list to add the target elemenet into
    def insertNode_LAST(self, target):
        #Base case: if there is no target to pass element in, then just return the current linked list
        if not target: 
            return self.head.next

        #create an instance of the Node object to pass in the target
        target_node = Node(target)
        #base case: if the list is empty, we will add the target value into the head. 
        if self.head is None:
             self.head = target_node
        #intialize a dummy node to look at each element in the linked list
        current = self.head
        #loop throught the linked list and add the target value into the linked list. 
        while current:
            if current.next == None: 
                current.next = target_node
                target_node.next = None
            current = current.next
        return current

    #Function to insert a node into a linked list: (Insertion into the head)
    #Input: 1 -> 2 -> 3 -> 4 -> 10 -> 6, target = 5
    #Output: 5 -> 1 -> 2 -> 3 -> 4 -> 10 -> 6
    #Time complexity: O(1), this is a constant time operation since we only have to reference the head node and add element into it
    def insertNode_HEAD(self, target):
        #base case: if there is no target to insert
        if not target: 
            return self.head.next
        target_node = Node(target)
        #base case: if the linked list is empty, and the head node is Null
        if self.head is None: 
            self.head = target_node
        
        currentHead = self.head
        self.head = target_node
        self.head.next = currentHead
        
        return self.head.next

            
    #Funtion to insert a node into a linked list after a given value: 
    def insertNode_GIVEN(self,target, position):
        pass


#Main function to creaete list node
def main():
    print("Linked List Implementation")
    print("")
    #create a linked list by creating an instance of class linked list
    llist = LinkedLst()
    #The first node is also the head node
    llist.head = Node(1)
    #the second node and the third node
    second = Node(2)
    third = Node(3)
    forth = Node(4)
    five = Node(10)
    six = Node(5)
    #adding element into a linked list
    llist.head.next = second
    second.next = third
    third.next = forth
    forth.next = five
    five.next = six
    print("Created singly linked list is below: ")
    llist.printNode()

    print("")
    print("Reversing a linked list")
    llist.reverseList()
    llist.printNode()

    print("")
    print("Node Deletion")
    llist.removeNode(None)
    llist.printNode()
    print("")
    print("Remove node that are in a list of node.")
    nodes = [1,2,3]
    llist.removeGroupNode(nodes)
    llist.printNode()
    print("Insert Node Into The End of The List...")
    target = 6
    target_NULL = None
    target_12 = 12
    
    llist.insertNode_LAST(target)
    llist.printNode()
    llist.insertNode_LAST(target_NULL)
    llist.printNode()
    llist.insertNode_LAST(target_12)
    llist.printNode()
    print("Insert Node Into Head Of The List...")
    headTarget = 7
    emptyLL = LinkedLst()
    emptyLL.head = None
    emptyLL.insertNode_LAST(target)
    emptyLL.printNode()
    llist.insertNode_HEAD(headTarget)
    emptyLL.insertNode_HEAD(headTarget)
    llist.printNode()
    emptyLL.printNode()
    print("")

main()