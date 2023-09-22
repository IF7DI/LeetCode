class Solution(object):
    def twoSum(self, nums, target):

        for i in range(len(nums)):
            for k in range(i):
                if(nums[i] + nums[k] == target):
                    return i, k
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        