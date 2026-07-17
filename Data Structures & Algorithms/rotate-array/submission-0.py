class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)

        k = k % n

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(n - k, n - 1)   # Reverse last k elements
        reverse(0, n - k - 1)   # Reverse first n-k elements
        reverse(0, n - 1)       # Reverse the entire array