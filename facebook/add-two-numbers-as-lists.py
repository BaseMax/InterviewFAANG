# Max Base
# https://github.com/BaseMax/FAANGInterview
# Definition for singly-linked list.
class ListNode:
   def __init__(self, x, pare):
       self.val = x
       # self.next = None
       self.next = pare

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        a=[]
        b=[]
        # Bug: while A.next != None:
        while A != None:
            a.append(A.val)
            try:
                A=A.next
            except AttributeError:
                A=None
        # Bug: while A.next != None:
        while B != None:
            b.append(B.val)
            try:
                B=B.next
            except AttributeError:
                B=None
        # swap b to a if B is bigger then A
        if len(b)>len(a):
            t=a
            a=b
            b=t
        r=[0 for i in a]
        i=0
        la=len(a)-1
        lb=len(b)-1
        while i<=la:
            try:
                r[i]=a[i]+b[i]
                # print("res item a", a[i])
                # print("res item b", b[i])
            except IndexError:
                r[i]=a[i]
                # print("res item a", a[i])
                # print("er")
                # print("res item a", a[i])

            # print("res item", r[i])
            # if r[i] > 9:
            #     print(ri, ri % 10)
            #     # r[i]=r[i]%10
            #     # r[i+1]+=1
            i+=1
        i=0
        lr=len(r)-1
        while i<=lr:
            # print(r[i])
            if r[i] > 9:
                r[i]=r[i]%10
                r[i+1]+=1
            i+=1
        # print(a, b, r)
        return r
s=Solution()
A=ListNode(9, ListNode(9, ListNode(1, None)))
B=ListNode(1, None)
r=s.addTwoNumbers(A, B)
print(r)
