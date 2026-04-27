class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = set(nums)
        longest = 0

        for num in a :
            if (num-1) not in a:
                length = 1
                while (num +length) in a :
                    length +=1
                longest = max(length ,longest)

        return longest        