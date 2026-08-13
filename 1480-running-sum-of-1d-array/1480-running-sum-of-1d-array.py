class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum=0
        for i, x in enumerate(nums):
            nums[i]+=sum
            sum+=x
        
        return nums
