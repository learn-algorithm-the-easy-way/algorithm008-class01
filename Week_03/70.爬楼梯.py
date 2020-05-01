#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
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
################################################################################
# 继续向前走，但是这里递归的问题没解决，
# TODO: 后面还是得回来解决傻递归&带记忆的递归的方案
# TODO: 做其他的递归题目，回看老师的递归讲解视频
# TODO: 训练 62\91\509 继续巩固
################################################################################
# 自己写的带记忆的递归（失败）
class Solution:
    def climbStairs(self, n: int) -> int:
        array = [] * (n + 1)
        return climb_staris(0, n, array)

def climb_staris(level, _max, array):
    if level > _max: return 0
    if level == _max: return 1
    if array[level]:
        return array[level]
    # process
    array[level] = climb_staris(level + 1, _max, array) + climb_staris(level + 2, _max, array)
    return array[level]
    # drill down
    # reverse state
################################################################################
# 2020-05-01 17:09:29
#看题解，递归的修改不是很成功，但是看懂了其他的内容:

# 代码收藏
class Solution:
    def climbStairs(self, n: int) -> int:
        f = [1, 2]
        for i in range(2, n):
            f.append(f[i-1] + f[i-2])
        return f[n-1]

#作者：what-to-do
#链接：https://leetcode-cn.com/problems/climbing-stairs/solution/solution-python3-by-bu-zhi-dao-gan-sha/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def climbStairs(self, n: int) -> int:
        a = b = 1
        for _ in range(n):
            a, b = b, a + b
        return  a
# 来自光头哥...
# https://leetcode.com/problems/climbing-stairs/discuss/25296/3-4-short-lines-in-every-language
# Similar questions:
#91. Decode Ways
#62. Unique Paths
#509. Fibonacci Number
#Practice them in a row for better understanding 😉
################################################################################
# 2020-05-01 17:02:38
# 参考中文社区官方题解，修改了自己的”傻递归“的代码
# 主要区别在level的判断上，自己之前对level和整个递归过程的理解是有问题的，现在也不确定自己是不是
# 完全理解了。不理解就先记住吧....
class Solution:
    def climbStairs(self, n: int) -> int:
        array = []
        return climb_staris(0, n, array)

def climb_staris(level, _max, array):
    if level > _max: return 0
    if level == _max: return 1
    # process
    return climb_staris(level + 1, _max, array) + climb_staris(level + 2, _max, array)
    # drill down
    # reverse state
################################################################################
# 2020-05-01 14:35:29
# 再尝试一下递归，之后准备看题解和国际站的答案
# 因为家务耽误了，刚才递归还是没成功，代码放在这里之后，直接去看答案
class Solution:
    def climbStairs(self, n: int) -> int:
        array = []
        return climb_staris(0, n, array)

def climb_staris(level, _max, array):
    if level > _max:
        return 
    # process
    r = climb_staris(level - 1, _max, array) + climb_staris(level - 2, _max, array)
    # drill down
    # reverse state
    level = level + 1

if __name__ == "__main__":
    print(Solution().climbStairs(6))

################################################################################
# 2020-05-01 14:30:46
# 整理代码
#Accepted
#45/45 cases passed (36 ms)
#Your runtime beats 73.19 % of python3 submissions
#Your memory usage beats 20.59 % of python3 submissions (13.6 MB)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 2
        x, y, i = 1, 2, 3
        while i <= n:
            r = x + y
            x, y = y, r
            i += 1
        return r

if __name__ == "__main__":
    print(Solution().climbStairs(6))
################################################################################
# 2020-05-01 14:30:00
# Accepted
#45/45 cases passed (44 ms)
#Your runtime beats 36.01 % of python3 submissions
#Your memory usage beats 20.59 % of python3 submissions (13.7 MB)
# 利用三个变量的值传递，通过了
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 2
        x, y, i = 1, 2, 3
        while i <= n:
            r = x + y
            print("{}: {} = {} + {}".format(i, r, x, y))
            x = y
            y = r
            i += 1
            print("--i:{}, x:{}, y:{} r:{}---".format(i, x, y, r))
        return r

# @lc code=end

if __name__ == "__main__":
    print(Solution().climbStairs(6))

    #for i in range(0,5):
        #print("{}: {}".format(i, Solution().climbStairs(i)))
        #("{}: {}".format(i, Solution().climbStairs(i)))

# 2020-05-01 14:15:26
# 重新审题和思考
# 题目的关键在于 f(n) = f(n-1) + f(n-2)的结构，虽然是典型的递归形式，但是并不一定需要采用递归的方案。
# 核心的思路是：
# 基于前面的两步的结果计算现在的结果
# 实现方式
# 1. 递归
# 2. 数组、或者三个变量值就可以了
################################################################################
# 2020-05-01 14:07:24
# 自己有尝试先按照递归的处理模板框架来写，但是对模板的应用只是大概记住了步骤，没有完全背下来。
# 现在的处理思路是重新审题，重新思考一下。之前也没有把集中方法都尝试一下，所以这次要认真过一遍。
################################################################################
#2020-05-01 14:06:13
# 自己尝试独立写但是失败了，代码如下
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        print(climb_stairs(0, n))

def climb_stairs(level, n):
    if level > n:
        return ret
    # process
    # drill down
    ret = climb_stairs(level-1, n) + climb_stairs(level-2, n)
    # reverse state
    level = level + 1
    #return ret
################################################################################
# 2020-05-01 14:05:49 这是之前写的代码的部分，看起来应该是会报错的
# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0: return 0
        elif n == 1: return 1
        else:
            climb_stairs()
        
        def climb_stairs(level,n, array):
            if level > n:
                return 
            # process
            array[level] = climb_stairs(level-1,n,array) + climb_stairs(level-2,n,array)
            # drill down
            
            # reverse
        

# @lc code=end

#def recursion(level, param1, param2):
    # recursion terminator
#    if level > MAX_LEVEL:
#	   process_result
#	   return
    # process logic in current level
#    process(level, data...)
    # drill down
 #   self.recursion(level + 1, p1, ...)
    # reverse the current level status if needed

if __name__ == "__main__":
    #print(Solution().climbStairs(6))

    for i in range(0,10):
        print("{}: {}".format(i, Solution().climbStairs(i)))
        #("{}: {}".format(i, Solution().climbStairs(i)))
################################################################################