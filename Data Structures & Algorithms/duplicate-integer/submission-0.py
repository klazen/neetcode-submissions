class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dup=[]
        k=False
        for i in range(len(nums)):
            if nums[i] not in dup:
                dup.append(nums[i])
            else:
                k=True
                break
        return k