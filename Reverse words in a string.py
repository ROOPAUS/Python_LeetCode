class Solution:
    def reverseWords(self, s: str) -> str:
        st=''
        a=s.split(' ')
        b=a[::-1]
        for i in range(len(a)):
            if(b[i]!=''):
                if(st!=''):
                    st= st + ' '+b[i]
                else:
                    st=b[i]
        return st

s=input("enter string to reverse")
result=Solution().reverseWords(s)
print(result)