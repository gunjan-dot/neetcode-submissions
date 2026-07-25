class Solution:
    

    def validPalindrome(self, s: str) -> bool:
        def checkpalindrome(s):
            test = s
            s_list = list(s)
            l, r = 0 , len(s) - 1
            while l <r:
                s_list[l], s_list[r] = s_list[r], s_list[l]
                l += 1 
                r-= 1 
            s = "".join(s_list)
            return test == s 

        for i in range(len(s)):
            check = checkpalindrome(s[:i] + s[i+1:])
            if check:
                return True
        return False
        