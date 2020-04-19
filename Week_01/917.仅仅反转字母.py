#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        #l = S.split()
        l = list(S)
        pace = []
        alpha = []
        tmp_num = 0
        for i in l:
            if i.isalpha():
                tmp_num += 1
                alpha.append(i)
                #print('right str:', i)
            else:
                pace.append(tmp_num)
                pace.append(i)
                tmp_num = 0
        pace.append(tmp_num)
        #print(l, pace, alpha)

        r = []
        for j in pace:
            if type(j) == type(1):
                while j:
                    #print("now j is {}, l is {}".format(j, l))
                    r.append(alpha.pop())
                    j -= 1
            else:
                r.append(j)
        #print(r)
        return ''.join(r)
                    




# 思路
# 字符串转为数组 -> 栈
# 字符串中遇到非字符记录符号和之前的数量 -> array
    # ascii ord()
# 基于栈和array重新组合
# @lc code=end

