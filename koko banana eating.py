class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatAll(piles, k, h):
            time = 0
            for pile in piles:
                time += (pile + k - 1) // k  # Equivalent to math.ceil(pile / k)
            return time <= h
        
        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            if canEatAll(piles, mid, h):
                high = mid  # Try a smaller k
            else:
                low = mid + 1  # Increase k because mid is too small
        return low
