# Max Base
# https://github.com/BaseMax/FAANGInterview
class Solution:
  # @param A : string
  # @return a list of strings
  def prettyJSON(self, A):
    indent = 0
    res = []
    line = ''
    for x in A:
      if x in '{[':
        if line:
          res.append(line)
        res.append('\t' * indent + x)
        line = ''
        indent += 1
      elif x in ']}':
        if line:
          res.append(line)
        indent -= 1
        line = '\t' * indent + x  # Might be followed by ','
      else:
        if not line:
          line = '\t' * indent
        line += x
        if x == ",":
          res.append(line)
          line = ''
    if line:
      res.append(line)
    return res

s=Solution()
# print( s.prettyJSON('{A:"B۱",C:{D:"E",F:{G:"H",I:"J"}}}') )
# print( s.prettyJSON('["foo",5,{"bar":["baz",null,1.0,2]}]') )
print( s.prettyJSON('["foo",5,["bar",1,2]]') )
# print( s.prettyJSON('[123,456]') )
