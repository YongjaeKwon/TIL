class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        new_s = []
        for i in range(len(s)):
            #if s[i] in alphanumeric:
            if s[i].isalnum():
                new_s.append(s[i])
        
        return new_s == new_s[::-1]
        