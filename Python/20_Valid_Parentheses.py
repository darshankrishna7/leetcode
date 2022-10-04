class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        for i in range(len(s)):
            if (s[i]=="(" or s[i]=="[" or s[i]=="{"):
                a.append(s[i])
            else:
                if len(a)==0:
                    return False
                if (s[i]==")" and a[-1]=="(") or(s[i]=="]"and a[-1]=="[") or (s[i]=="}"and a[-1]=="{"):
                    a.pop(-1)
                    pass     
                else:
                    return False
        if len(a)==0:
                return True
        else:
                return False
