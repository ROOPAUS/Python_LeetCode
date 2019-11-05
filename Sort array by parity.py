
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        a=[]
        b=[]
        for i in A:
            if(i%2==0):
                a.append(i)
            else:
                b.append(i)
        a=a+b
        
        return a

n=input("Enter number of elements in list:")
A=[]
for i in range(n):
    A.append(input("Enter list element"))
result=Solution().sortArrayByParity(A)
print(result)