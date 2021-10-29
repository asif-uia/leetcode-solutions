class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == haystack or needle == "":
            return 0
        else: 
            for i in range(len(haystack)):
                if(haystack[i:i+len(needle)] == needle):
                    return i
                
            return -1