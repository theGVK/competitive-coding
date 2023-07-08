class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        m=defaultdict(int)
        x=0
        for i in nums:
            m[i]+=1
            if m[i]==1:
                nums[x]=i
                x+=1
        return len(m)
