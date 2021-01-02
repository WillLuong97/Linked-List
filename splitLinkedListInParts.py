#Problem 725. Split Linked List in Parts
'''
Given a (singly) linked list with head node root, write a function to split the linked list into k consecutive linked list "parts".

The length of each part should be as equal as possible: no two parts should have a size differing by more than 1. This may lead to some parts being null.

The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal parts occurring later.

Return a List of ListNode's representing the linked list parts that are formed.

Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]
Example 1:
Input:
root = [1, 2, 3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The input and each element of the output are ListNodes, not arrays.
For example, the input root has root.val = 1, root.next.val = 2, \root.next.next.val = 3, and root.next.next.next = null.
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but it's string representation as a ListNode is [].
Example 2:
Input: 
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
Note:

The length of root will be in the range [0, 1000].
Each value of a node in the input will be an integer in the range [0, 999].
k will be an integer in the range [1, 50].
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#Definition of a linked list object: 
class LinkedList:
    def __init__(self):
        self.root = None
    #function to print out a linked list: 
    def printLinkedList(self):
        if not self.root: 
            return None
        
        current = self.root
        while current.next: 
            print(current.val + "->")
            current = current.next

    #list node insertion to the tail: 
    def insertNode(self, new_data):
        if not self.root: 
            root = ListNode(new_data)
        else: 
            current = self.rootoot
            while current.next:
                current = current.next
            current.next = ListNode(new_data)
        return root
            


    #Helper method to check the count the number of nodes in the linked list: 
    def countNode(self):
        if not self.root: 
            return None
        count = 0
        current = self.root
        while current:
            count += 1
            current = current.next

        return count 

    #Function to split the linked list into equal parts
    def splitListToParts(self, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        result = []
        nodeCount = self.countNode()
        subArray = []
        current = self.root
        needed = nodeCount // k
        remainder = nodeCount % k
        for i in range(k):#loop through equal parts
            head = current
            #build the sub array based on the needed and remainder
            for j in range(needed + (i < remainder) - 1):
                if current: 
                    current = current.next
            #after the sub array has been created, we will move to the next sub array with the next node element in the linked list
            if current: 
                current.next, current = None, current.next
            result.append(head)

        return result


#Main function to run the test cases:
def main():
    print("TESTING SPLIT LINKED LIST IN PARTS...")
    firstNode = ListNode(1)
    secondNode = ListNode(2)
    thirdNode = ListNode(3)
    llist = LinkedList()
    llist.root = firstNode
    llist.root.next = secondNode
    secondNode.next = thirdNode
    k = 5
    print(llist.splitListToParts(k))
    print("END OF TESTING...")
main()
