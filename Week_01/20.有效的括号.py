#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#Category	Difficulty	Likes	Dislikes
#algorithms	Easy (41.36%)	1547	-
#Tags
#string | stack
#
#Companies
#airbnb | amazon | bloomberg | facebook | google | microsoft | twitter | zenefits
#
#给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
#有效字符串需满足：
#
#左括号必须用相同类型的右括号闭合。
#左括号必须以正确的顺序闭合。
#注意空字符串可被认为是有效字符串。
#
#示例 1:
#
#输入: "()"
#输出: true
#示例 2:
#
#输入: "()[]{}"
#输出: true
#示例 3:
#
#输入: "(]"
#输出: false
#示例 4:
#
#输入: "([)]"
#输出: false
#示例 5:
#
#输入: "{[]}"
#输出: true

# 要注意corner case的处理
################################################################################
# 整理后的代码如下
# 自己写的时候参考了下方的一个比较好理解的代码，但是发现了一个bug，对"]"的处理，要加异常捕获
    def isValid(self, s: str) -> bool:
        stack = ['?']
        _dict = {'(':')','[':']','{':'}'}
        for i in s:
            try:
                if i in _dict: stack.append(i)
                elif _dict[stack.pop()] != i: return False
            except:
                return False
        return len(stack) == 1
################################################################################
# 自己写的通过了
class Solution:
    def isValid(self, s: str) -> bool:
        stack = ['?']
        _dict = {'(':')','[':']','{':'}'}
        for i in s:
            if i in _dict:
                stack.append(i)
            elif i in _dict.values():
                try:
                    if _dict[stack.pop()] != i:
                        return False
                except:
                    return False
        return len(stack) == 1
################################################################################
# 核心逻辑
# * 遇到左括号压栈，遇到右括号谈栈比对（或者反过来）
# * 过程中一旦发现不对应的情况立刻结束
# * 最后对处理完的栈底做判断

# 具体实现的过程中每个人的写法都会有一些细微的区别
################################################################################
# 2020-05-02 11:00:28 国际站的解答也是一般
# https://leetcode.com/problems/valid-parentheses/discuss/9203/Simple-Python-solution-with-stack
class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
################################################################################
# 这个方法更清晰，更简洁
# 这里有问题，比如"]"的情况是无法通过的，需要增加try...except
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic: stack.append(c)
            elif dic[stack.pop()] != c: return False 
        return len(stack) == 1

#作者：jyd
#链接：https://leetcode-cn.com/problems/valid-parentheses/solution/valid-parentheses-fu-zhu-zhan-fa-by-jin407891080/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 这种方法不推荐，但是逻辑有趣，既然括号是有效的，一定有一个()或者[]或者{}存在，所以就不停的扫描
# 时间复杂度太高了
# Accepted
#76/76 cases passed (76 ms)
#Your runtime beats 5.19 % of python3 submissions
#Your memory usage beats 5.22 % of python3 submissions (13.7 MB)
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('[]','').replace('()','').replace('{}','')
        return True if s == '' else False
################################################################################
# 2020-05-02 10:43:49
# 废话太多，精简一下
# 官方题解写的还是蛮精妙的，但是不是顺着一下能理解的逻辑，感觉是写完之后整理成的这个状态。
def isValid(s):
    stack = []
    mapping = {")": "(","}": "{","]": "["}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack
# 2020-05-02 10:43:04 
# 官方题解
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack

#作者：LeetCode
#链接：https://leetcode-cn.com/problems/valid-parentheses/solution/you-xiao-de-gua-hao-by-leetcode/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
################################################################################
# 2020-05-02 10:35:11
# 做了10分钟，如上，答案不对，对栈的实现不熟悉，放弃，直接看题解吧
# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ['(', '{', '[']:
                stack.insert(0, i)
            elif i in [')']:
                if stack[0] == '(':
                    stack.pop(0)
                else:
                    return False
            elif i in ['}']:
                if stack[0] == '}':
                    stack.pop(0)
                else:
                    return False
            elif i in [']']:
                if stack[0] == ']':
                    stack.pop(0)
                else:
                    return False
        return True
# @lc code=end

s = "()"
s = "([])"
print(Solution().isValid(s))

################################################################################
# 2020-05-02 10:24:56 思路
# 利用栈
# 左括号压入，右括号对应的左括号弹出
# 栈一般用列表实现即可