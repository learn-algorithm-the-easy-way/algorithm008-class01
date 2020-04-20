#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#Category	Difficulty	Likes	Dislikes
#algorithms	Easy (59.39%)	183	-
#Tags
#hash-table | sort
#
#Companies
#amazon | uber | yelp
#
#给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
#示例 1:
#
#输入: s = "anagram", t = "nagaram"
#输出: true
#示例 2:
#
#输入: s = "rat", t = "car"
#输出: false
#说明:
#你可以假设字符串只包含小写字母。
#
#进阶:
#如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

################################################################################
#2020-04-20 18:37:12 第一遍思路
#构造两个字典，key为字母，value为出现的个数，如果相同则是异味词

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return dict_init(s) == dict_init(t)
        

def dict_init(s: str):
    """
    构造字典用
    """
    r = {}
    for i in s:
        try:
            r[i] += 1
        except:
            r[i] = 0
    return r

#dict_init("aba")
# @lc code=end

################################################################################
# 其他思路
# 来自老师的视频
# 1. 暴力， sort， sotred_str 相等？ O(NlogN)
# 2. hash table
