class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        for i in range(len(s)):
            maxf = 0
            freq = {} 
            for j in range(i,len(s)):
                freq[s[j]] = freq.get(s[j], 0) + 1 

                maxf = max(freq.values())
                window = j - i + 1 
                replacements = window - maxf 

                if replacements <= k:
                    max_len = max(max_len, window)
        return max_len
