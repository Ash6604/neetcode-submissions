class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = set()
        for numss in nums :
            if numss in a :
                return True
            else:
                a.add(numss)
        return False
        