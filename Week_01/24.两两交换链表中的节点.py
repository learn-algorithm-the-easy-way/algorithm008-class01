#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (65.11%)
# Likes:    482
# Dislikes: 0
# Total Accepted:    98.2K
# Total Submissions: 150.3K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 
# 
# 
# 示例:
# 
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


################################################################################
#https://leetcode-cn.com/problems/swap-nodes-in-pairs/solution/bi-jiao-zhi-jie-gao-xiao-de-zuo-fa-han-tu-jie-by-w/?utm_source=LCUS&utm_medium=ip_redirect_q_uns&utm_campaign=transfer2china
# 画图是个好办法，参考上面的图，简洁明了

################################################################################
# 把return 上面的那句 p = l.next 改为 p = l 即可，因为转换了之后，游标的位置要调整，游标的位置搞错了
# 但是这个方法有点慢...

#Accepted
#55/55 cases passed (48 ms)
#Your runtime beats 27.7 % of python3 submissions
#Your memory usage beats 6.25 % of python3 submissions (13.6 MB)

# 跑了一下参考代码，还挺快的...代码结构和逻辑几乎是一模一样的...不知道为啥...
#Accepted
#55/55 cases passed (36 ms)
#Your runtime beats 79.38 % of python3 submissions
#Your memory usage beats 6.25 % of python3 submissions (13.4 MB)
################################################################################
# 2020-05-02 17:39:19
# 运转的结果有误，两两切换后哨兵的位置弄错了，间隔了一个元素
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 设置哨兵
        pre = ListNode(0)
        pre.next = head
        # 设置游标指向第一个节点
        p = pre
        # 游标和next指向的是即将变换的节点
        while p.next and p.next.next:
            l, r = p.next, p.next.next
            l.next = r.next
            r.next = l
            p.next = r
            p = l.next
        return pre.next
################################################################################
# 2020-05-02 17:30:35 
# 错误的内容，但是整体结构是对的，还是对步骤不清晰，刚才参考了下面的链接，画了自己的图之后理解了问题在哪里
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/solution/bi-jiao-zhi-jie-gao-xiao-de-zuo-fa-han-tu-jie-by-w/
# 问题在游标的设置上出了问题，游标应该体现的是哨兵节点指向第一个节点，如果直接设置为第一个节点，就没办法指回来了

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 设置哨兵
        pre = ListNode(0)
        pre.next = head
        # 设置游标指向第一个节点
        p = pre.next
        # 游标和next指向的是即将变换的节点
        while p and p.next:
            l, r = p, p.next
            l.next = r.next
            r.next = l
            p.next = r
            p = l.next
        return pre.next
################################################################################
# 2020-05-02 16:46:52
# 看题解
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/solution/hua-jie-suan-fa-24-liang-liang-jiao-huan-lian-biao/
# 虽然是java的内容，但是原理想通，两种解法，递归和非递归

# https://leetcode-cn.com/problems/swap-nodes-in-pairs/solution/bi-jiao-zhi-jie-gao-xiao-de-zuo-fa-han-tu-jie-by-w/
# python 的解法，可以自己先写while的循环吧
################################################################################
# 自己写，失败了，我对单个链表转换那部分还比较自信，我觉得我是对的，但是对递归这块应该是出错了
# 整体的哨兵节点和在某一个具体环节的哨兵节点的应用是不是不太一样呢？
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
       return swap_pairs(head) 

def swap_pairs(first):
    guard = ListNode(0)
    guard.next = first
    # if
    if not first:
        return guard.next
    # process
    s = first.next
    t = first.next.next
    first.next = t
    s.next = first
    guard.next = s
    # drill down
    swap_pairs(t)
    # reverse state

