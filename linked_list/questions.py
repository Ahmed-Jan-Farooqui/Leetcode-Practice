# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    '''
        Use a recursive method that navigates to the end of a linked list,
        and sets the previous node as the next.
    '''
    def _dfs(curr, prev):
        nonlocal head
        if curr is None:
            head = prev
            return
        _dfs(curr.next, curr)
        curr.next = prev

    _dfs(head, None)
    return head

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    '''
        Do a simple merge algorithm.
    '''
    temp_one, temp_two = list1, list2
    final_list = ListNode()
    temp_final = final_list
    while temp_one is not None and temp_two is not None:
        if temp_one.val < temp_two.val:
            temp_final.next = temp_one
            temp_one = temp_one.next
        else:
            temp_final.next = temp_two
            temp_two = temp_two.next
        temp_final = temp_final.next
    if temp_one is not None:
        while temp_one is not None:
            temp_final.next = temp_one
            temp_one = temp_one.next
            temp_final = temp_final.next
    if temp_two is not None:
        while temp_two is not None:
            temp_final.next = temp_two
            temp_two = temp_two.next
            temp_final = temp_final.next
    return final_list.next

def hasCycle(self, head: Optional[ListNode]) -> bool:
    '''
        Use fast and slow pointers.
        Note that if the list terminates, then it doesn't have a cycle.
        The above should be obvious.
    '''
    slow, fast = head, head.next
    while True:
        if slow == None or fast == None:
            return False
        if slow == head:
            return True
        slow = slow.next
        if fast.next is None:
            return False
        fast = fast.next.next


def reorderList(self, head: Optional[ListNode]) -> None:
    '''
        We can find the middle of the linked list, reverse the list,
        and then iterate through and modify the next pointers accordingly.
    '''
    def reverseList(head):
        temp = head
        def _dfs(curr, prev):
            nonlocal temp
            if curr == None:
                temp = prev
                return
            _dfs(curr.next, curr)
            curr.next = prev
        _dfs(head, None)
        return temp
    
    def findMidPoint(head):
        s, f = head, head.next
        while True:
            if f == None:
                break
            if f.next == None:
                break
            f = f.next.next
            s = s.next
        return s
    
    head_second = findMidPoint(head)
    head_second = reverseList(head_second)
    
    temp_one, temp_two = head, head_second

    while (temp_one is not None and temp_two is not None):
        if temp_one == temp_two:
            break
        temp_one_next, temp_two_next = temp_one.next, temp_two.next
        temp_two.next = temp_one.next
        temp_one.next = temp_two
        temp_one, temp_two = temp_one_next, temp_two_next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    '''
        Let's reverse the list and remove the Nth node then reverse
        again.
    '''
    def reverseList(head):
        temp = None
        def _reverse(curr, prev):
            nonlocal temp
            if curr == None:
                temp = prev
                return
            _reverse(curr.next, curr)
            curr.next = prev
        _reverse(head, None)
        return temp
    
    head = reverseList(head)
    count = 0
    temp, prev = head, None
    while temp is not None:
        count += 1
        if count == n:
            if prev == None:
                head = temp.next
            else:
                prev.next = temp.next # Break link.
        temp, prev = temp.next, temp
    return reverseList(head)
                 

            

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    '''
        I can create a hashmap to keep track of:
            old_address : new_address
        This way, I can set the new node's random value to the 
        correct pointer value.
        However, to do this, I must go through the list twice:
        Once to populate the hashmap.
        Second to populate the random pointers!
    '''
    hash_list = {}
    temp_old, head_new, temp_new, prev = head, None, None, None
    while temp_old is not None:
        new_node = Node(temp_old.val)
        if head_new is None:
            head_new = new_node
        if temp_new is None:
            temp_new = new_node
        if prev is not None:
            prev.next = new_node
        prev = new_node
        hash_list[temp_old] = new_node
        temp_old = temp_old.next
        temp_new = temp_new.next
    
    temp_old, temp_new = head, head_new
    while temp_new is not None:
        if temp_old.random is not None:
            temp_new.random = hash_list[temp_old.random]
        else:
            temp_new.random = None
        temp_old = temp_old.next
        temp_new = temp_new.next

    return head_new


def findDuplicate(self, nums: List[int]) -> int:
    '''
        Here, we use the numbers as the index to mark when they are
        encountered. If the index is -ve, that means we have seen this
        number before.
    '''
    for idx, num in enumerate(nums):
        if  nums[abs(num) - 1] < 0:
            return abs(num)
        nums[abs(num) - 1] *= -1
    return 0

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    '''
        Run the merge algorithm on all of the k lists.
    '''
    if len(lists) == 0:
        return None
    min_ptr = None
    min_ptr_val = float('infinity')
    min_ptr_idx = -1
    final_list = ListNode()
    temp = final_list
    while True:
        # Find the minimum value from all the lists.
        for idx, linked_list in enumerate(lists):
            if linked_list is None:
                continue
            if linked_list.val < min_ptr_val:
                min_ptr_val = linked_list.val
                min_ptr = linked_list
                min_ptr_idx = idx
        # Check termination
        if min_ptr is None:
            break
        # Push the minimum value
        temp.next = min_ptr
        temp = temp.next
        # Advance the appropriate list
        lists[min_ptr_idx] = lists[min_ptr_idx].next
        # Reset the minimums
        min_ptr = None
        min_ptr_val = float('infinity')
        min_ptr_idx = -1
    return final_list.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    def reverse(curr, prev, terminate):
        if curr is None:
            return
        if terminate is not None and curr.next == terminate:
            curr.next = prev
            return
        reverse(curr.next, curr, terminate)
        curr.next = prev
    
    temp, potential_head, prev_list = head, None, None
    count = 0
    while temp is not None:
        count += 1
        temp_next = temp.next
        if count == k:
            count = 0
            if potential_head is None:
                potential_head = temp
            if prev_list is None:
                reverse(head, temp.next, temp.next)
                prev_list = head
            else:
                prev_list_next = prev_list.next
                reverse(prev_list.next, temp.next, temp.next)
                prev_list.next = temp
                prev_list = prev_list_next
        temp = temp_next
    return potential_head


            
            
            

                

    