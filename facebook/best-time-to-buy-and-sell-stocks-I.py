# Max Base
# https://github.com/BaseMax/InterviewFAANG
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        count=len(A)
        if count<2:
            return 0
        previous = A[0]
        result = 0
        i=0
        while i<count:
            j=i+1
            while j<count:
                # print(i,j)
                temp = A[j] - A[i]
                if temp > result:
                    result=temp
                j+=1
            i+=1
        # another commons way:
        # for a in A[1:]:
        #     temp = a - previous
        #     if temp > result:
        #         result=temp
        #     previous = a
        return result

s=Solution()
print(s.maxProfit([1, 2]), "excepted", 1)
print(s.maxProfit([1, 4, 5, 2, 4]), "excepted", 4)

