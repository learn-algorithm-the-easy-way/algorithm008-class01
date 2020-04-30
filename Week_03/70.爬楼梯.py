#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#爬楼梯
#Category	Difficulty	Likes	Dislikes
#algorithms	Easy (48.28%)	957	-
#Tags
#dynamic-programming
#
#Companies
#adobe | apple
#
#假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
#每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
#注意：给定 n 是一个正整数。
#
#示例 1：
#
#输入： 2
#输出： 2
#解释： 有两种方法可以爬到楼顶。
#1.  1 阶 + 1 阶
#2.  2 阶
#示例 2：
#
#输入： 3
#输出： 3
#解释： 有三种方法可以爬到楼顶。
#1.  1 阶 + 1 阶 + 1 阶
#2.  1 阶 + 2 阶
#3.  2 阶 + 1 阶
#Discussion | Solution

################################################################################
# 2020-04-28 21:44:40 看老师w3l7v2的视频之后，尝试带入模板失败，基本上写出下面的框架后就放弃了。
# 2020-04-28 21:46:19 现在回看，主要是卡在了归纳的时候对本级的处理理解的不到位导致的。

# @lc code=start
#class Solution:
#    def climbStairs(self, n: int) -> int:
#        if n == 1:
#            return 1
        
        # this level
#        x = 2
#        r = 
        # next level
#            climbStairs(self, x+1)
        
# @lc code=end

################################################################################
# 2020-04-28 21:45:25
# 看到视频里提到的数学归纳法，之前老师有讲过，没记住，先归纳出递归的公式，之后再套用模板试一下
# 1: 1
# 2: 2
# 3: f(1) + f(2) 这里的思考理解成要上到第三级台阶只能从第二级台阶上一个台阶或者从第一级台阶上两个这样来走 （还要思考漏项或者重复项的可能性） mutual exclusive, complete exhaustive
# 4: f(2) + f(3)
# f(n) = f(n-1) + f(n-2) : Fibonacci
################################################################################
# 2020-04-29 10:57:21
# 已知公式f(n) = f(n-1) + f(n-2), 现在的核心就是要尝试写出递归
# 2020-04-29 13:41:47
# 利用20分钟尝试了一下
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        elif n == 2: return 2
        else: return self.climbStairs(n-1) + self.climbStairs(n-2) 
# Time Limit Exceeded
# 16/45 cases passed (N/A)
# Testcase
# 38
# 自己手工试了一下
if __name__ == "__main__":
    #print(Solution().climbStairs(6))

    for i in range(1,38):
        print("{}: {}".format(i, Solution().climbStairs(i)))
# 自己手工试了一下，到最后时间的确非常的长。
1: 1
2: 2
3: 3
4: 5
5: 8
6: 13
7: 21
8: 34
9: 55
10: 89
11: 144
12: 233
13: 377
14: 610
15: 987
16: 1597
17: 2584
18: 4181
19: 6765
20: 10946
21: 17711
22: 28657
23: 46368
24: 75025
25: 121393
26: 196418
27: 317811
28: 514229
29: 832040
30: 1346269
31: 2178309
32: 3524578
33: 5702887
34: 9227465
35: 14930352
36: 24157817
37: 39088169

# 中间遇到了一个小的报错，关于self的问题，参考https://www.jianshu.com/p/814d65a9c404 解决。

# 再来看题解，优化“傻递归”
################################################################################
# 2020-04-29 13:49:15
# 尝试题解中增加列表储存结果的
# 2020-04-29 14:25:40 增加数组的递归没搞定，搞定了类似题解中方法三的动态规划的方法
# 其中的注意点是：python的数组要动态的增加，如果无法做到动态增加，在最开始直接分配相应的大小
# 注意对初始情况的验证和调整
# 但是递归的模板还是没用上...
Accepted
45/45 cases passed (40 ms)
Your runtime beats 53.75 % of python3 submissions
Your memory usage beats 20.59 % of python3 submissions (13.7 MB)

class Solution:
    def climbStairs(self, n: int) -> int:
        r = [0,1,2] + [0] *(n-2)
        #print(r)
        if n == 1: return 1
        elif n == 2: return 2
        else:
            for i in range(3,n + 1):
                r[i] = r[i - 1] + r[i - 2]
        #print(r)
        return r[n]
################################################################################
# 2020-04-29 14:52:59 
# 再次尝试增加数组的方式还是失败了，回来看题解，再看老师的视频
# https://leetcode.com/problems/climbing-stairs/discuss/25296/3-4-short-lines-in-every-language
# 这里的关键思路是 a,b = b, a+b 这一步每一次的切换中一定要去处理的
# 综上，这道题在初期理解的时候可以用递归或者循环的方式来理解，但不是递归的典型案例。
# 先暂时放下这道题，等把典型的递归题搞明白了再回来看这题。