#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        return invert_tree(root)

def invert_tree(node):
    if node.left == None and node.right == None:
        return node
    # process
    node.left, node.right = node.right, node.left
    # drill down
    if node.left == None:
        invert_tree(node.right)
    if node.right == None:
        invert_tree(node.left)
    # reverse state
    return node
# @lc code=end

################################################################################

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        return invert_tree(root)

def invert_tree(node):
    if node.left == None and node.right == None:
        return node
    # process
    node.left, node.right = node.right, node.left
    # drill down
    invert_tree(node.right)
    invert_tree(node.left)
    # reverse state
    return node
# @lc code=end

################################################################################
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        return invert_tree(root)

def invert_tree(node):
    if node.left == None and node.right == None:
        return node
    # process
    node.left, node.right = node.right, node.left
    # drill down
    invert_tree(node.right)
    invert_tree(node.left)
    # reverse state
    return node
# @lc code=end


################################################################################
#Accepted
#68/68 cases passed (48 ms)
#Your runtime beats 25.44 % of python3 submissions
#Your memory usage beats 5.26 % of python3 submissions (13.8 MB)

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        return invert_tree(root)

def invert_tree(node):
    if not node:
        return None
    # process
    node.left, node.right = node.right, node.left
    # drill down
    invert_tree(node.right)
    invert_tree(node.left)
    # reverse state
    return node
# @lc code=end
# 模板要变通的使用，关键在于节奏
# 理解leetcode中二叉树的序列化和反序列化

