#
# @lc app=leetcode.cn id=1200 lang=python3
#
# [1200] 最小绝对差
#
最小绝对差
Category	Difficulty	Likes	Dislikes
algorithms	Easy (66.00%)	18	-
Tags
Unknown

Companies
Unknown

给你个整数数组 arr，其中每个元素都 不相同。

请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。

 

示例 1：

输入：arr = [4,2,1,3]
输出：[[1,2],[2,3],[3,4]]
示例 2：

输入：arr = [1,3,6,10,15]
输出：[[1,3]]
示例 3：

输入：arr = [3,8,-10,23,19,-4,-14,27]
输出：[[-14,-10],[19,23],[23,27]]
 

提示：

2 <= arr.length <= 10^5
-10^6 <= arr[i] <= 10^6
Discussion | Solution

# @lc code=start
###########################################################################
#一刷 2020-04-25 16:50:14

class Solution:
    def minimumAbsDifference(self, arr):
    #def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        #print(arr)
        r,diff= [],(arr[1] - arr[0])
        #print(diff)
        for flag  in range(len(arr[:-1])):
            tmp = arr[flag+1] - arr[flag]
            if diff > (tmp):
                #print("{} > {} - {}".format(diff,arr[flag+1],arr[flag]))
                r = []
                #print(arr[flag],arr[flag+1])
                diff = tmp
                r.append([arr[flag], arr[flag+1]])
            elif diff == tmp:
                r.append([arr[flag],arr[flag+1]])
        #print(r)
        return(r)
# @lc code=end

#testcase = [2,1,3,4]
testcase = [40,11,26,27,-20]
Solution().minimumAbsDifference(testcase)
#感受
#比较简单，通过排序后两两比较即可获取答案
执行用时：392 ms
内存消耗：27.8 MB
###########################################################################
# 查看题解感受
# 国内站的题解和我的思路类似
# 国际站的大神经常会用到zip()方法，自己用的很少，简单解释zip方法和逆过程*zip代码的说明如下:
a = [1, 2, 3]
b = [4, 5, 6]
print(list(zip(a,b)))
#[(1,4),(2,5),(3,6)]
# zip方法为默认内置函数，且返回可迭代对象，效率更高，可以试着改写一下代码
###########################################################################

# @lc code=start
class Solution:
    def minimumAbsDifference(self, arr):
    #def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mn = min(b - a for a, b in zip(arr, arr[1:]))
        return [[a,b] for a,b in zip(arr, arr[1:]) if b-a == mn]
# @lc code=end

#testcase = [2,1,3,4]
testcase = [40,11,26,27,-20]
Solution().minimumAbsDifference(testcase)

# zip的使用的确很巧妙，代码看起来也很简洁，但是实际上和我刚才的代码的复杂度比起来，变慢了
36 / 36 个通过测试用例
状态：通过
执行用时：516 ms
内存消耗：27.8 MB
########################################################################

36/36 cases passed (400 ms)
Your runtime beats 86.15 % of python3 submissions
Your memory usage beats 25 % of python3 submissions (27.7 MB)

class Solution:
    def minimumAbsDifference(self, arr):
    #def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        r,mn = [],arr[1] - arr[0]
        for a, b in zip(arr, arr[1:]):
            if mn > b-a:
                mn = b-a
                r = []
                r.append([a,b])
            elif mn == b-a:
                r.append([a,b])
        return r
# @lc code=end

#testcase = [2,1,3,4]
testcase = [40,11,26,27,-20]
Solution().minimumAbsDifference(testcase)