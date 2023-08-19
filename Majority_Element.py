'''

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

'''
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        limit = len(nums) / 2
        unique_values = []
        for x in nums:
            if x not in unique_values:
                unique_values.append(x)

        for j in unique_values:
            if nums.count(j) > limit:
                return j
