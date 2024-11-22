class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        mapper = [0]*26
        for c1, c2 in zip(s, t):
            mapper[ord(c1) - ord('a')] += 1
            mapper[ord(c2) - ord('a')] -= 1

        for i in range(26):
            if mapper[i] != 0:
                return False
        return True