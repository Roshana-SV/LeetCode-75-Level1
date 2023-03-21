class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t=sum(nums)
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            ls=s-nums[i]
            rs=t-s
            if ls==rs:
                return i
        return -1        
