class Solution:
    def maxArea(self, height: List[int]) -> int:
        cap = 0
        k = 0
        j = len(height) - 1
        for i in range(len(height)):
            width = j - k
            H = min(height[k],height[j])
            total = width * H
            cap = max(total,cap)
            if height[k] < height[j]:
                k += 1
            else:
                j -= 1
        return cap