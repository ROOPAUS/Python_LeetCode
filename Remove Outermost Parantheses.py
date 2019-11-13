class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        s_return=""
        s_open=0
        s_close=0
        for i in range(len(S)):
            if(s_open==0):
                s_open=s_open+1
            elif(S[i]=="("):
                s_open=s_open+1
                s_return=s_return + S[i]
            elif(S[i]==")"):
                s_close=s_close+1
                if(s_open!=s_close and s_return!=""):
                    s_return=s_return + S[i]
                else:
                    s_open=0
                    s_close=0
        return s_return

s=input("Enter string:")
result=Solution().removeOuterParentheses(s)
print(result)