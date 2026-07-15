class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = defaultdict(int)
        l = 0
        count = 0
        for r in range(len(fruits)):
            freq[fruits[r]] += 1
            if len(freq) > 2:
                freq[fruits[l]] -= 1
                if freq[fruits[l]] == 0:
                    del freq[fruits[l]]
                l += 1
            count = max(count,r-l+1)
        return count

        