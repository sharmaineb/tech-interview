"""Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer."""

class Solution:
# create a function called romanToInt
    def romanToInt(self, s):
# largest value to smallest value = add them up
# smaller value before larger value = subtract them
# create hash map
        roman_numerals = { "I" : 1, "V" : 5, "X" : 10, "L" : 50,
             "C" : 100, "D" : 500, "M" : 1000}
# set result to 0        
        result = 0
# iterate through the input string with for loop
# iterate through the length of string
        for i in range(len(s)):
# check if we're going to subtract the value
# check if there's a character that comes after it = compare the values
# what's the value of the character at index i | pass in key value
# check if it's smaller than the next character
            if i + 1 < len(s) and roman_numerals[s[i]] < roman_numerals[s[i + 1]]:
# supposed to be in decreasing order but if it is in increasing order 
# smaller value has to be subtracted from the results                   
                result -= roman_numerals[s[i]]
# otherwise we're going to add the value
            else:
                result += roman_numerals[s[i]]
# return result
        return result

if __name__ == "__main__":
    test = Solution()
    input = test.romanToInt("III")
    print(input)