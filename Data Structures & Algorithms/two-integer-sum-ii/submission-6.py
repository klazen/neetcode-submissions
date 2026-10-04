class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if target%2==0 and numbers.count(int(target/2))>1:
            return [numbers.index(int(target/2))+1,numbers.index(int(target/2))+2]
        else:
            nums=set(numbers)
            if target>0:
                c=int(target/2)+1
            elif target==0:
                c=1
            else:
                c=int(target/2-0.5)+1
            while True:
                if c in nums and (target-c) in nums:
                    return [numbers.index(target-c)+1,numbers.index(c)+1]                
                c+=1