class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        X=set()
        for i in nums:
            if i in X:
                return i
            else:
                X.add(i)
