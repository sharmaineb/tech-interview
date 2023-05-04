"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters."""

class Solution:
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        for i in range(len(haystack) + 1 - len(needle)):
            if haystack[i: i + len(needle)] == needle:
                return i
        return - 1

if __name__ == "__main__":
    test = Solution()
    input = test.strStr(haystack = "sadbutsad", needle = "sad")
    print(input)

"""Search for a substring within another strings
Looking for a needle in a haystack
For example, can we find the needle(substring) inside of the other string and if we can, where is the first index that this string(needle) appears at. 
What index are we going to return? It should be the starting index where the substring starts within the other string.
If the needle does not exist in the haystack, we return -1 as the index because we can’t find it.
Another edge case, what if the needle is an empty string?
In this case, we can return 0.
Algorithm used: nested for loops.
Time complexity: using a nested for loop for this problem. So the outer for loop is going to be iterating through every starting position in the haystack.
How many positions could it be?
For every single starting position, we’re going to look at every single character in the haystack.
So the time complexity is going to be the multiplication of the length of both the needle and the haystack. That’ll be big O(n * m).  

NOTES FOR CODE:
First check if the needle is empty, if it is, we can return 0 immediately.
If needle is non-empty:
Outer for loop use index i, go through every starting position in the haystack
Inner for loop use index j, and we’ll go through every character in the needle
Does every character in the needle match the current portion of the haystack
If they don’t match, at index i + j, we start at i and j will be our incrementer
If it is not equal to needle, which is j as we’re starting at the beginning of.
If not equal, break out of for loop and then look at next i position in haystack
If they are equal, then we continue with the next iteration of this loop until we have seen every single character and confirmed they are equal
How do we check that?
When j is equal to the last index of the needle which is length of needle minus one
Then we can return the index of the beginning which was index i
If that didn’t happen then we move on to the next iteration of the for loop and then do the same
But if we never found a match substring, then we can return negative 1 outside of the loop
If the haystack, starting at index i, which goes up until index i plus the length of the needle
So this substring is equal to the needle
So we’re comparing the substring of the haystack starting at index i checking if it’s equal to the needle
If it is equal we can return i
If not, we’ll try at the next index of i and check if it’s going to be equal
We’re checking every possibility 
Space complexity is big 0 of 1 because we’re not really using any extra space. 
"""