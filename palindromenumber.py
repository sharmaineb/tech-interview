"""Given an integer x, return true if x is a 
palindrome
, and false otherwise.
Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1"""
# time complexity = O(log n)

class Solution:
    def isPalindrome(self, x):
        # check for special cases:
        # negative numbers & numbers that end with a 0
        # except 0 itself
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        # initialize the reversed number to 0
        reverse = 0

        # reverse the digits of the number by repeatedly dividing by 10 
        # then adding the remainder
        while x > reverse:
            reverse = reverse * 10 + x % 10
            x //= 10
        
        # if the length of the number is odd, we can ignore the middle digit
        return x == reverse or x == reverse // 10
    
if __name__ == "__main__":
    test = Solution()
    input = test.isPalindrome(121)
    print(input)

"""The isPalindrome function takes in an integer x and returns True if it is a palindrome, and False otherwise.

We first handle the special cases where the number is negative or ends with a 0 (except for 0 itself), which cannot be palindromes.

We then initialize a variable rev to 0, which will store the reversed number. We reverse the digits of the number 
x by repeatedly dividing it by 10 and adding the remainder to rev. We continue until x is less than or equal to rev.

If the length of the number is odd, we can ignore the middle digit since it can never affect the palindromic nature of 
the number. Therefore, we check if x is equal to rev or rev with the last digit removed (by dividing rev by 10).

We then return True if the number is a palindrome, and False otherwise."""

"""The time complexity of this algorithm is O(log n), where n is the input integer. 
This is because the algorithm divides the input integer by 10 at each iteration of the while loop, 
effectively reducing the size of the integer by a factor of 10. The number of iterations is proportional 
to the number of digits in the input integer, which is logarithmic in base 10."""

