class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        return addTwoNumbersCi(l1, l2, 0);
    }
    
    public ListNode addTwoNumbersCi(ListNode l1, ListNode l2, int ci) {
        ListNode head = null;
        if (l1 == null && l2 == null && ci == 0) {
            return head;
        } 
        l1 = l1 == null ? new ListNode(0) : l1;
        l2 = l2 == null ? new ListNode(0) : l2;
        head = new ListNode((l1.val + l2.val + ci) % 10);
        head.next = addTwoNumbersCi(l1.next, l2.next, (l1.val + l2.val + ci) / 10);
        return head;
    }
}
