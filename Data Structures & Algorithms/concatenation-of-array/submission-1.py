class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans: List[int] = []
        for i in range(2*len(nums)):
            ans.append(nums[i % len(nums)])

        return ans
            
        