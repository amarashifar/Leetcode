class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for characters in s: 
            if characters.isalnum():
                string += characters.lower()
        return string == string[::-1]