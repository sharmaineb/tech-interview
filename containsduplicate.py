"""Given an integer array nums, return true if any value appears at

least twice in the array, and return false if every element is distinct."""

# Example 1:
# Input: nums = [1,2,3,1]
# Output: True

"""Give these numbers. If we look at the first number. How do we know if it is a
duplicate or not? Compare it to every single number in the array. We'd have to do that 
for every number. """

# Sort
# If we sort the input, every duplicates in the array, they will be next to each other
# we'd only have to iterate once. 
# Use a hash set = allows us to check our hashmap if a certain value exists

"""Sets in Python:
a set in python is an unordered group of data that you can iterate through, can change its values
and doesn't have any duplicate elements. Works well if using it to check whether a certain element
is present in the set."""

"""set add() = adds a given element to a set if the element is not present in the set."""

# Solution
class Solution:
# create a function called containsDuplicate
    def containsDuplicate(self, nums):
# create hash set
        hash_set = set()
# go through every value in the input array
        for n in nums:
# is n a duplicate? does it already exist in our hash set.
# if it does, we know our array contains duplicates = return True
            if n in hash_set:
                return True
# if it doesn't contain a duplicate, add the value and the iterate through
# the rest of nums and then the loop with quit = return False to show that we
# did not find any duplicates
            hash_set.add(n)
        return False

if __name__ == "__main__":
    num_test = Solution()
    nums = num_test.containsDuplicate([1,2,3,1])
    print(nums)