from typing import List

# same question as lc105
"""
    重建二叉树

    输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

    例如，给出
        前序遍历 preorder = [3,9,20,15,7]   # 根左右
        中序遍历 inorder = [9,3,15,20,7]    # 左根右

    返回如下的二叉树：
        3
       / \
      9  20
        /  \
       15   7

    限制：
        0 <= 节点个数 <= 5000

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # tree construction in recursion, 424ms,88.2mb, 
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def build(preorder: List[int], inorder: List[int]) -> TreeNode:

            # empty list, return
            if len(preorder) == 0:
                return

            # single element left, return a new node
            if len(preorder) == 1:
                return TreeNode(preorder[0])

            # create a new node
            node = TreeNode(preorder[0])
                
            # split the preorder and inorder into left and right parts
            position = -1
            for index in range(0, len(inorder), 1):
                if inorder[index] == preorder[0]:
                    position = index
                    break
            in_left = inorder[0:position]
            in_right = inorder[position+1:len(inorder)]
            pre_left = preorder[1:len(in_left)+1]
            pre_right = preorder[len(in_left)+1:]

            # recursively construct both left and right children
            node.left = build(pre_left, in_left)
            node.right = build(pre_right, in_right)

            # return the tree constructed
            return node

        if preorder is not None and inorder is not None:
            return build(preorder, inorder)
        else:
            return "invalid input"



if __name__ == '__main__':

    s = Solution()

    input = [
        [[3,9,20,15,7], [9,3,15,20,7]],
        [[1,2,4,7,3,5,6,8], [4,7,2,1,5,3,8,6]],

        [[3], [3]],
        [[None], [None]],
        [None, None],
         
    ]

    print('-----')
    for item in input:
        print(s.buildTree(item[0], item[1]))

        print('-----')
