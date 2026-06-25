class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        lastoccurIndex = {}

        for i, ch in enumerate(s):
            lastoccurIndex[ch] = i

        res = []
        start = 0
        end = 0

        for i, ch in enumerate(s):
            end = max(end, lastoccurIndex[ch])

            if i == end:
                res.append(end - start + 1)
                start = i + 1

        return res