# Max Base
# https://github.com/BaseMax/FAANGInterview
# numbers={
#   "1000":"M",
#   "500":"D",
#   "100":"C",
#   "50":"L",
#   "10":"X",
#   "5":"V",
#   "1":"I",
# }
class Solution:
  # @param A : integer
  # @return a strings
  numbers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000] 
  symbols = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"] 
  def romanToInt(self, string):
    result=0
    c=len(self.numbers)-1
    l=len(string)
    i=0
    while True:
      if i>=l:
        break
      # print("check", string[i])
      # last element
      ci=c
      while ci>=0:
        # print("compare", string[i], "and", self.symbols[ci])
        if i == l-1:
          if string[i]==self.symbols[ci]:
            result+=self.numbers[ci]
          # else:
          #   print("Error1")
        else:
          if string[i] + string[i+1]==self.symbols[ci]:
            result+=self.numbers[ci]
            i=i+1
          elif string[i]==self.symbols[ci]:
            result+=self.numbers[ci]
          # else:
          #   print("Error2")
        ci-=1
      i=i+1
      # divide=num // self.numbers[i]
      # if divide > 0:
      #   num=num % self.numbers[i]
      #   result+=divide * self.symbols[i]
      # i-=1
    return result
s=Solution()
print(s.romanToInt("I"))
print(s.romanToInt("III"))
print(s.romanToInt("IV"))
print(s.romanToInt("V"))
print(s.romanToInt("VI"))
