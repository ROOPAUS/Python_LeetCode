class Solution:
    def defangIPaddr(self, address: str) -> str:
        r='[.]'
        address_list=list(address)
        for i in range(len(address_list)):
            if(address_list[i]=='.'):
                address_list[i]='[.]'
                
        return ''.join(address_list)

address=input("Enter address")
result=Solution().defangIPaddr(address)
print(result)