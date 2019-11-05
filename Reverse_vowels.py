class Solution:
    def reverseVowels(self, s: str) -> str:
        v={'a','A','e','E','i','I','o','O','u','U'}
        v_stack=[]
        s2=''
        for i in s:
            if(i in v):
                v_stack.append(i)
        s1=list(s)
        for i in range(len(s1)):
            if(s1[i] in v):
                s1[i]=v_stack.pop()
            s2=s2+s1[i]
        return s2

s=input("Enter string to reverse vowels: ")
result=Solution().reverseVowels(s)
print(result)