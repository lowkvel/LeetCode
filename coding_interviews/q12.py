from typing import List

# same question as lc79
"""
    矩阵中的路径

    给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
    单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

    例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。
        ABCE
        SFCS
        ADEE

    示例 1：
        输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
        输出：true

    示例 2：
        输入：board = [["a","b"],["c","d"]], word = "abcd"
        输出：false
 
    提示：
        1 <= board.length <= 200
        1 <= board[i].length <= 200
        board 和 word 仅由大小写英文字母组成

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        pass






if __name__ == '__main__':

    s = Solution()

    input = [
        [[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"],
        [[["a","b"],["c","d"]], "abcd"],
    ]

    print('-----')
    for item in input:
        print(s.exist())

        print('-----')

