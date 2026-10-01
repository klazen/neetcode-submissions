class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dup=set()
        k=False
        for i in range(len(nums)):
            if nums[i] not in dup:
                dup.add(nums[i])
            else:
                k=True
                break
        return k