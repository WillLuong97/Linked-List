# Leetocode 147. Insertion Sort List

'''
Problem statement: 
Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
'''
#Linked list structure
class ListNode: 
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

#Function to insertion sort a linked list: 
def insertionSortList(head):
    #base case: empty list, no return 
    if not head: 
        return None
    
    #create a dummy node to move element from the head list and 
    #sort them in a new list
    dummyNode = ListNode()
    current = head
    #loop through the linked list to compare and move element around until it is fully sorted
    while current: 
        prevPtr = dummyNode
        nextPtr = dummyNode.next
        while nextPtr: 
            #if the element already sorted, break out of this and place it in the new list
            if current.val < nextPtr.val: 
                break 
            #if not keep moving the pointer until it reaches an element that is greater than it
            prevPtr = prevPtr.next
            nextPtr = nextPtr.next
        #move the element from the head linked list into the new linked list
        tmp = current.next
        current.next = nextPtr
        prevPtr.next = current
        current = tmp 
        
    return dummyNode.next



#function to sort a list with insertion sort: 
#time complexity: O(N^2)
#space complexity: O(1)
def insertionSort(nums):
    #base case: 
    if not nums:
        return None
    #loop through the nums to begin the insertion sort: 
    for i in range(len(nums)):
        currentValue = nums[i]
        #swap the element if they are not sorted: 
        while i > 0 and nums[i-1] > currentValue:
            nums[i] = nums[i-1]
            i = i - 1 
        nums[i] = currentValue
            

#main function to test the program: 
def main():
    print("TESTING INSERTION SORT...")
    nums = [5,6,1,3,2]
    print(insertionSort(nums))
    print(nums)
    print("END OF TESTING...")
main()