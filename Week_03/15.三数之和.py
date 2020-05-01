#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
################################################################################
#2020-05-01 23:49:04
# 找到原因了，一方面三数之和的情况下利用双指针天生就是不够的，而我的判断条件又太粗了。
# 需要三个指针，利用三指针有多种方法可以做
# * 固定一个数的位置，另外两个数做双指针遍历
# * 直接开启三指针的模式，两个指针从两头开始向中间逼近，这时候对中间指针的位置，三个指针的计算的情况分析比较复杂，要求相对较高
# * a + b = -c 的模式下，基于哈希辅助，尝试降低复杂度
# * 其他类似的解法
# * 暴力解法是固定三个指针的循环，应该在O三方左右的复杂度
# 目前看起来复杂度都在O(n平方)，的确是情况更复杂，所以比两数之和要考虑的更多
################################################################################
# 2020-05-01 23:31:19
# 尝试双指针的方案，但是总是漏掉一些情况，放弃，直接看题解
# @lc code=start
class Solution:
    #def threeSum(self, nums: List[int]) -> List[List[int]]:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        elif set(nums) == set([0]):
            return [[0,0,0]]
        nums.sort()
        l, r, ret = 0, len(nums) - 1, []
        while l < r:
            twosum = nums[l] + nums[r]
            if -twosum in nums[l + 1:r]:
               ret.append([nums[l], nums[r], -twosum])
               #l += 1
               r -= 1
               print("if {}, {}".format(l, r))
            elif twosum < 0:
               l += 1
               print("elif1 {}, {}".format(l, r))
            elif twosum > 0:
               r -= 1
               print("elif2 {}, {}".format(l, r))
            else:
                print("???")
                break
        result = []
        for x in ret:
            if x not in result:
                result.append(x)
        return result



# @lc code=end

# 2020-05-01 22:47:02
# 思路： 双指针法 or 夹逼法
# 先排序，之后用指针扫即可

if __name__ == "__main__":
    #l = [0,3,1,1,0,0,1,9,7]
    #l = [-1, 0, 1, 2, -1, -4]
    #l = [0, 0, 0]
    #l = [0, 0, 0, 0]
    #l = [1, 1, 1]
    #l = [1,-1,-1,0]
    #l = [-2,0,1,1,2]
    #l = [-2,0,0,2,2]
    l = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]

    print(Solution().threeSum(l))

