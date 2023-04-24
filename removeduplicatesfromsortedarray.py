"""Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted."""

"""Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

# we want the output in ascending order sorted
# the first unique value, we're going to put in the first position right in index 0.
# second unique value, we're going to put it in the second position etc...
 
Constraints:
1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order."""

# take an array that could have duplicates and is in ascending order and then
# convert it into a new array where we remove the duplicates

# solution
# time complexity = O(n)

class Solution:
# create a function called removeDuplicates
    def removeDuplicates(self, nums):
# initialize pointers 
# start left & right pointers start at index 1.
        left_pointer = 1
# have right pointer iterate through the values in the input array
        for right_pointer in range(left_pointer, len(nums)):
# check if the value at index r is a new value or a value we've seen already
# compare it to the value that came before it at index r - 1
# if they're not the same == new unique value
            if nums[right_pointer] != nums[right_pointer - 1]:
# put the value where the left index is
                nums[left_pointer] = nums[right_pointer]
# increment the left pointer 
                left_pointer += 1
# return how many unique values are in the array
        return left_pointer
    
if __name__ == "__main__":
    test = Solution()
    input = test.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
    print(input)

"""The time complexity of the removeDuplicates function is O(n), where n 
is the length of the input array nums. This is because the function only 
needs to iterate through the input array once and perform constant-time 
operations for each element in the array. Specifically, it initializes 
two pointers and iterates through the array using a for loop. For each 
element in the array, it checks if the element is the same as the previous 
element, and if not, it moves the element to the left side of the array and 
increments the left pointer. Since the function performs constant-time operations 
for each element in the array, the time complexity is O(n)."""