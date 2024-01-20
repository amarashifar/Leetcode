class Solution:
    def isPalindrome(self, s: str) -> bool:
        myString = ""
        for c in s: 
            if c.isalnum():
                myString += c.lower()
        return myString == myString [::-1]