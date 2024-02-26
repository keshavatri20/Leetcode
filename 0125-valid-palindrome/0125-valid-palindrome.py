class Solution:
    def isPalindrome(self, s: str) -> bool:
        l , r = 0, len(s)-1
        
        def alphaNum(c):
            return ('A' <= c <= 'Z' or 'a' <= c <= 'z' or '0' <= c <= '9')
        
        while l<r:
            while l<r and not alphaNum(s[l]):
                l+=1
            while l<r and not alphaNum(s[r]):
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l,r = l+1, r-1
        return True    
        