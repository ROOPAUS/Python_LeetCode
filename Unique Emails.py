class Solution:
    def numUniqueEmails(self, emails: [str]) -> int:
        s=[]
        count=0
        for i in emails:
            if('.' in i):
                j=i[0:i.index('@')].replace('.','')
            else:
                j=i[0:i.index('@')]
            if('+' in j):
                j=j[0:j.index('+')] + i[i.index('@'):len(i)]
            else:
                j=j+i[i.index('@'):len(i)]
            if(j not in s):
                s.append(j)
                count=count+1
        
        return count

n=int(input("Enter number of elements in list:"))
emails=[]
for i in range(n):
    emails.append(input("Enter list element"))
result=Solution().numUniqueEmails(emails)
print(result)