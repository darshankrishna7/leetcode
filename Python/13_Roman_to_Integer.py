class Solution:
    def romanToInt(self, s: str) -> int:
        outp =0
        dic = { 'I': 1, 'V':5, 'X': 10, 'L': 50, 'C' : 100, 'D': 500, 'M': 1000 }

        for i,c in enumerate(s):
            val = dic[c]
            if i < len(s)-1 and val < dic[s[i+1]]:
                outp -= val
            else: outp+=val
        return outp
