class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        # Compute the failure function
        failure = [0] * len(needle)
        i, j = 1, 0
        while i < len(needle):
            if needle[i] == needle[j]:
                j += 1
                failure[i] = j
                i += 1
            elif j > 0:
                j = failure[j - 1]
            else:
                failure[i] = 0
                i += 1
        
        # Perform the search
        i, j = 0, 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return i - j
            elif j > 0:
                j = failure[j - 1]
            else:
                i += 1
        
        return -1
