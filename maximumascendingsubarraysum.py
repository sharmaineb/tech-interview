"""Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.

A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi  < numsi+1. Note that a subarray of size 1 is ascending.

 

Example 1:

Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.
Example 2:

Input: nums = [10,20,30,40,50]
Output: 150
Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.
Example 3:

Input: nums = [12,17,15,13,10,11,12]
Output: 33
Explanation: [10,11,12] is the ascending subarray with the maximum sum of 33.
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100"""
# time complexity = O(n)

class Solution:
    def maxAscendingSum(self, nums):
        if not nums: 
            return 0
        
        current_sum = max_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                current_sum += nums[i]
            else:
                current_sum = nums[i]
            max_sum = max(max_sum, current_sum)

        return max_sum

if __name__ == "__main__":
    test = Solution()
    input = test.maxAscendingSum([10,20,30,40,50])
    print(input)

"""The maxAscendingSum function takes in a list of integers nums and returns the maximum sum of an ascending subarray in the list.

We first check if the list is empty. If so, we return 0 as there are no ascending subarrays in an empty list.

We then initialize current_sum and max_sum to the first element of the list, as a subarray containing only the first element is necessarily ascending.

We then iterate over the rest of the elements in the list, comparing each element to the previous element. If the current element is greater than the 
previous element, we add it to current_sum. If not, we reset current_sum to the current element, as we start a new ascending subarray.

At each iteration, we update max_sum with the maximum of its current value and current_sum, as we want to keep track of the maximum sum seen so far.

We then return max_sum."""

"""The time complexity of the given code is O(n) where n is the length of the input list nums. This is because the code traverses 
the list once and performs 
constant-time operations on each element. The time taken to execute the code grows linearly with the size of the input list."""