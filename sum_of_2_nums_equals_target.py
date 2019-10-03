class Solution():
     def twoSum(self, nums, target):
         for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(target==nums[i]+nums[j]):
                    return [i,j]
    
nums = [2,7,11,15]
target = 9
ret = Solution().twoSum(nums,target)
print(ret)