"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""

# Go over the array and try to find two integers that add up to a target value
# using a dictionary to keep track
# enumerate() method adds a counter to an iterable and returns it in a form of enumerating object
# the enumerated object can then be used directly for loops or converted into a list of tuples using
# the list() function

# ````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

# Given an input array and some target. We want to find the two values in this input array that
# sum to that target value
# check every combination of two values and see if they sum up to the target

"""Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]."""

class Solution:
# create a function called twoSum
    def twoSum(self, nums, target):
# use a hash map/ element that comes before the current one. Previous element is going to be stored
# in this hash map. Mapping the value to the index of that value.
        hmap = {} # value : index
# iterate through every value in this array. use the index as well as the actual number
        for i, n in enumerate(nums):
# before we add to the map, check if the difference which is equal to the target minus number
            difference = target - n
# if the difference is already in the hash map
            if difference in hmap:
# if the difference is in the hash map, return the solution
# solution: pair of the indices
                return [hmap[difference], i]
# if we don't find the solution, update the hash map.
# continue since we are guaranteed that a solution exists
            hmap[n] = i
        return
    
# time complexity = O(n)
# Solution 2
# create a function called twoSum
def twoSum(self, nums, target):
# initialize a dictionary to keep track of nums (as key) and indices (as value)
        dict = {}
# loop over array using enumerate which results in both index and value elements in the array
# calculate the target num and check if target num is in the dictionary 
        for i in range(len(nums)):
            difference = target - nums[i]
# if it is the current num and num_target from the dictionary will result in the output           
            if difference in dict: 
                return [dict[difference], i]
# if not, you add the current num to the dictionary as it's going to be a num_target num
            else:
               dict[nums[i]] = i

if __name__ == "__main__":
    num_test = Solution()
    nums = num_test.twoSum([2,7,11,15], 9)
    print(nums)

"""The time complexity of this implementation is O(n), where n is the length of the input array nums. 
This is because the implementation only needs to loop over the input array once, and the dictionary 
lookups for each element take constant time on average. The time complexity is linear in the size of the input."""
