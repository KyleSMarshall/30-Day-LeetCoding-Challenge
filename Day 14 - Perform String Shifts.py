  # Solution
  
  class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        s = list(s)
        for i in range(len(shift)):
            if shift[i][0] == 0:
                for k in range(shift[i][1]):
                    s.append(s.pop(0))
            else:
                for k in range(shift[i][1]):
                    s = [s.pop()] + s
        return ''.join(s)
