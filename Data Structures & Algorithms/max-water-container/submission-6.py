class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        left=0
        right=n-1
        def area(left,right):
            return (right-left)*(min(heights[left],heights[right]))
        ar=area(left,right)
        while right>left:
              if heights[left]<=heights[right]:
                left+=1
                ar=max(ar,area(left,right))
              else:
                right-=1
                ar=max(ar,area(left,right))
        return ar