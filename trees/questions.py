# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    '''
        1. Find ancestors.
        2. Return the last match between the two lists.
    '''
    def _findAncestors(curr, value, ancestors):
        if curr is None:
            return
        ancestors.append(curr)
        if value < curr.val:
            return _findAncestors(curr.left, value ,ancestors)
        if value > curr.val:
            return _findAncestors(curr.right, value ,ancestors)
        return
    
    ancestors_p = [] 
    ancestors_q = [] 
    _findAncestors(root, p.val, ancestors_p)
    _findAncestors(root, q.val, ancestors_q)
    count = 0
    match_node = None
    while count < len(ancestors_p) and count < len(ancestors_q):
        if ancestors_p[count].val == ancestors_q[count].val:
            match_node = ancestors_p[count]
        count += 1
    return match_node



def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    '''
        Simple BFS
    '''
    from queue import deque
    if root is None:
        return []
    final = []
    queue = deque()
    queue.appendleft(root)
    count = 1
    while len(queue) > 0:
        level = []
        next_level_count = 0
        for _ in range(count):
            curr = queue.pop()
            level.append(curr.val)
            if curr.left is not None:
                queue.appendleft(curr.left)
                next_level_count += 1
            if curr.right is not None:
                queue.appendleft(curr.right)
                next_level_count += 1
        final.append(level)
        count = next_level_count
    return final


def rightSideView(root: Optional[TreeNode]) -> List[int]:
    '''
        Basic idea: do BFS, and the last value at each level 
        is visible from the right (assuming left, right insertion)
    '''
    from queue import deque
    if root is None:
        return []
    queue = deque()
    queue.appendleft(root)
    final = []
    count = 1
    while len(queue) > 0:
        next_level_count = 0
        for idx in range(count):
            curr = queue.pop()
            if idx == count - 1:
                final.append(curr.val)
            if curr.left is not None:
                queue.appendleft(curr.left)
                next_level_count += 1
            if curr.right is not None:
                queue.appendleft(curr.right)
                next_level_count += 1
        count = next_level_count
    return final



def goodNodes(root: TreeNode) -> int:
    '''
        I only need to keep track of the last Good Node in a given path.
        I also know the root is always Good, so will start with that.
    '''
    def _findGoodNodes(curr, last_good_node):
        if curr is None:
            return 0

        if last_good_node is None:
            return 1 + _findGoodNodes(curr.left, curr) + _findGoodNodes(curr.right, curr)

        left_c, right_c = 0, 0
        if curr.val >= last_good_node.val:
            return 1 + _findGoodNodes(curr.left, curr) + _findGoodNodes(curr.right, curr)

        return _findGoodNodes(curr.left, last_good_node) + _findGoodNodes(curr.right, last_good_node)
    
    return _findGoodNodes(root, None)

def isValidBST(root: Optional[TreeNode]) -> bool:
    '''
        Use bounds.
    '''
    def _validBST(curr, left_bound, right_bound):
        if curr is None:
            return True
        
        if not (curr.val > left_bound and curr.val < right_bound):
            return False

        return (_validBST(curr.left, left_bound, curr.val) and _validBST(curr.right, curr.val, right_bound))

    return _validBST(root, float('-inf'), float('inf'))



def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    nodes = []
    def _inOrderTraversal(curr):
        if curr is None:
            return
        _inOrderTraversal(curr.left)
        nodes.append(curr.val)
        _inOrderTraversal(curr.right)
        return
    
    _inOrderTraversal(root)
    return nodes[k-1]


# Did this myself. Took me a really long time but pretty proud.
def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    in_order_hash = {val : idx for idx, val in enumerate(inorder)}
    pre_ord_idx = 0
    def _constructNodes(l, r):
        nonlocal pre_ord_idx
        number = preorder[pre_ord_idx]
        idx = in_order_hash[number]
        node = TreeNode(number)
        pre_ord_idx += 1

        if l >= r:
            return node
        
        # Split into two halves and continue.
        if idx - 1 >= l:
            node.left = _constructNodes(l, idx-1)
        if idx+1 <= r:
            node.right = _constructNodes(idx+1, r)
        
        return node
    root = _constructNodes(0, len(inorder) - 1)
    return root

            



                