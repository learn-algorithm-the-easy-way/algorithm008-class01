#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
括号生成
Category	Difficulty	Likes	Dislikes
algorithms	Medium (75.23%)	985	-
Tags
string | backtracking

Companies
google | uber | zenefits

数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例：

输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]
Discussion | Solution

# @lc code=start
class Solution:
    #def generateParenthesis(self, n: int) -> List[str]:
    def generateParenthesis(self, n: int):
        _generate(0, 2*n, "")
        return
            
# @lc code=end

# 递归模板
#def recursion(level, param1, param2):
#   # recursion terminator
#    if level > MAX_LEVEL:
#	   process_result
#	   return
#   # process logic in current level
#    process(level, data...)
#   # drill down
#   self.recursion(level + 1, p1, ...)
#   # reverse the current level status if needed

# 先尝试傻递归，把结果输出
##############################################################
# 2020-04-29 15:59:16 看着老师的视频，跟着做了一遍，先把全部的结果输出出来
# 对于左右括号的检查，视频也看了，没有直接改，想自己试一下
def _generate(level, MAX, s):
        # terminator
        if level >= MAX:
            print(s)
            return 

        # process current logic: left, right
        s1 = s + "("
        s2 = s + ")"
        # drill down
        _generate(level + 1, MAX, s1)
        _generate(level + 1, MAX, s2)
        # reverse state

if __name__ == "__main__":
    Solution().generateParenthesis(3)
##############################################################
# 2020-04-29 16:11:55 自己试一下
# 先写所有括号的输出
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        _generate(0, 2*n, '')

def _generate(level, MAX, s):
    if level >= MAX:
        print(s)
        return
    
    # process
    s1 = s + ')' 
    s2 = s + '('

    # drill down
    _generate(level+1, MAX, s1)
    _generate(level+1, MAX, s2)
    # reverse state

# 改写代码
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        _generate(0,0, n, '')

def _generate(left, right, n, s):
    if left == n and right == n:
        print(s)
        return
    
    # process
    s1 = s + '(' 
    s2 = s + ')'

    # drill down
    if left < n:
        _generate(left + 1, right, n, s1)
    if right < left:
        _generate(left, right + 1, n, s2)

    # reverse state

# 增加相关的处理
class Solution:
    def generateParenthesis(self, n: int) -> List[str]: 
        r = []
        a = _generate(0,0, n, '',r)
        
        return a


def _generate(left, right, n, s,r):
    
    if left == n and right == n:
        print("s:", s)
        r.append(s)
        print("r:", r)
        return r
    
    # process
    s1 = s + '(' 
    s2 = s + ')'

    # drill down
    if left < n:
        _generate(left + 1, right, n, s1,r)
    if right < left:
        _generate(left, right + 1, n, s2,r)

    # reverse state

输入
2
输出
null
预期结果
["(())","()()"]
stdout
s: (())
r: ['(())']
s: ()()
r: ['(())', '()()']

# 2020-04-29 16:34:57 奇怪的问题，为啥最后的结果r没有返回呢？
class Solution:
    def generateParenthesis(self, n: int) -> List[str]: 
        ret = []
        return _generate(0,0, n, '', ret)

def _generate(left, right, n, s,r):

    if left == n and right == n:
        print("s:", s)
        r.append(s)
        print("r:", r)
        return r

    # process
    s1 = s + '(' 
    s2 = s + ')'

    # drill down
    if left < n:
        _generate(left + 1, right, n, s1,r)
    if right < left:
        _generate(left, right + 1, n, s2,r)
    return r
    # reverse state

Accepted
8/8 cases passed (40 ms)
Your runtime beats 76.61 % of python3 submissions
Your memory usage beats 6.06 % of python3 submissions (13.8 MB)

最后要加一个return r