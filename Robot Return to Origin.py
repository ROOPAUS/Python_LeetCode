class Solution:
    def judgeCircle(self, moves: str) -> bool:
        up_down=0
        right_left=0
        for i in moves:
            if(i=='U'):
                up_down=up_down+1
            elif(i=='D'):
                up_down=up_down-1
            elif(i=='R'):
                right_left=right_left+1
            else:
                right_left=right_left-1
        if(up_down==0 and right_left==0):
            return True
        else:
            return False

moves=input("Enter string")
result=Solution().judgeCircle(moves)
print(result)
        
"""Simpler method
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D') """