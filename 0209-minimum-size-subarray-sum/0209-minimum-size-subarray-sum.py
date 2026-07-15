class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        ans = float('inf')
        total = 0
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                ans = min(r-l+1,ans)
                total -= nums[l]
                l += 1
        if ans == float('inf'):
            return 0
        return ans

        