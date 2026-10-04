class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)
        nums.sort()
        for i in range(0,n):
            if nums[i]<=0 and (i==0 or (nums[i]!=nums[i-1] and i>0)):
                left=i+1
                right=n-1
                while left<right:
                    if nums[i]+nums[left]+nums[right]==0:
                        ans.append([nums[i],nums[left],nums[right]])
                        left+=1
                        right-=1
                    elif nums[i]+nums[left]+nums[right]<0:
                        left+=1
                    else:
                        right-=1
        ans2=[]
        for i in ans:
            if i not in ans2:
                ans2.append(i)
        return ans2