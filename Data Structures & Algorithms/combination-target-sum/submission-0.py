class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack (index,combination,total):
            if total == target:
                res.append(combination.copy())
                return
            if index >=len(nums) or total > target:
                return

            # make all combinations

            combination.append(nums[index])
            backtrack(index,combination,total+ nums[index])

            #backtrack

            combination.pop()

            #choice 2 skipcurr and try another index
            backtrack(index+1,combination,total) 
        backtrack(0,[],0)
        return res        

        