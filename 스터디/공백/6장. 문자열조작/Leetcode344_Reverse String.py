class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # return 없이 구현
        
        left_idx, right_idx = 0, len(s)-1
        while left_idx < right_idx:
            s[left_idx], s[right_idx] = s[right_idx], s[left_idx]
            left_idx +=1
            right_idx -=1

'''
# 1 #
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        print(s.reverse())        

'''