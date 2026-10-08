class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        if height==[0]*n or len(height)<=2:
            return 0
        c=0
        for i in range(n):
            if height[i]>0:
                left=i
                break
        for i in range(n-1,-1,-1):
            if height[i]>0:
                RIGHT=i
                break
        
        while True:
            if left<RIGHT and height[left+1]>=height[left]:
                left+=1
            else:
                break
        while True:
            if height[RIGHT-1]>=height[RIGHT]:
                RIGHT-=1
            else:
                break
        
        
        while left<RIGHT:
            right=-1
            for i in range(left+1,RIGHT+1):
                if i==RIGHT and height[RIGHT]<height[left]:
                    break
                if height[i]>=height[left]:
                    right=i
                    break
            if right == -1:
                max_height = -1
                for i in range(left+1, RIGHT+1):
                    if height[i] >= max_height:
                        max_height = height[i]
                        right = i
                if right == -1: 
                    break
            
            for i in range(left+1,right):
                c+=min(height[left],height[right])-height[i]
            left=right
            if left==RIGHT:
                break
        return c