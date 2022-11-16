# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        pick = 0
        s = 1
        e = n
        for i in range(1,n+1):
            pick = (s+e)//2
            if guess(pick) == 0:
                return pick
            elif guess(pick) == -1:
                e = pick-1
            elif guess(pick) == 1:
                s = pick + 1
                
            