'''

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


check min string from each word
and loop through word from start
if first word of each word is not same
then return empty string
otherwise compare all word from start until there is different

'''
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        string = ""
        list_min = min([len(i) for i in strs])
        print(f"list_min {list_min}")
        #loop through each vocabs with for loop (with min string from words)
        for i in range(list_min-1):
            if strs[0][i] == strs[1][i] == strs[2][i]:
                return strs[0][i]
        return string





solution = Solution()

strs = ["flower" , "flow" , "flight"]
print(solution.longestCommonPrefix(strs))