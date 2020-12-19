#1019. Next Greater Node In Linked List

'''
We are given a linked list with head as the first node.  Let's number the nodes in the list: node_1, node_2, node_3, ... etc.

Each node may have a next larger value: for node_i, next_larger(node_i) is the node_j.val such that j > i, node_j.val > node_i.val, and j is the smallest possible choice.  If such a j does not exist, the next larger value is 0.

Return an array of integers answer, where answer[i] = next_larger(node_{i+1}).

Note that in the example inputs (not outputs) below, arrays such as [2,1,5] represent the serialization of a linked list with a head node value of 2, second node value of 1, and third node value of 5.

Example 1:

Input: [2,1,5]
Output: [5,5,0]
Example 2:

Input: [2,7,4,3,5]
Output: [7,0,5,5,0]
Example 3:

Input: [1,7,5,1,9,2,5,1]
Output: [7,9,9,9,0,5,0,0]

Note:

1 <= node.val <= 10^9 for each node in the linked list.
The given list has length in the range [0, 10000].
'''

#Linked list node structure: 
class ListNode(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    #insert node into a linked list: 
    def listInsertion(self, data):
        #if the list empty, initialize head element: 
        newNode = ListNode(data)
        # if not self.head: 
        #     self.head = newNode

        #if the list is not empty:
        newNode.next = self.head
        self.head = newNode

    #function to traverse the linked list and print out all element in an array forms
    #for debugging purposes
    def printNode(self):
        temp = self.head 
        #array to store all the element in the linked list 
        arrayOfNode = []
        while temp:
            arrayOfNode.append(temp.value)
            temp = temp.next

        return arrayOfNode 
       
    #Function to find the next greater node in a linked list
    def nextLargerNodes(self):
        #base case: empty list would yeild empty list back
        if not self.head: 
            return []
        current = self.head
        #array to store the value of the linked list into 
        interger_array = []
        #conver the linked list into the interger array
        while current:
            interger_array.append(current.value)
            current = current.next

        stack = []
        answer = [0] * len(interger_array)

        #loop through the interger array while adding element and popping from it
        for i in range(len(interger_array)):
            while stack and interger_array[stack[-1]] < interger_array[i]:
                answer[stack.pop()] = interger_array[i]

            stack.append(i)

        return answer

#Time complexity: 0(n^2), the algorithm will have to traverse through all list node in the linked list
#Space complexity: O(n)

    def nextLargerNodes_OPTIMIZED(self):
        #base case: 
        if not self.head:
            return []

        current = self.head
        stack = []
        d = []
        answer = [] 
        i = 0
        result = [0] * 100000000
        while current:
            while stack and d[stack[-1]] < current.val:
                answer[stack.pop()] = current.val
            stack.append(i)
            i+=1
            d.append(current.val)
            current = current.next

        return result[:i]
            


#main function to run the test cases: 
def main():
    print("TESTING NEXT GREATER NODE IN A LINKED LIST...")
    #create a linked list: 
    llist = LinkedList()
    #test cases:
    input_1 = reversed([2,1,5])
    for i in input_1:
        llist.listInsertion(i)

    print(llist.printNode())
    print(llist.nextLargerNodes())

    input_2 =  [2,7,4,3,5]

    print("END OF TESTING...")
main()