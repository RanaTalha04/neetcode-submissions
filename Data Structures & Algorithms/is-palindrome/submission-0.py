class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(char.lower() for char in s if char.isalnum())

        left = 0
        right = len(clean) - 1
        while right > left:
            if clean[right] != clean[left]:
                return False
            else:
                left += 1
                right -= 1
        return True
