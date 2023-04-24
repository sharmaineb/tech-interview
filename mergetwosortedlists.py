"""You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list."""

# given two linked lists
# both are sorted. we want to merge them = output linked list
# using the given nodes 

"""Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution
# time complexity = O(n)

class Solution:
# create a function called mergeTwoLists
    def mergeTwoLists(self, list1, list2):
# create dummy node so you don't insert into an empty list
        node = ListNode()
# tail of the list is initially the dummy node
        tail = node 
# iterate through the two lists
# while list1 and list2 are non-null | we can do our comparison
        while list1 and list2:
# if the value of list1 is less than the value of list2
            if list1.val < list2.val:
# take list1 value and insert it to the tail
# update list1
                tail.next = list1
                list1 = list1.next
# if list2 is less than or equal
# list2 is inserted
# update tail
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
# what if one list is empty but the other is not
# find the non-empty list 
# insert it to the end of the results
        if list1:
            tail.next = list1
# if list2 is non-null
# only one of them can be non-null
        elif list2:
            tail.next = list2
        
        return node.next



if __name__ == "__main__":
    test = Solution()
    input = test.mergeTwoLists([1,2,4], [1,3,4])
    print(input)

"""The time complexity of mergeTwoLists is O(n), where n is the total number of nodes in the two input lists.

This is because we iterate through both lists once, comparing and appending nodes until we reach the end of 
one of the lists. We then simply append the remaining nodes of the non-empty list to the end of our result list.

The time complexity of the function is directly proportional to the total number of nodes in the input lists, resulting in a linear time complexity of O(n)."""