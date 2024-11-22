class Solution:
    def isPalindrome(self, x: int) -> bool:
        revNum = 0
        if x < 0 or (x > 9 and x % 10 == 0):
            return False

        while x > revNum:
            revNum = revNum * 10 + x % 10
            x //= 10

        return True if revNum // 10 == x or revNum == x else False