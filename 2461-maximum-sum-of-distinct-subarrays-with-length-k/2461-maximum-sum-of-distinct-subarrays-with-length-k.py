class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        window = 0
        ans = 0

        for i in range(k):
            window += nums[i]
            freq[nums[i]] += 1

        if len(freq) == k:
            ans = window

        for i in range(k,len(nums)):
            left = nums[i-k]
            window -= left
            freq[left] -= 1
            if freq[left] == 0:
                del freq[left]
            
            right = nums[i]
            window += right
            freq[right] += 1
            if len(freq) == k:
                ans = max(window,ans)

        return ans
