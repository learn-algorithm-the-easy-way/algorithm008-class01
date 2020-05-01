#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start



################################################################################
# TODO 研究一下下面的代码里涉及到生成器或者迭代器的内容、继续尝试看看哪个复杂度低，时间短等
################################################################################
# 2020-05-01 21:03:25
# 知识点
# nums[:] 与 nums 的区别
# nums[:] = blabla vs nums = blabla
# 前者是向nums指向的地址填写数据，nums指向的内存地址不变，后者是改变了nums的指向的地址并且之前的内存地址会被回收
# 所以原来的"nums = nums + [0] * zero" 就不生效了，改成"nums[:] = nums + [0] * zero" 才可以
# https://stackoverflow.com/questions/32448414/what-does-colon-at-assignment-for-list-do-in-python
# https://stackoverflow.com/questions/10623302/how-assignment-works-with-python-list-slice
class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        while 0 in nums:
            zero += 1
            nums.remove(0)
        nums[:] = nums + [0] * zero
        #print(nums)
################################################################################
# 2020-05-01 20:52:16
# 看题解，收藏代码
# https://leetcode.com/problems/move-zeroes/discuss/72012/Python-short-in-place-solution-with-comments
def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    count=nums.count(0)
    nums[:]=[i for i in nums if i != 0]
    nums+=[0]*count

def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    for j in range(nums.count(0)):
        nums.remove(0)
        nums.append(0)

#https://leetcode-cn.com/problems/move-zeroes/solution/python-1-xing-onlogn-5-xing-on-by-knifezhu/
# 国内也有一些有趣的解法, 时间复杂度不一定低，可以参考一下语法的用法
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(key=bool, reverse=True)

#作者：QQqun902025048
#链接：https://leetcode-cn.com/problems/move-zeroes/solution/python-1-xing-onlogn-5-xing-on-by-knifezhu/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

#sort 时间复杂度为O(NlogN), 直接遍历可以达到 O(N)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for i, n in enumerate(filter(lambda x: x, nums)):
            nums[i] = n
        for i in range(i + 1, len(nums)):
            nums[i] = 0

#直接使用 filter 迭代器可以避免交换操作，思路更简单

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def gen(nums):
            for x in nums:
                if x:
                    yield x
        
        i = 0
        for i, n in enumerate(gen(nums)):
            nums[i] = n
        for i in range(i + 1, len(nums)):
            nums[i] = 0

#    手动实现filter
#作者：QQqun902025048
#链接：https://leetcode-cn.com/problems/move-zeroes/solution/python-1-xing-onlogn-5-xing-on-by-knifezhu/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

################################################################################
# 尝试写双指针的解法
# 之前对双指针的理解不是很到位，其实这里的双指针有一个指针就是在最前面扫的指针，也就是0的开始指针，我最开始的想法是类似于“三指针”，实际上是没必要的。
# 奇怪的事情是我的解法和题解的几乎一摸一样，但是第一遍跑的时间差距有点大...不知道为什么

#Accepted
#21/21 cases passed (52 ms)
#Your runtime beats 56.32 % of python3 submissions
#Your memory usage beats 7.41 % of python3 submissions (14.3 MB)
#
#Accepted
#21/21 cases passed (36 ms)
#Your runtime beats 95.13 % of python3 submissions
#Your memory usage beats 7.41 % of python3 submissions (14.4 MB)

class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
################################################################################
# 参考了vscode插件里提供的python3的最高vote答案，一开始没理解这是双指针，自己写之后才明白过来
# in-place
def moveZeroes(self, nums):
    zero = 0  # records the position of "0"
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1
#Accepted
#21/21 cases passed (36 ms)
#Your runtime beats 95.13 % of python3 submissions
#Your memory usage beats 7.41 % of python3 submissions (14.3 MB)
################################################################################
# 再次尝试，结果print的是对的，但是test总是出问题，原因不详
class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        while 0 in nums:
            zero += 1
            nums.remove(0)
        nums = nums + [0] * zero
        print(nums)
################################################################################
# 想尝试python的trick的方法未成功，在扫描列表的同时直接pop导致列表越界
class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        for i in range(len(nums) - 1):
            print(i)
            if nums[i] == 0:
                nums.pop(i)
                zero += 1
        nums + [0] * zero

# @lc code=end


#print("Origin:", [0,1,0,3,12])
#Solution().moveZeroes([0,1,0,3,12])