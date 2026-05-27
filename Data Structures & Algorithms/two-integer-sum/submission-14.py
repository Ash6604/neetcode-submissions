class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        mpp = {}

        for i in range(n):
            needed = target - nums[i]
            if needed in mpp:
                return [mpp[needed],i]
            mpp[nums[i]]= i
