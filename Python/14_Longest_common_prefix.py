class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        for i in zip(*strs):
            if(len(set(i))) ==1: lcp += i[0]
            else:break
        return lcp
