def addtwonumbers(l1, l2):
    val1 = l1[::-1]
    val2 = l2[::-1]
    val1_str = ''.join(map(str, val1))
    val2_str = ''.join(map(str, val2))  
    sum=str(int(val1_str)+int(val2_str))
    sum=sum[::-1]
    sum=[int(digit) for digit in sum]
    return sum

l1 = [2, 3, 4]
l2 = [5, 6, 7]
print(addtwonumbers(l1, l2))

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
       cur=l1
       l1_val_str=""
       while(cur):
            l1_val_str=l1_val_str+str(cur.val)
            cur=cur.next
       l1_val_str=int(l1_val_str[::-1])
       l2_val_str=""
       cur2=l2
       while(cur2):
            l2_val_str=l2_val_str+str(cur2.val)
            cur2=cur2.next
       l2_val_str=int(l2_val_str[::-1])
       sum=str(l1_val_str+l2_val_str)
       sum=sum[::-1]
       head = ListNode(int(sum[0]))
       current = head
    
       for digit in sum[1:]:
            current.next = ListNode(int(digit))
            current = current.next
       return head
