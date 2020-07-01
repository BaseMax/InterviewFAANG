# Max Base
# https://github.com/BaseMax/InterviewFAANG
class Solution:
	# @param A : string
	# @param B : string
	# @return an integer
	def strStr(self, A, B):
		if A=="" or B=="":
			return -1
		elif A==B:
			return 0
		i=0
		Alength=len(A)
		Blength=len(B)
		while i<Alength:
			found=True
			j=0
			tempI=i
			while j<Blength:
				# print(A[i], B[j])
				if i>=Alength or A[i]!=B[j]:
					found=False
					break
				j+=1
				i+=1
			if found:
				# print("found")
				return tempI
			i=tempI+1
		return -1
s=Solution()
print(s.strStr("maxbasecode@gmail.com", "@"), 11)
print(s.strStr("maxbasecode@gmail.com", ".com"), 17)
print(s.strStr("maxbasecode@gmail.com", "gmail.com"), 12)
print(s.strStr("bbbbbbbbab", "baba"), -1)

