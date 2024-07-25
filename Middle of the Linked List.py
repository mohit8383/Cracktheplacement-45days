class Solution(object):
    def middleNode(self, head):
        count = 0
        ptr = head
        while ptr is not None:
            count += 1
            ptr = ptr.next
        
        ptr = head
        for i in range(count // 2):
            ptr = ptr.next
        
        return ptr
    
