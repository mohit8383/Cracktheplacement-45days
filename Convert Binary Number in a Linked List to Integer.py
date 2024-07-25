class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary = []
        while head:
            binary.append(head.val)
            head = head.next
        ans = 0
        binary = binary[::-1]
        
        for i in range(len(binary)):
            bit = int(binary[i])
            ans += bit * (2 ** i)
        return ans
