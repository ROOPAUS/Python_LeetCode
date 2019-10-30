class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hash_map = {"(":")", "[":"]", "{":"}"}
        for i in s:
            if i in hash_map:
                stack.append(hash_map[i])
            elif not stack or stack.pop() != i: 
                return False
        return len(stack) == 0

#Driver code
s=input("Enter the string")
result= Solution().isValid(s)
print(result)