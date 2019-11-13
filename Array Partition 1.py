class Solution:
    def arrayPairSum(self, nums: [int]) -> int:
        nums.sort()
        min_sum = 0
        for i in range(0,len(nums),2):
            min_sum += nums[i]
        return min_sum

nums=[]
n=int(input("Enter number of elementa in a string:"))
for i in range(n):
    nums.append(int(input("Enter element:")))
result= Solution().arrayPairSum(nums)
print(result)