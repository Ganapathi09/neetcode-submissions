class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myset = set()

        left = 0
        result = 0

        for right in range(len(s)):
            while s[right] in myset:
                myset.remove(s[left])
                left += 1
            myset.add(s[right])
            result = max(result , right - left + 1)
        return result        
