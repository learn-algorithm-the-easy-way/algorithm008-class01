#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# TODO
# 看国际站的代码
# 自己写数组到链表的序列化和反序列化的代码
# 自己写链表的实现和基本操作的代码
################################################################################
# 整理和优化代码
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ret = end = ListNode(None)
        # 开始合并链表，以某一个链表为单位做循环
        while l1 and l2:
            if l1.val <= l2.val: end.next, l1 = l1, l1.next
            else: end.next, l2 = l2, l2.next
            end = end.next
        end.next = l1 if l1 else l2
        return ret.next
################################################################################
# 2020-05-02 16:08:46
# 解决问题

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ret = end = ListNode(None)
        # 开始合并链表，以某一个链表为单位做循环
        while l1 and l2:
            if l1.val <= l2.val:
                end.next = l1
                l1 = l1.next
            else:
                end.next = l2
                l2 = l2.next
            end = end.next
        if l1:
            end.next = l1
        else:
            end.next = l2
        return ret.next
################################################################################
# 2020-05-02 12:47:18
# 找到了问题: 我的循环判断的是l1.next是否为空，也就是说我会找到的是l1的结束节点的前一个节点，l1还剩下一个节点需要去处理，这个方法不是不能做，
# 会麻烦一些。所以一般循环都是基于while l1 and l2 或者 l1 or l2 的方式来处理，保证其中的一个遍历到头

# https://leetcode-cn.com/problems/merge-two-sorted-lists/solution/xin-shou-you-hao-xue-hui-tao-lu-bu-fan-cuo-4nian-l/
# 上面的链接给的思路比较通用和普遍，也比较容易理解
# 精简版本
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    ret = move = ListNode(0)
    while l1 and l2:
        if l1.val <= l2.val:
            move.next = l1
            l1 = l1.next
        else:
            move.next = l2
            l2 = l2.next
        move = move.next
    move.next = l1 if l1 else l2
    return ret.next
# 废话较多的原版
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 创建哑节点作为 结果链表 的开头
        dummy = ListNode(0)
        # 有个游标，标识 结果链表 的结尾
        move = dummy
        # l1 和 l2 都未遍历结束
        while l1 and l2:
            # 如果 l1 的数值比较小
            if l1.val <= l2.val:
                # 把 l1 头部节点拼接到 结果链表 的结尾
                move.next = l1
                # l1 指向下一个节点
                l1 = l1.next
            else:
                # 把 l2 头部节点拼接到 结果链表 的结尾
                move.next = l2
                # l2 指向下一个节点
                l2 = l2.next
            # 移动 结果链表 的结尾指针
            move = move.next
        # l1 或者 l2 尚未使用完，拼接到 结果链表 的最后
        move.next = l1 if l1 else l2
        # 返回哑节点的下一个位置
        return dummy.next

#作者：fuxuemingzhu
#链接：https://leetcode-cn.com/problems/merge-two-sorted-lists/solution/xin-shou-you-hao-xue-hui-tao-lu-bu-fan-cuo-4nian-l/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
################################################################################
# 2020-05-02 12:29:57
#https://leetcode-cn.com/problems/merge-two-sorted-lists/solution/yi-kan-jiu-hui-yi-xie-jiu-fei-xiang-jie-di-gui-by-/
# 上面是另一个递归的方案，看起来更清晰，还提供了其他类似的递归的题目，在后面看递归的时候可以用一下
# TODO 递归的方案理解和自己写

# 这里利用了递归，效率一般
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val: l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2
#作者：QQqun902025048
#链接：https://leetcode-cn.com/problems/merge-two-sorted-lists/solution/python-4xing-by-knifezhu-3/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
#Accepted
#208/208 cases passed (48 ms)
#Your runtime beats 47.48 % of python3 submissions
#Your memory usage beats 7.14 % of python3 submissions (13.4 MB)
################################################################################
# 2020年05月02日12:07:51
# 时间到了，没完全做出来，放弃
# 好的地方：哨兵用上了、链表的连接用上了
# 不好的地方：自己判断主要问题在最后的结尾部分的处理，另外是循环条件的判断上出现了问题
# 理论上来说，把结尾处理好了，这题应该能过的
# 所以这一编还得算第一遍没结束

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 哨兵
        ret = end = ListNode(None)
        # 开始合并链表，以某一个链表为单位做循环
        while l1.next:
            if l2.next == None:
                end.next = l1
            if l1.val > l2.val:
                end.next = l2
                l2 = l2.next
                end = end.next
            else:
                end.next = l1
                l1 = l1.next
                end = end.next
        return ret.next
            
        
        # 循环结束如果l2还有，则续上l2后续的所有内容


# @lc code=end

################################################################################
# 2020-05-02 11:44:06
# 思路：
# 典型的链表问题，需要多个指针
# 一个是哨兵指针，也可以建立空节点，最后直接返回这个节点
# 另外是两个指针，一个指针用于寻找下一个阶段，另一个指针用于把新的节点合并到链表后指向链表的尾部
################################################################################
# 这是五一之前做的
# @lc code=start
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = prev = ListNode(-1)
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        
        if l1 is not None:
            prev.next = l1
        else:
            prev.next = l2
        return head.next
# @lc code=end

