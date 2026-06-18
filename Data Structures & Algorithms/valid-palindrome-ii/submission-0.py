class Solution:
    def validPalindrome(self, s: str) -> bool:
        #helper func
        def isplaindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
            
        #main func
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return (
                    isplaindrome(left + 1, right) or
                    isplaindrome(left, right - 1)
                )

            left += 1
            right -= 1

        return True