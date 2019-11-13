class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        s_count=Counter(s)
        count=0
        for i in range(len(s)):
            if(s_count[s[i]]==1):
                print(s[0])
                print(s_count[i])
                count=1
                return i
        if(count==0):
            return -1
s=input("Enter string:")
result=Solution().firstUniqChar(s)
print(result)