"""Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order."""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# time complexity = O(n)

class Solution:
    def deleteDuplicates(self, head):
        # initialize a pointer to the head node
        current = head

        # traverse the list and remove duplicates
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        # return the modified list
        return head

if __name__ == "__main__":
    test = Solution()
    input = test.deleteDuplicates([1,1,2,3,3])
    print(input)

"""The deleteDuplicates function takes in the head node of a sorted linked list and returns a new linked list with 
duplicates removed.

We initialize a pointer current to the head node of the list and traverse the list using a while loop. At each iteration, we compare the value of 
the current node with the value of its next node. If they are the same, we remove the next node by pointing the current 
node's next pointer to the next node's next pointer. If they are different, we move the current pointer to the next node.

We then return the modified linked list.
"""

"""The time complexity of this algorithm is O(n), 
where n is the length of the input linked list. 
This is because the algorithm iterates through each node in the linked list once, 
and each comparison and pointer manipulation operation takes constant time."""