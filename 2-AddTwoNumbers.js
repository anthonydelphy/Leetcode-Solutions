/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val);
 *     this.next = (next===undefined ? null : next);
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let result = new ListNode(0); // Dummy head
    let cursor = result;
    let carry = 0;

    while (l1 || l2 || carry !== 0) {
        let v1 = l1 !== null ? l1.val : 0;
        let v2 = l2 !== null ? l2.val : 0;

        let sum = v1 + v2 + carry;
        //For JavaScript specifically, the Math.Floor is necessary to ensure that the var is truncated down to an integer
        carry = Math.floor(sum / 10); 
        cursor.next = new ListNode(sum % 10);
        cursor = cursor.next;

        if (l1) l1 = l1.next;
        if (l2) l2 = l2.next;
    }
    
    return result.next; // Return the next node to skip the dummy head
};
