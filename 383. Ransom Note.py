class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomCounter = collections.Counter(ransomNote)
        magCounter = collections.Counter(magazine)

        for k, v in ransomCounter.items():
            if k in magCounter:
                magCounter[k] -= v
            else:
                return False

        for k, v in magCounter.items():
            if v < 0:
                return False
        
        return True