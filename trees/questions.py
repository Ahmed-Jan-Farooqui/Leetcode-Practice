# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    def _dfs(curr):
        if curr is None:
            return None
        curr_left = curr.left
        curr_right = curr.right
        curr.left = _dfs(curr_right)
        curr.right = _dfs(curr_left)
        return curr
    
    return _dfs(root)


def maxDepth(root: Optional[TreeNode]) -> int:
    def _dfs(curr, height):
        if curr is None:
            return height
        left_height = _dfs(curr.left, height+1)
        right_height = _dfs(curr.right, height+1)
        height = max(left_height, right_height)
        return height
    return _dfs(root, 0)


def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    '''
        Basic Idea:
            1. The max length path from any node to any other node
            is just the height of the left and right trees added together.
            2. Use this information to figure out the max length path
            of the entire tree.
    '''
    def _dfs(curr, height):
        if curr is None:
            return height
        left_h, right_h = _dfs(curr.left, height+1), _dfs(curr.right, height+1)
        height = max(left_h, right_h)
        max_len_path = _dfs(curr.left, 0) + _dfs(curr.right, 0)
        return max(height, max_len_path)
    return _dfs(root.left, 0) + _dfs(root.right, 0)


def isBalanced(root: Optional[TreeNode]) -> bool:
    def findHeight(curr, height):
        if curr is None:
            return height
        left_h = findHeight(curr.left, height+1)
        right_h = findHeight(curr.right, height+1)
        if abs(left_h - right_h) > 1 or left_h == -1 or right_h == -1:
            return -1
        return max(left_h, right_h)
    
    isHeightBalanced = False if findHeight(root, 0) == -1 else True
    return isHeightBalanced

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    def _dfs(curr_one, curr_two):
        if curr_one is None and curr_two is None:
            return True
        if curr_one is None or curr_two is None:
            return False
        if curr_one.val != curr_two.val:
            return False
        left_validity = _dfs(curr_one.left, curr_two.left)
        right_validity = _dfs(curr_one.right, curr_two.right)
        return left_validity and right_validity
    return _dfs(p, q)


def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def isSame(curr_one, curr_two):
        if curr_one is None and curr_two is None:
            return True
        if curr_one is None or curr_two is None:
            return False
        if curr_one.val != curr_two.val:
            return False
        left_v = isSame(curr_one.left, curr_two.left)
        right_v = isSame(curr_one.right, curr_two.right)
        return left_v and right_v
    
    def isSubtree(curr, root):
        if curr is None:
            return False
        if isSame(curr, root):
            return True
        found_l, found_r = isSubtree(curr.left, root), isSubtree(curr.right, root)
        return found_l or found_r
    
    return isSubtree(root, subRoot)



                