class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            s=0
            n=str(num)
            for i in range(len(n)):
                s=s+ int(n[i])
            num=s
        return num
