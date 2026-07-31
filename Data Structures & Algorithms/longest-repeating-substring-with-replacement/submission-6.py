class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window 
        l = 0 
        r = 0 
        maxlen = 0 
        freqs = [0] * 26 
        maxfreq = 0 
        for r in range(len(s)):
            idx = ord(s[r]) - ord('A')
            freqs[idx] += 1 
            maxfreq = max(maxfreq , freqs[idx])
            replacement = (r-l+1) - maxfreq
            if replacement <= k:
                maxlen = max(maxlen, r-l+1)
                r += 1 
            else:
                idx = ord(s[l]) - ord('A')
                freqs[idx] -=1 
                l += 1 
        return maxlen



        # Brute Force
        # maxlen = 0 
        # for i in range(len(s)):
        #     freqs = 26 * [0]
        #     max_f = 0
        #     for j in range(i, len(s)):
        #         idx = ord(s[j]) - ord('A')
        #         freqs[idx] += 1 
        #         max_f = max(max_f, freqs[idx])
        #         replacement = (j - i + 1) - max_f

        #         if replacement <= k:
        #             maxlen = max(maxlen, j - i + 1)
        #         else:
        #             break
        # return maxlen