class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        window = s[:k]
        vowel_count = 0
        for i in range(len(window)):
            if window[i] in vowels:
                vowel_count += 1
        
        max_vowel_count = vowel_count

        for i in range(k, len(s)):
            # adjust window
            if s[i-k] in vowels:
                vowel_count -= 1

            # add current character in the window
            if s[i] in vowels:
                vowel_count += 1
            max_vowel_count = max(max_vowel_count, vowel_count)
        return max_vowel_count
