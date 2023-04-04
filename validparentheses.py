"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type."""

"""Example 1:

Input: s = "()"
Output: true

# started with open parentheses and closes in a closed parentheses.
# closed in the correct order.

Example 2:

Input: s = "()[]{}"
Output: true

# parentheses, brackets, and curly braces are open and closed in the
# correct order.

Example 3:

Input: s = "(]"
Output: false

# the order is off, they don't match each other. 
 
Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'."""

# O(n) = time complexity
# O(n) = space complexity

# solution
class Solution:
# create a function called isValid
    def isValid(self, s):
# initiate list
        parentheses_list = []
# create map for close to open parentheses 
        close_to_open = { ")" : "(", "]" : "[", "}" : "{"}
# iterate through every character in the input string
        for char in s:
# if the character is in close_to_open map == closing parentheses
            if char in close_to_open:
# make sure our list is not empty
# cannot add a closing parentheses to an empty list
# check if the value at the top of our list is matching the opening parentheses
                if parentheses_list and parentheses_list[-1] == close_to_open[char]:
# if they match we can pop from our stack | removing an element at a specific position
                    parentheses_list.pop()
# if they don't match or the list is empty return false
                else:
                    return False
# if we get an open parentheses, take the char and append it to list
            else:
                parentheses_list.append(char)
# once we've gone through every char we can only return True
# if our list is empty otherwise we return false 
        return True if not parentheses_list else False
    
if __name__ == "__main__":
    test = Solution()
    input = test.isValid("()[]{}")
    print(input)

