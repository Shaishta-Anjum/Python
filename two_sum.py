class Solution():   
    def twoSum(self, nums:list[int], target: int) -> list[int]:
        for i, x1 in enumerate(nums):
            for j in range(i+1,len(nums)):
                x2=nums[j]
                if x1+x2==target:
                    return [i,j]

lst=[2,3,4,5,6,7,8,9]
t=int(input("Enter Target value:"))
res=Solution().twoSum(lst,t)
print(res)