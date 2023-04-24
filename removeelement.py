"""Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted."""

"""Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""

"""Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores)."""

# solution
class Solution:
# create a function called removeElement
    def removeElement(self, nums, val):
# start pointer at index 0
        pointer = 0
# iterate over every single value in the input array
        for i in range(len(nums)):
# if we see a value that's not equal the number of elements in nums = swap
# taking all values in nums that are not a particular value and putting them at the 
# beginning of nums
            if nums[i] != val:
# if it's not the value we're looking for then we can put it in our index pointer
                nums[pointer] = nums[i]
# increment pointer by num
                pointer += 1
# return pointer
        return pointer
    
if __name__ == "__main__":
    test = Solution()
    input = test.removeElement([0,1,2,2,3,0,4,2], 2)
    print(input)

# time complexity = O(n)
"""The time complexity of this code is O(n), where n is 
the length of the input array "nums". 
This is because the code iterates over each element in the array once, 
performing constant-time operations for each element. 
The worst-case scenario is that all elements in the array are equal 
to the given value "val", in which case the code still performs n operations. 
The time complexity is O(n)."""