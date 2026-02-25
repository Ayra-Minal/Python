'''
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
Return the answer in an array.
Example 1:
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
'''

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp=sorted(nums)
        ret=[]
        d={}
        for i,num in enumerate(temp):
            if num not in d:
                d[num]=i
        for i in nums:
            ret.append(d[i])
        return ret

if __name__ == '__main__':
    sol=Solution()
    nums = [1,2,3,3,6,7]
    print(sol.smallerNumbersThanCurrent(nums))
