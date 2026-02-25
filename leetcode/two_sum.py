'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

class Solution():
    def twoSum(self,nums,target):
        seen={}
        for i in range(len(nums)):
            diff=target-nums[i]
            print(seen)
            if diff in seen:
                return (seen[diff],i)
            else:
                seen[nums[i]]=i
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range (len(nums)):
            diff = target - nums[i]
            if diff in nums[i+1:]:
                return [i,nums.index(diff,i+1)]
"""            
nums = [1,2,3,4]
target=6
sol=Solution()
ans=sol.twoSum(nums,target)
print(ans)               
