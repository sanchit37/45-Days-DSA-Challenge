class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            columnNumber -= 1  # Adjust for 1-based indexing
            result = chr(65 + (columnNumber % 26)) + result
            columnNumber //= 26
        return result

# Test cases
def test_convertToTitle():
    solution = Solution()
    
    # Test case 1
    assert solution.convertToTitle(1) == "A", "Test case 1 failed"
    
    # Test case 2
    assert solution.convertToTitle(28) == "AB", "Test case 2 failed"
    
    # Test case 3
    assert solution.convertToTitle(701) == "ZY", "Test case 3 failed"
    
    # Additional test cases
    assert solution.convertToTitle(26) == "Z", "Test case 4 failed"
    assert solution.convertToTitle(27) == "AA", "Test case 5 failed"
    assert solution.convertToTitle(52) == "AZ", "Test case 6 failed"
    assert solution.convertToTitle(703) == "AAA", "Test case 7 failed"
    
    print("All test cases passed!")

# Run the tests
test_convertToTitle()
