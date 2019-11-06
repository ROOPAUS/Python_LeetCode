class Solution:
    def countCharacters(self, words:[str], chars: str) -> int:
        from collections import Counter
        count=0
        charcount=Counter(chars)
        for s in words:
            scount=Counter(s)
            if(scount & charcount==scount):
                count=count+len(s)
        return count
n=int(input("Enter number of words in list: "))
chars=input("Enter characters")
words=[]
for i in range(n):
    words.append(input("Enter element"))
result=Solution().countCharacters(words,chars)
print(result)
