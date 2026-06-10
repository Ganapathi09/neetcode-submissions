class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(start,subset):
            if len(subset) == k:
                result.append(subset.copy())
                return

            for num in range(start,n+1):
                subset.append(num)
                dfs(num+1,subset)
                subset.pop() 
        dfs(1,[])

        return result         

        