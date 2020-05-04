#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
# https://leetcode-cn.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (47.30%)
# Likes:    488
# Dislikes: 0
# Total Accepted:    141.9K
# Total Submissions: 299.2K
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
# 
# 
# 
# 说明:
# 
# 
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
# 
# 
# 
# 
# 示例:
# 
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# 输出: [1,2,2,3,5,6]
# 
#

################################################################################
# 2020-05-04 23:31:58 整理完的代码如下
# 这里另一种写法是取消p，数组的增加采用 list.append()的方案，就是答案中的方法2了
class Solution:
    #def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = p2 = p = 0
        nums1_copy = nums1[:m]
        while p1 < m and p2 < n:
            if nums1_copy[p1] <= nums2[p2]:
                nums1[p] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1
            p += 1
        if p2 < n: nums1[p:] = nums2[p2:]
        if p1 < m: nums1[p:] = nums1_copy[p1:]
################################################################################
# 2020-05-04 23:27:12 用答案2做了比对，问题出现在最初的列表拷贝上的问题
# 应该是 `nums1_copy = nums1[:m]` 而不是 `nums1[:]`问题就出在了这里...
# 另外自己的代码中由于用了方法2，其中的p也是没有必要的，而且如果用空数组的话，也会出现报错


################################################################################
# 2020-05-04 23:11:25 尝试自己写，有问题，折在了这个用例上
# Testcase
# [2,0]
# 1
# [1]
# 1
# Answer
# [1,2,0]
# Expected Answer
# [1,2]
# class Solution:
    #def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = p2 = p = 0
        nums1_copy = nums1[:]
        while p1 < m and p2 < n:
            if nums1_copy[p1] <= nums2[p2]:
                nums1[p] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1
            p += 1
        print(p1,p2,p)
        print(nums1)
        if p2 < n:
            nums1[p:] = nums2[p2:]
        if p1 < m:
            nums1[p:] = nums1_copy[p1:]
        print(nums1)


# @lc code=end

#Solution().merge([1,2,3,0,0,0],3,[2,5,6],3)
Solution().merge([2,0],1,[1],1)


# 2020-05-04 22:50:37 
# 刚才都看完了题解，现在尝试刷一下这题
################################################################################
# 官方解法第3种方案
# https://leetcode-cn.com/problems/merge-sorted-array/solution/he-bing-liang-ge-you-xu-shu-zu-by-leetcode/
# 这里的双指针是倒序处理的，注意最后的边界条件的处理，也就是说到最后如何解决nums2还有数据的情况
# 这种情况只要自己画一下应该就可以明白情况
# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, p= m - 1, n - 1, m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        nums1[:p2 + 1] = nums2[:p2 + 1]

#Accepted
#59/59 cases passed (44 ms)
#Your runtime beats 48.31 % of python3 submissions
#Your memory usage beats 6.9 % of python3 submissions (13.7 MB)
################################################################################
# 官方解法第2种方案
# https://leetcode-cn.com/problems/merge-sorted-array/solution/he-bing-liang-ge-you-xu-shu-zu-by-leetcode/
# 注意最后的if的判断条件为双指针最后的处理方案，一般是一个扫描结束了，另一个还没有结束的情况的描述
# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[:m]
        nums1[:] = []
        p1 = p2 = 0
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1
        if p1 < m:
            nums1[p1 + p2:] = nums1_copy[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]
################################################################################
# 官方解法第一种方案
# https://leetcode-cn.com/problems/merge-sorted-array/solution/he-bing-liang-ge-you-xu-shu-zu-by-leetcode/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # tips: 
        # [:]保证在原内存地址中存入数据
        # sorted vs list.sort()
        # sorted 返回一个新的列表但是不会在原列表做改动，list.sort()直接在原列表做排序
        # sorted 对可迭代的数据类型都可以排序，但是list.sort()只能对列表排序
        # https://stackoverflow.com/questions/22442378/what-is-the-difference-between-sortedlist-vs-list-sort
        nums1[:] = sorted(nums1[:m] + nums2)

# @lc code=end

#Accepted
#59/59 cases passed (32 ms)
#Your runtime beats 96.07 % of python3 submissions
#Your memory usage beats 6.9 % of python3 submissions (13.7 MB)

################################################################################
# 2020-05-04 19:54:15
# 题解提供了三个思路，这里回顾一下
# * 直接先merge再排序，自己竟然没有想到，o(╯□╰)o
# * 双指针方法，和我想到的for循环比起来，双指针更可用，所以对于一边遍历一边处理的时候，都可以考虑用指针来代替之前想到的循环遍历的方案。
# * 倒序的双指针，解决了第二种方法空间复杂度比较高的问题
# 这里有一点是双指针让程序循环起来可以用while来处理，另外还是要拷贝一份数据出来（法二）
# python中的语法糖[:]，把空数据写回原来的内存位置
################################################################################
# 2020-05-04 19:47:33 思路
# 暴力法：把nums2和nums1同时遍历，一旦出现合适的就插入
# 问题：不能在遍历的同时插入，会导致遍历出现错误
# 放弃：看题解