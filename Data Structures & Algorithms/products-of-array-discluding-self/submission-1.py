class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l2r = [1] * len(nums)  # l2r[i] = product of all elements BEFORE i
        r2l = [1] * len(nums)  # r2l[i] = product of all elements AFTER i

        prod = 1
        for i in range(1, len(nums)):
            prod *= nums[i-1]
            l2r[i] = prod

        prod = 1
        for i in range(len(nums) - 2, -1, -1):
            prod *= nums[i+1]
            r2l[i] = prod

        return [l2r[i] * r2l[i] for i in range(len(nums))]

