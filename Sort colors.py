class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n=len(nums)

        for i in range(n - 1):
            for j in range(i + 1, n):
                if(nums[i] > nums[j]):
                    nums[i], nums[j] = nums[j], nums[i]
        
