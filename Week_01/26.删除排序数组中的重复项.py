#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

################################################################################
# 总算理解题解了 2020-05-02 00:46:44
# 太困太累，经历跟不上了，明天继续
class Solution:
    #def removeDuplicates(self, nums: List[int]) -> int:
    def removeDuplicates(self, nums):
        x = 1
        for i in range(len(nums)-1):
            if(nums[i]!=nums[i+1]):
                nums[x] = nums[i+1]
                x+=1
        return(x)
################################################################################
# 尝试暴力法？
# 直接新建，也不行，因为要在原列表的内存地址的位置
class Solution:
    #def removeDuplicates(self, nums: List[int]) -> int:
    def removeDuplicates(self, nums):
        new = []
        for i in range(len(nums)):
            if nums[i] not in new:
                new.append(nums[i])
        return len(new)
################################################################################
# 不能在列表一边处理一边remove或者pop，会出问题的，下面就是
class Solution:
    #def removeDuplicates(self, nums: List[int]) -> int:
    def removeDuplicates(self, nums):
        _dict = {}
        for flag, i in enumerate(nums):
            _dict[i] = False
        print(_dict)
        for j in nums:
            if _dict[j] == False:
                _dict[j] = True
            else:
                _list.remove(j)
            print(nums)
        #print(nums)
        print(_dict)
        return(nums)
################################################################################
# 采用自带的方法来处理，显然这不是题目想要的，先完成之
#Accepted
#161/161 cases passed (48 ms)
#Your runtime beats 83.91 % of python3 submissions
#Your memory usage beats 8.16 % of python3 submissions (15.1 MB)
# @lc code=start
class Solution:
    #def removeDuplicates(self, nums: List[int]) -> int:
    def removeDuplicates(self, nums):
        nums[:] = list(set(nums))
        nums.sort()
        return len(nums)
# @lc code=end

if __name__ == "__main__":
    _list = [0,0,1,1,1,2,2,3,3,4]
    print(Solution().removeDuplicates(_list))