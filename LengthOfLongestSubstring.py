from collections import defaultdict
class Solution(object):
    #Sliding window with HashSet
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        j = 0
        maxLength = 0
        aSet = set()
        
        while (j < len(s)):
            if (s[j] not in aSet):
                aSet.add(s[j])
                j += 1
                maxLength = max(maxLength, j - i)
            else:
                aSet.remove(s[i])
                i += 1
        
        return maxLength

    #Sliding window with HashMap
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        aDict = defaultdict(int)
        i = 0
        j = 0
        maxLength = 0
        
        while (j < len(s)):
            if (s[j] in aDict):
                i = max(i, aDict[s[j]] + 1)
            aDict[s[j]] = j
            j += 1
            maxLength = max(maxLength, j - i)
                
        return maxLength
                
            
            
        
                
                
        

        