class Solution:
    def uniqueOccurrences(self, a: [int]) -> bool:
        dic={}
        for i in a:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=0
        temp=set(dic.values())
        if len(temp)==len(dic):
            return True
        return False

a=[]
n=int(input("Enter number of elements in list:"))
print(n)
for i in range(n):
    a.append(int(input("Enter element")))
result=Solution().uniqueOccurrences(a)
print(result)
