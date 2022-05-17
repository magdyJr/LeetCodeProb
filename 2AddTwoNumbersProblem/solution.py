from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    #checks if the value > 9 then we carry 1 to the next node value
    def checking(self,output,l1):
        if output.val >9:
            if l1.next == None:
                    l1.next=ListNode()
                    l1.next.next=None
                    l1.next.val=1
            else :
                    l1.next.val+=1

    # we add 2 lists recursively
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1==None and l2==None:
            return None
        else :
            output=ListNode()
            #if l1 has none then we output l2
            if l1== None:
                output.val=l2.val
                self.checking(output,l2)
                output.next=self.addTwoNumbers(None,l2.next)
            #if l2 has none then we output l1
            elif l2==None:
                output.val=l1.val
                self.checking(output,l1)
                output.next=self.addTwoNumbers(l1.next,None)
            #here we add them if they r not none
            else:
                output.val=l1.val+l2.val
                self.checking(output,l1)
                output.next=self.addTwoNumbers(l1.next,l2.next)
            if output.val > 9:
                output.val-=10
            return output


#Testcases
l1=ListNode(3,None)
l2=ListNode(4,l1)
l3=ListNode(5,l2)

ll1=ListNode(1,None)
ll2=ListNode(2,ll1)
ll3=ListNode(3,ll2)
sol=Solution()

l55=sol.addTwoNumbers(ll3,l3)
print(f'{l55.val}{l55.next.val}{l55.next.next.val}')

