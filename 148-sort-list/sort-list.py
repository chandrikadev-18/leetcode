class Solution:
    def sortList(self, head):
        
        # Base condition
        if not head or not head.next:
            return head

        # Step 1: Find the middle
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Divide into two halves
        mid = slow.next
        slow.next = None

        # Step 3: Sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)

        # Step 4: Merge sorted halves
        return self.merge(left, right)

    def merge(self, left, right):

        dummy = ListNode(0)
        current = dummy

        while left and right:

            if left.val <= right.val:
                current.next = left
                left = left.next

            else:
                current.next = right
                right = right.next

            current = current.next

        if left:
            current.next = left

        if right:
            current.next = right

        return dummy.next