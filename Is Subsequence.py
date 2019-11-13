class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_list=list(s)
        j=0
        for i in range(len(s_list)):
            if(s_list[i] in t):
                t=t[(t.index(s_list[i])+1):]
                j=j+1
        if(j==len(s_list)):
            return True
        else:
            return False

s=input("Enter string to check:")
t=input("Enter the main string of characters:")
result=Solution().isSubsequence(s,t)
print(result)