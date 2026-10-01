class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for i in nums:
            dic[i]=dic.get(i,0)+1
        unique_elements=list(dic.keys())
        def get_frequency(element):
            return dic[element]
        unique_elements.sort(key=get_frequency,reverse=True)
        return unique_elements[:k]