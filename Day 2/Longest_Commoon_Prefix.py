class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Sort the array of strings
        strs.sort()
        
        # Take the first and last string after sorting
        first = strs[0]
        last = strs[-1]
        
        # Find the common prefix between the first and last string
        common_prefix = ""
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                break
            common_prefix += first[i]
        
        return common_prefix
