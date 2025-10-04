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