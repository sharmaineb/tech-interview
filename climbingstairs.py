"""You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. 

In how many distinct ways can you climb to the top?"""

"""Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps"""

# goal is two climb to two
# can take one step = 1
# two steps at once = 2
# can either take one step twice or one two step to get to 2

"""Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step"""

# time complexity = O(n)

# Solution
class Solution:
# create a function called climbStairs
    def climbStairs(self, n):
# have two variables that are both initialized as one
        one_step = 1
        two_step = 1
# loop through n minus 1 time
# continuously update the two variables one & two
        for i in range(n - 1):
# temp variable before other variables are updated
            temp_num = one_step
# update one. one is set to one plus two | adding two previous values = new result
            one_step = one_step + two_step
# update two to whatever the previous value of what one was | updating one
# before we update two 
# set two to the temporary variable | avoid setting it to one plus two             
            two_step = temp_num 
# return what one happens to land on        
        return one_step
    
if __name__ == "__main__":
    test = Solution()
    input = test.climbStairs(3)
    print(input)

"""The time complexity of this function is O(n) since it iterates through the 
loop n-1 times, and each iteration takes constant time. The time complexity is linear in terms of the input size n."""