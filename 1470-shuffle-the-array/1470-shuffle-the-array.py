class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result=[]
        i=0
        j=n

        for k in range(len(nums)):
            if k<n:
                result.append(nums[i])
                i+=1
            if j<len(nums):
                result.append(nums[j])
                j+=1
        return result