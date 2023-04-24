"""You are given a list of integers, and you need to write a function that returns a list 
containing the sum of each consecutive pair of integers in the original list. For example, 
given the list [1, 2, 3, 4], the function should return [3, 5, 7].

Write a Python function that takes a list of integers as input and returns a list of integers 
as output according to the above specification. Your solution should be efficient and well-structured, 
and you should be prepared to explain your thought process and any design choices you made."""
# time complexity = O(n)

def consecutive_sum(nums):
    """
    Takes a list of integers and returns a list of integers
    containing the sum of each consecutive pair of integers in the
    original list.
    """
    result = []
    for i in range(len(nums) - 1):
        result.append(nums[i] + nums[i+1])
    return result

nums = consecutive_sum([1,2,3,4])
print(nums)
"""This solution uses a for loop to iterate over the list of integers, and adds each consecutive pair of 
integers to a new list. The for loop stops at the second-to-last element in the list to prevent an out-of-bounds error 
when trying to access nums[i+1]."""

"""Example 1:
input: nums = [1, 2, 3, 4]
consecutive_sum(nums)
output: [3, 5, 7]

The algorithm uses a loop to iterate over the nums list, and for each iteration, 
it performs a constant amount of work to compute the sum of the current element and 
the next element in the list. The time complexity of this algorithm is O(n), 
where n is the length of the input list. This is because the algorithm needs to iterate 
over every element in the input list once to compute the sum of each consecutive pair."""