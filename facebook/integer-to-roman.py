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
numbers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000] 
symbols = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"] 
def parse(num):
  result=""
  num=int(num)
  i=len(numbers)-1
  while i>=0:
    divide=num // numbers[i]
    if divide > 0:
      num=num % numbers[i]
      result+=divide * symbols[i]
    i-=1
  return result
print(parse(1))
print(parse(5))
print(parse(6))
print(parse(7))
print(parse(9))
print(parse(10))
print(parse(11))
print(parse(58))
print(parse(1994))
