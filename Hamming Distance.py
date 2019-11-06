class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x1=list(bin(x)[2:].zfill(32))
        y1=list(bin(y)[2:].zfill(32))
        count=0
        for i in range(len(x1)):
            if(x1[i]=='1' and y1[i]=='0'):
                count=count+1
            elif(x1[i]=='0' and y1[i]=='1'):
                count=count+1
        return count
        
    
x=int(input("Enter the value of x:"))

y=int(input("Enter the value of y:"))
result=Solution().hammingDistance(x,y)
print(result)