class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        k=True
        for i in s:
            if s.count(i)==t.count(i) and len(s)==len(t):
                k=True
            else:
                k=False
                break
        return k