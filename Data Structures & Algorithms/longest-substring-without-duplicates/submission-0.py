class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        MAX_LEN = 0 
        l = 0 
        visited = set()
        for r in range(len(s)):
            while s[r] in visited:
                visited.remove(s[l])
                l += 1 
                
            visited.add(s[r])
            MAX_LEN = max(MAX_LEN, r - l +1)
        return MAX_LEN
