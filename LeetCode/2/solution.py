class Solution:
    def addTwoNumbers(self, l1, l2):
        return self.addTwoNumbersCi(l1, l2, 0)

    def addTwoNumbersCi(self, l1, l2, ci):
        head = None
        if l1 == None and l2 == None and ci == 0:
            return head
        l1 = ListNode(0) if l1 == None else l1
        l2 = ListNode(0) if l2 == None else l2
        head = ListNode((l1.val + l2.val + ci) % 10)
        head.next = self.addTwoNumbersCi(l1.next, l2.next, int((l1.val + l2.val + ci) / 10))
        return head
