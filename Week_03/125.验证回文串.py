#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#
#验证回文串
#Category	Difficulty	Likes	Dislikes
#algorithms	Easy (43.26%)	179	-
#Tags
#two-pointers | string
#
#Companies
#facebook | microsoft | uber | zenefits
#
#给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
#说明：本题中，我们将空字符串定义为有效的回文串。
#
#示例 1:
#
#输入: "A man, a plan, a canal: Panama"
#输出: true
#示例 2:
#
#输入: "race a car"
#输出: false



################################################################################
# TODO 双指针要继续练习
# 其中的一些基础的函数和filter等的用法的研究和使用
################################################################################
#2020-05-01 18:53:55
# 基于刚才题解的内容，再修改一下之前的代码
# 顺便测试一下运行时间的情况
# 没想到自己写的正则看起来到目前是最快的... ''.join的方法非常慢

class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        clean_str = re.sub(r'[^a-zA-Z0-9]+', '', s).lower()
        return clean_str == clean_str[::-1]
#Accepted
#476/476 cases passed (52 ms)
#Your runtime beats 76.68 % of python3 submissions
#Your memory usage beats 7.41 % of python3 submissions (15.3 MB)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = ''.join(i.lower() for i in s if i.isalnum())
        return clean_str == clean_str[::-1]
#Accepted
#476/476 cases passed (76 ms)
#Your runtime beats 29.77 % of python3 submissions
#Your memory usage beats 7.41 % of python3 submissions (19.2 MB)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = [*filter(str.isalnum, s.lower())]
        return clean_str == clean_str[::-1]
#Accepted
#476/476 cases passed (44 ms)
#Your runtime beats 92.04 % of python3 submissions
#Your memory usage beats 7.41 % of python3 submissions (15.1 MB)

################################################################################
#2020-05-01 18:52:26
#Accepted
#476/476 cases passed (56 ms)
#Your runtime beats 67.37 % of python3 submissions
#Your memory usage beats 55.56 % of python3 submissions (13.8 MB)
# 虽然没有另一个方法快，但是双指针的使用训练到了
# 注意避免死循环，最后要加上l、r的变换条件

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1; r -= 1
        return True
################################################################################
# 看题解的双指针的用法
# 发现自己之前写的时候出现的问题
# 两个指针夹逼到中间即可，不用全部走到头
# 让指针跑起来用while即可，这样逻辑会清晰很多，我用if-else的时候会限制每一次指针判断的步数，会出问题，这里的场景和之前的计算面积的双指针的场景不太一样。
def isPalindrome(self, s):
    l, r = 0, len(s)-1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l <r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l +=1; r -= 1
    return True
# https://leetcode.com/problems/valid-palindrome/discuss/39982/Python-in-place-two-pointer-solution
################################################################################
# 看题解下面两种都是和我的法一类似的解法，但是更简练
# * isalnum() 直接判断是否是字母和数字, 我用了正则，也可以不用正则，自己手工判断
# * 构造新的字符串时的套路不同
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [*filter(str.isalnum, s.lower())]
        return s == s[::-1]

# 首先利用isalnum函数排除非字母数字，lower/tolower将所有字母转为小写 然后镜像对比处理后的字符串
#作者：QQqun902025048
#链接：https://leetcode-cn.com/problems/valid-palindrome/solution/c-5xing-on-by-qqqun902025048-2/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def isPalindrome(self, s):
        s = ''.join(e for e in s if e.isalnum()).lower()
        return s==s[::-1]
# https://leetcode.com/problems/valid-palindrome/discuss/39982/Python-in-place-two-pointer-solution
################################################################################
# 2020-05-01 18:24:13
# 尝试双指针方法时出错，被指针的判断绕晕了
# 放弃，看题解吧...
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        ret = []
        while r >= 0:
            print("l: {}, r: {}".format(s[l], s[r]))
            if  alhpa_or_number(s[l]) and alhpa_or_number(s[r]):
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                    ret.append(True)
                else:
                    return False
            if not alhpa_or_number(s[l]):
                    l += 1
            if not alhpa_or_number(s[r]):
                    r -= 1
            print('**********')

def alhpa_or_number(s):
    #print("{}: {}".format(s, (s.isalpha() and s.isnumeric())))
    return s.isalpha() or s.isnumeric()
################################################################################
# 2020-05-01 17:53:16
# 尝试再整理一下代码看看效果, 有点意外，一个是速度进一步提升，另一个是空间上没有变化
#Accepted
#476/476 cases passed (40 ms)
#Your runtime beats 96.15 % of python3 submissions
#Your memory usage beats 7.41 % of python3 submissions (15.2 MB)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        clean_str = re.sub(r'[^a-zA-Z0-9]+', '', s).lower()
        reverse_str = clean_str[::-1]
        return reverse_str == clean_str
################################################################################
# @lc code=start
#Accepted
#476/476 cases passed (52 ms)
#Your runtime beats 76.68 % of python3 submissions
#Your memory usage beats 7.41 % of python3 submissions (15.2 MB)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = remove_illagle_chars(s)
        reverse_str = clean_str[::-1]
        return reverse_str == clean_str

def remove_illagle_chars(s):
    import re
    return re.sub(r'[^a-zA-Z0-9]+', '', s).lower()

# @lc code=end

if __name__ == "__main__":
    _str_list = ["aaa", "A man, a plan, a canal: Panama", "race a car"]
    for _str in _str_list:
        print(Solution().isPalindrome(_str))
        #print(remove_illagle_chars(_str))


#2020-05-01 17:39:35
# 尝试自顶向下的编程方法，参考老师的方案，先写主题逻辑，之后编辑对应的函数即可
# 的确思路清晰很多
# 在删除非字母和数字的字符串方面参考了Stack Overflow的答案
# 在转置方面参考了Stack Overflow的答案
################################################################################
# 2020-05-01 17:33:33
# 审题 & 把测试用例准备好
# 方法一：
# * 去掉空格等各种字符
# * 反转字符串
# * 相等则ok
# 方法二：
# * 两个指针从两边开始遍历
################################################################################
