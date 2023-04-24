"""Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s."""

class Solution:
    def lengthOfLastWord(self, s):
        # remove any trailing spaces from the string
        s = s.rstrip()

        # initialize a counter for the length of the last word
        length = 0

        # traverse the string from right to left
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
        # if we come across a space, we have reached
        # the end of the last word
                break
            else:
                length += 1
        # return the length of the last word
        return length

if __name__ == "__main__":
    test = Solution()
    input = test.lengthOfLastWord("   fly me   to   the moon  ")
    print(input)

"""The time complexity of this solution is O(n), where n is the length of the input string 's'. 
The reason is that the algorithm traverses the string from right to left only once, 
looking for the last word and counting its length. Since the time it takes to traverse the string is 
proportional to the length of the string, the time complexity is O(n)."""
