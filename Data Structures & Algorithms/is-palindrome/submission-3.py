class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=("".join(char for char in s if char.isalnum())).lower()
        if s1=='':
            return True
        s2=s1[len(s1):0:-1]+s1[0]
        if s1==s2:
            return True
        else:
            return False