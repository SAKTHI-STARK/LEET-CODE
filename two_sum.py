class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            for j in range(i+1,len(nums)):
                if target==nums[i]+nums[j]:
                    print(i,j)

    
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i,x in enumerate(nums):
#             for j in range(i+1,len(nums)):
#                 if target==nums[i]+nums[j]:
#                     return[i,j]