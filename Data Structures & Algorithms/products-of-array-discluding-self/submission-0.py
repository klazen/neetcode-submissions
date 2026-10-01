class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        for i in nums:
            product*=i
        out=[]
        if product!=0:
            for i in nums:
                out.append(int(product/i))
            return out
        else:
            for i in range(len(nums)):
                if nums[i]!=0:
                    out.append(0)
                else:
                    prod=1
                    for j in range(len(nums)):
                        if j!=i:
                            prod*=nums[j]
                    out.append(prod)
            return out