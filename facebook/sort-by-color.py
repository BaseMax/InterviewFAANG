# Max Base
# https://github.com/BaseMax/InterviewFAANG
class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(A) - 1):
                if A[i] > A[i + 1]:
                    A[i], A[i + 1] = A[i + 1], A[i]
                    swapped = True
        return A

s=Solution()
print(s.sortColors([0, 1, 2, 0, 1, 2]))
