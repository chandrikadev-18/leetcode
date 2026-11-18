# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        st = []
        curr = head

        while curr:
            while st and st[-1].val < curr.val:
                st.pop()

            st.append(curr)
            curr = curr.next

        dummy = ListNode(0)
        curr = dummy

        for node in st:
            curr.next = node
            curr = curr.next

        curr.next = None

        return dummy.next