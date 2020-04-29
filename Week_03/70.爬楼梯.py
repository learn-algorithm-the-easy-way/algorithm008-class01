#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#爬楼梯
Category	Difficulty	Likes	Dislikes
algorithms	Easy (48.28%)	957	-
Tags
dynamic-programming

Companies
adobe | apple

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
Discussion | Solution

#####################################
# 2020-04-28 21:44:40 看老师w3l7v2的视频之后，尝试带入模板失败，基本上写出下面的框架后就放弃了。
# 2020-04-28 21:46:19 现在回看，主要是卡在了归纳的时候对本级的处理理解的不到位导致的。

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        # this level
        x = 2
        r = 
        # next level
            climbStairs(self, x+1)
        
# @lc code=end

#####################################
# 2020-04-28 21:45:25
# 看到视频里提到的数学归纳法，之前老师有讲过，没记住，先归纳出递归的公式，之后再套用模板试一下
# 1: 1
# 2: 2
# 3: f(1) + f(2) 这里的思考理解成要上到第三级台阶只能从第二级台阶上一个台阶或者从第一级台阶上两个这样来走 （还要思考漏项或者重复项的可能性） mutual exclusive, complete exhaustive
# 4: f(2) + f(3)
# f(n) = f(n-1) + f(n-2) : Fibonacci
