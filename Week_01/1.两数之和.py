#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for flag, i in enumerate(nums):
            for fj, j in enumerate(nums[(flag+1):]):
                if i + j == target:
                    return [flag, flag+fj+1]
                
# @lc code=end
# 自我点评：暴力法求解

