#
# @lc app=leetcode.cn id=299 lang=python3
#
# [299] 猜数字游戏
#
#Category	Difficulty	Likes	Dislikes
#algorithms	Easy (47.45%)	65	-
#Tags
#hash-table
#
#Companies
#Unknown
#
#你正在和你的朋友玩 猜数字（Bulls and Cows）游戏：你写下一个数字让你的朋友猜。每次他猜测后，你给他一个提示，告诉他有多少位数字和确切位置都猜对了（称为“Bulls”, 公牛），有多少位数字猜对了但是位置不对（称为“Cows”, 奶牛）。你的朋友将会根据提示继续猜，直到猜出秘密数字。
#
#请写出一个根据秘密数字和朋友的猜测数返回提示的函数，用 A 表示公牛，用 B 表示奶牛。
#
#请注意秘密数字和朋友的猜测数都可能含有重复数字。
#
#示例 1:
#
#输入: secret = "1807", guess = "7810"
#
#输出: "1A3B"
#
#解释: 1 公牛和 3 奶牛。公牛是 8，奶牛是 0, 1 和 7。
#示例 2:
#
#输入: secret = "1123", guess = "0111"
#
#输出: "1A1B"
#
#解释: 朋友猜测数中的第一个 1 是公牛，第二个或第三个 1 可被视为奶牛。
#说明: 你可以假设秘密数字和朋友的猜测数都只包含数字，并且它们的长度永远相等。
#
#Discussion | Solution
################################################################################

# 2020-04-20 13:59:22 第一遍思路
# 分成两个部分，第一步先找到相同位置的数据对不对，第二步去掉完全正确的数据，看剩下的数据有没有相同的(set())，有的话就是要的答案
# 扩展在思考用哪一种数据结构来处理，还没想好

# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a = 0
        tmp = []
        for flag, i in enumerate(secret):
            print(flag, i, guess[flag])
            if i == guess[flag]:
                a += 1
                tmp.append(i)    
        print(a, tmp)
        for j in tmp:
            #secret = secret.replace(j, "")
            #guess = guess.replace(j, "")
            # 删除对应位置的字符
            pass
        print(secret, guess)
        iset = set(secret).intersection(set(guess))
        print(len(iset))
        print(str(a) + "A" + str(len(iset)) + "B")
        return str(a) + "A" + str(len(iset)) + "B"
            # @lc code=end

#Solution().getHint("1807", "7810")
#Solution().getHint("2314", "5555")
#Solution().getHint("1123", "0111")
        
# @lc code=end

################################################################################
#Accepted
#152/152 cases passed (64 ms)
#Your runtime beats 37.72 % of python3 submissions
#Your memory usage beats 12.5 % of python3 submissions (13.8 MB)
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a = 0
        tmp = []
        s = [0] * 10
        g = [0] * 10
        for flag, i in enumerate(secret):
            #print(flag, i, guess[flag])
            if i == guess[flag]:
                a += 1
            else:
                s[int(i)] += 1
                g[int(guess[flag])] += 1
        print(a, tmp, s, g)
        #r = [x + y for x, y in zip(s, g)]
        #print(r)
        rr = 0
        for j in range(10):
            if s[j] != 0 and g[j] != 0:
                rr += min(s[j], g[j])
        print(str(a) + "A" + str(rr) + "B")
        return str(a) + "A" + str(rr) + "B"
            # @lc code=end

