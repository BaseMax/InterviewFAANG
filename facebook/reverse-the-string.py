# Max Base
# https://github.com/BaseMax/InterviewFAANG
class Solution:
	# @param A : string
	# @return a strings
	def solve(self, A):
		words=A.split(" ")
		# print(words)
		words=reversed(words)
		result=""
		for word in words:
			# print(word)
			if word != "":
				result+=word+" "
		result=result.strip()
		# if result[-1] == " ":
		# 	result=result[0:-1]
		return result

s=Solution()
print(s.solve("the sky is blue"))
print(s.solve("this is ib"))
print(s.solve("qxkpvo  f   w vdg t wqxy ln mbqmtwwbaegx   mskgtlenfnipsl bddjk znhksoewu zwh bd fqecoskmo"))
