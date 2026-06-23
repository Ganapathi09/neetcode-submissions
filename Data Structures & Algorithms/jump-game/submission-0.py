class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIndex = 0

        for i in range(0,len(nums)):
            if i > maxIndex:
                return False
            maxIndex = max(maxIndex,i + nums[i])
        return True        
        