
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret=[]
        set_num=set(nums)
        for i in range(1,len(nums)+1):
            if i not in set_num:
                ret.append(i)
        return ret




if __name__ == '__main__':
    sol=Solution()
    nums = [1,2,3,3,6,7]
    print(sol.findDisappearedNumbers(nums))
    