# Max Base
# https://github.com/BaseMax/InterviewFAANG
class Solution:
    # @param A : list of integers
    # @return A after the sort
    # Bad performance:
    # def sortColors(self, A):
    #     swap = True
    #     while swap:
    #         swap = False
    #         for i in range(len(A) - 1):
    #             if A[i] > A[i + 1]:
    #                 A[i], A[i + 1] = A[i + 1], A[i]
    #                 swap = True
    #     return A
    def sortColors(self, A):
        result1=[]
        result2=[]
        result3=[]
        for i in A:
            if i == 0:
                result1.append(i)
            elif i == 1:
                result2.append(i)
            elif i == 2:
                result3.append(i)
        # print(result1)
        # print(result2)
        # print(result3)
        return result1+result2+result3

s=Solution()
print(s.sortColors([0, 1, 2, 0, 1, 2]))
print(s.sortColors([ 2, 0, 0, 1, 0, 0, 2, 2, 1, 1, 0, 0, 1, 0, 2, 1, 1, 0, 1, 0, 1, 2, 2, 2, 0, 0, 1, 0, 2, 1, 1, 2, 1, 2, 2, 1, 0, 2, 2, 1, 1, 1, 0, 1, 0, 1, 0, 2, 1, 2, 0, 2, 0, 1, 1, 0, 2, 2, 1, 2, 0, 2, 1, 1, 1, 2, 0, 1, 0, 2, 2, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 2, 1, 1, 0, 2, 1, 2, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 1, 1, 0, 2, 1, 2, 2, 2, 1, 2, 2, 0, 1, 0, 1, 2, 1, 1, 0, 1, 2, 0, 1, 0, 2, 2, 1, 2, 1, 0, 2, 2, 1, 1, 0, 2, 1, 2 ]))
