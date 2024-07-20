class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()[::-1]
        result = ""
        for word in words:
            result += word + " "
        return result[:-1]
