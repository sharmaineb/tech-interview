"""Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character."""

class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

"""The reverseString function takes in a list of characters s and modifies it in-place to reverse its order.

We first initialize two pointers, left and right, to the beginning and end of the list, respectively.

We then use a while loop to swap the characters at the left and right positions, and increment left and decrement 
right until they meet in the middle of the list.

We are modifying s in-place, so we do not need to return anything from the function.

This solution has a time complexity of O(n/2), which simplifies to O(n), as we are swapping each character once. 
It has a space complexity of O(1), as we are modifying the input list in-place and using only constant extra space."""