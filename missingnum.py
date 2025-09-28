class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(range(len(nums)+1))-sum(nums)
    

if __name__ == '__main__':
    sol=Solution()
    nums = [1,2,0,3]
    print(sol.missingNumber(nums))
        