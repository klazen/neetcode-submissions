class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        all_sorted=[]
        for i in strs:
            all_sorted.append("".join(sorted(i)))
        set_sorted=set(all_sorted)
        dic={}
        for i in set_sorted:
            dic[i]=[]
        for i, original in enumerate(strs):
            sorted_str = all_sorted[i]
            dic[sorted_str].append(original)
        return list(dic.values())