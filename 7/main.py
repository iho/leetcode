class Solution:
    def reverse(self, x: int) -> int:
        if x < -1*(2**31) or x > ((2**31)-1):
            return 0
        res = int(''.join(reversed(str(abs(x)))))
        if res < -1*(2**31) or res > ((2**31)-1):
            return 0
        if x <0:
            return res*-1
        return res
        