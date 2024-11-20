class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        sorted_strs = sorted(strs, key = len)
        smallest_string = sorted_strs[0]
        print(smallest_string)
        is_lcp = True

        for i in range(len(smallest_string)):
            character = smallest_string[i]
            for j in range(1, len(sorted_strs)):
                if sorted_strs[j][i] != character:
                    is_lcp = False
                    break         

            if is_lcp:
                lcp += character  
        return lcp
