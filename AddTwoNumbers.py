# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        carryOver = 0
        currL1 = l1
        currL2 = l2
        newList = ListNode(-1)
        currNew = newList
        while (currL1 is not None or currL2 is not None):
            currSum = 0
            if (currL1 is not None):
                currSum += currL1.val
                currL1 = currL1.next
                
            
            if (currL2 is not None):
                currSum += currL2.val
                currL2 = currL2.next
            
            currSum += carryOver
            
            if (currSum >= 10):
                currSum = currSum % 10
                carryOver = 1
            else :
                carryOver = 0
            
            currNew.next = ListNode(currSum)
            currNew = currNew.next
        
        if (carryOver == 1):
            currNew.next = ListNode(1)
        
        return newList.next
            
                
                
            
        