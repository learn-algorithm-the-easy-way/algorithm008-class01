#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#Category	Difficulty	Likes	Dislikes
#algorithms	Easy (48.12%)	8037	-
#Tags
#array | hash-table
#
#Companies
#adobe | airbnb | amazon | apple | bloomberg | dropbox | facebook | linkedin | microsoft | uber | yahoo | yelp
#
#给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
#你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
#
#示例:
#
#给定 nums = [2, 7, 11, 15], target = 9
#
#因为 nums[0] + nums[1] = 2 + 7 = 9
#所以返回 [0, 1]

################################################################################
# 收藏部分代码
class Solution:
    # @return a tuple, (index1, index2)
    # 8:42
    def twoSum(self, num, target):
        map = {}
        for i in range(len(num)):
            if num[i] not in map:
                map[target - num[i]] = i + 1
            else:
                return map[num[i]], i + 1

        return -1, -1
# https://leetcode.com/problems/two-sum/discuss/2/Python-solution-using-hash

def twoSum(nums, target):
    hashmap={}
    for i,num in enumerate(nums):
        if hashmap.get(target - num) is not None:
            return [i,hashmap.get(target - num)]
        hashmap[num] = i #这句不能放在if语句之前，解决list中有重复值或target-num=num的情况
# 上面的 if 行可以改为: if target - num in hashmap::w

def twoSum(nums, target):
    hashmap={}
    for ind,num in enumerate(nums):
        hashmap[num] = ind
    for i,num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i!=j:
            return [i,j]

#作者：lao-la-rou-yue-jiao-yue-xiang
#链接：https://leetcode-cn.com/problems/two-sum/solution/xiao-bai-pythonji-chong-jie-fa-by-lao-la-rou-yue-j/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

################################################################################
# 2020-05-01 22:25:59 再次整理代码如下
class Solution:
    #def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target: int):
        nums_dict= {}
        for i in range(len(nums)):
            nums_dict[nums[i]] = i
        for flag,i in enumerate(nums):
            if target - i in nums_dict and flag != nums_dict[target-i]:
                    return [flag, nums_dict[target-i]]
################################################################################
#https://leetcode-cn.com/problems/two-sum/solution/xiao-bai-pythonji-chong-jie-fa-by-lao-la-rou-yue-j/
# 基于题解方法三，修改自己之前的代码
# 自己错误的关键在于最后寻找答案时，没有充分利用列表遍历的信息，因为可能出现一种情况：
# 两个相同的数字，在字典构造时仅保留后一个位置，所以前面的一个位置就需要列表中的元素遍历时获取，因为这个位置在字典中是无法获取的
# 自己之前的代码没有考虑这种情况，不过我也是怀疑其实解法的作者也不是为了解决这个问题专门做的开发，也是写着写着写顺了就解决了
class Solution:
    #def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target: int):
        nums_dict = init_nums_dict(nums)
        for flag,i in enumerate(nums):
            if target - i in nums_dict:
                if flag != nums_dict[target-i]:
                    return [flag, nums_dict[target-i]]

def init_nums_dict(_list):
    _dict = {}
    for i in range(len(_list)):
        _dict[_list[i]] = i
    print(_dict)
    return _dict

#Accepted
#29/29 cases passed (64 ms)
#Your runtime beats 56.61 % of python3 submissions
#Your memory usage beats 5.48 % of python3 submissions (15.6 MB)
################################################################################
# 2020-05-01 21:47:29 发现问题，没有考虑如果一个值相等的情况 即 3+3==6 的情况
#2020-05-01 21:35:36
# 思路1：哈希
# 基于数组构造字典，利用字典值获取到对应的下标
class Solution:
    #def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target: int):
        nums_dict = init_nums_dict(nums)
        for i in nums:
            if target - i in nums_dict:
                return [nums_dict[i], nums_dict[target-i]]

def init_nums_dict(_list):
    _dict = {}
    for i in range(len(_list)):
        _dict[_list[i]] = i
    return _dict

if __name__ == "__main__":
    #print(Solution().twoSum(nums = [2, 7, 11, 15], target = 9))
    print(Solution().twoSum(nums = [3, 2, 4], target = 6))

# 即使把[3,2,4]解决了，[3,3]没解决，放弃...
class Solution:
    #def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target: int):
        nums_dict = init_nums_dict(nums)
        for i in nums:
            if target - i == i:
                pass
            elif target - i in nums_dict:
                return [nums_dict[i], nums_dict[target-i]]

def init_nums_dict(_list):
    _dict = {}
    for i in range(len(_list)):
        _dict[_list[i]] = i
    return _dict
################################################################################
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for flag, i in enumerate(nums):
            for fj, j in enumerate(nums[(flag+1):]):
                if i + j == target:
                    return [flag, flag+fj+1]
                
# 自我点评：暴力法求解

