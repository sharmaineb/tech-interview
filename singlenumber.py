"""Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space."""

"""Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 
Constraints:
1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once."""
# time complexity = O(n)

class Solution:
# create a function called singleNumber
    def singleNumber(self, nums):
        # create a dictionary
        dictionary = {}
        # create a for loop to iterate over given array
        for val in nums:
        # check if value in dictionary
            if val not in dictionary:
                dictionary[val] = 1
             
            else:
                dictionary[val] += 1
        
        for val in dictionary:
            if dictionary[val] == 1:
        # return the value that does not appear twice
                return val
            
if __name__ == "__main__":
    test = Solution()
    input = test.singleNumber([4,1,2,1,2])
    print(input)

"""The "Single Number" problem is a fairly simple algorithmic problem that asks you to find a unique 
number in an array where all other numbers occur twice. More specifically, you are given an array of integers, 
where each integer appears twice except for one integer which appears only once. You need to find and return the unique integer.

Here's an example to illustrate the problem:

Input: [2,2,1]
Output: 1

In this example, the array contains the numbers 2 and 1. The number 2 appears twice, and the number 1 appears once. 
Therefore, the function should return 1.

To solve this problem, you can use the XOR (exclusive or) operator. The XOR operator returns
a 1 in each bit position where the corresponding bits of either but not both operands are 1. 
In other words, if you XOR a number with itself, the result is 0, and if you XOR a number with 0, 
the result is the original number.

So, to find the unique number in the array, you can simply XOR all the numbers in the array together. 
Since the duplicate numbers will cancel each other out, the result will be the unique number.

The time complexity of this code is O(n), where n is the length of the input list nums. 
The first for loop iterates through all elements in nums once, and the second for loop iterates 
through all elements in the dictionary once, so the total number of iterations is 2n, 
which simplifies to O(n) as the dominant term."""