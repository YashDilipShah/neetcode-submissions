class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        l = 0
        r = 1
        while r <= len(nums) - 1:
            if nums[l] != nums[r]:
                k += 1
                nums[l+1] = nums[r]
                l += 1
                r += 1
            else: 
                r += 1
        return k