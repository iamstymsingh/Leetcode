from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # calculate frequency of chars of string p
        pfreq_map = Counter(p)

        # starting window is of size p
        window_freq = Counter(s[:len(p)])
        start_idxs = []

        for i in range(len(p), len(s)):
            if window_freq == pfreq_map:
                start_idxs.append(i - len(p))

            # adjust window
            window_freq[s[i]] += 1 # add current character
            window_freq[s[i-len(p)]] -= 1 # remove invalid character

            if window_freq[s[i-len(p)]] == 0:
                del window_freq[s[i-len(p)]]

        # check for the last window
        if window_freq == pfreq_map:
                start_idxs.append(len(s) - len(p))
        return start_idxs
