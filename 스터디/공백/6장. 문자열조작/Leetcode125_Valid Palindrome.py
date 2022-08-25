class Solution(object):
    def isPalindrome(self, s):
        string = ""
        for i in s:
            if i.isalpha():
                string += i.lower()

            if i.isnumeric():
                string += i
        
        if string == string[::-1]:
            return True
        else:
            return False

'''
# 1 #
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = re.split('[^a-zA-Z0-9]',s)
        
        s = "".join(s)
        
        if s.lower() == s[::-1].lower():
            return True
        else:
            return False
'''

'''
# 2 #
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        tmp = [x for x in s if x.isalnum()]
        
        return tmp == tmp[::-1]
'''
