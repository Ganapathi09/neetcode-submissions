class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def dfs(index , xor_total):
            if index == len(nums):
                return xor_total

             #include 

            include = dfs(index+1,xor_total ^ nums[index])

            exclude = dfs(index+1,xor_total) 

            return include+exclude   
        return dfs(0,0)        