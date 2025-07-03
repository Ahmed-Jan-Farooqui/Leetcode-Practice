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

