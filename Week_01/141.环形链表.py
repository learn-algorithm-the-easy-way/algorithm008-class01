#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# TODO: 回做，之前做的少
################################################################################
# 2020-05-01 19:22:28
# 看基于哈希的方法，国际站上都是快慢指针，因为题目要求空间复杂度为O(1)
# 看国内站的Java答案，尝试改写为Python的
# 关键是对哈希的应用，在python中不仅仅有字典，还有集合，这里用集合是合适的，平时集合用的很少，这里用上了
# 空间复杂度高了一些，但是这个方法学到了
#Accepted
#17/17 cases passed (60 ms)
#Your runtime beats 64.86 % of python3 submissions
#Your memory usage beats 9.52 % of python3 submissions (17.2 MB)

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        link_dict = set()
        while head != None:
            if head in link_dict:
                return True
            else:
                link_dict.add(head)
            head = head.next
        return False
################################################################################
# 2020-05-01 19:18:10 放弃挣扎，直接看题解，原因有二：
# * 这种循环链表的判断是一种模式，学会模式更重要
# * 自己对链表部分还不够熟悉
# 以下是光头哥的答案，用到了快慢指针，并且使用了try...except的方案
# 因为如果不是循环链表，一定会到尾部，到达尾部时fast.next就会报错，那就一定是错误的了
# 然后判断在没有到头的情况下主要去判断是否相等，如果相等了，说明是循环的
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
        
        
# @lc code=end

