class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len = 0 

        for i in range(len(s)):
            visited = set()
            for j in range(i, len(s)):
                if s[j] in visited:
                    break 
                visited.add(s[j])
                max_len = max(max_len, j - i + 1)
        return max_len

        # MAX_LEN = 0 
        # l = 0 
        # visited = set()
        # for r in range(len(s)):
        #     while s[r] in visited:
        #         visited.remove(s[l])
        #         l += 1 
                
        #     visited.add(s[r])
        #     MAX_LEN = max(MAX_LEN, r - l +1)
        # return MAX_LEN
 