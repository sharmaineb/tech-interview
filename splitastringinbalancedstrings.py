"""Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it into some number of substrings such that:

Each substring is balanced.
Return the maximum number of balanced strings you can obtain.

 

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
Example 2:

Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", each substring contains same number of 'L' and 'R'.
Note that s cannot be split into "RL", "RR", "RL", "LR", "LL", because the 2nd and 5th substrings are not balanced.
Example 3:

Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".
 

Constraints:

2 <= s.length <= 1000
s[i] is either 'L' or 'R'.
s is a balanced string."""

# time complexity = O(n)

class Solution:
    def balancedStringSplit(self, s):
        count = 0
        balance = 0

        for c in s: 
            if c == 'L':
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                count += 1
        return count

if __name__ == "__main__":
    test = Solution()
    input = test.balancedStringSplit("RLRRRLLRLL")
    print(input)

"""The balancedStringSplit function takes in a string s and returns the maximum number of balanced substrings that can be formed by splitting s.
We first initialize count and balance to 0. The variable count will keep track of the number of balanced substrings, and balance will keep track 
of the current balance of the string, which is the difference between the number of 'L's and 'R's seen so far.
We then iterate over each character in s. If the character is an 'L', we increment balance. If it is an 'R', we decrement balance. Whenever 
balance becomes 0, it means we have a balanced substring. We increment count and continue iterating over the rest of the string.
We then return count.
This solution has a time complexity of O(n), where n is the length of s, as we iterate over each character in the string once. 
It has a space complexity of O(1), as we are using only constant extra space for count and balance.
The time complexity of this code is O(n) where n is the length of the input string s. 
This is because the code iterates through every character in the string exactly once, 
performing constant-time operations with each character. Therefore, the time taken by the algorithm is proportional 
to the length of the input string."""