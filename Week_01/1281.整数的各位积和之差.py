#
# @lc app=leetcode.cn id=1281 lang=python3
#
# [1281] 整数的各位积和之差
#

# @lc code=start
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        _sum, _product = 0, 1
        for i in list(str(n)):
            _sum += int(i)
            _product *= int(i)
        #print('sum:', _sum)
        #print('product:', _product)
        #print(_product - _sum)
        return _product - _sum

# @lc code=end

