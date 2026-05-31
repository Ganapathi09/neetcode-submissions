class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        result = []

        def backtrack(index, subset, total):

            if total == target:
                result.append(subset.copy())
                return

            if total > target:
                return

            for i in range(index, len(candidates)):

                # Skip duplicates at same level
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                # Pick
                subset.append(candidates[i])

                # Move to next index
                backtrack(i + 1,
                          subset,
                          total + candidates[i])

                # Backtrack
                subset.pop()

        backtrack(0, [], 0)
        return result