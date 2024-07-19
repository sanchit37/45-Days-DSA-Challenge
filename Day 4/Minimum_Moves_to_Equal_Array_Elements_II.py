class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # Sort the array
        nums.sort()
        
        # Find the median
        median = nums[len(nums) // 2]
        
        # Calculate the sum of absolute differences
        moves = sum(abs(num - median) for num in nums)
        
        return moves

# Test cases
def test_minMoves2():
    solution = Solution()
    
    # Test case 1
    assert solution.minMoves2([1,2,3]) == 2, "Test case 1 failed"
    
    # Test case 2
    assert solution.minMoves2([1,10,2,9]) == 16, "Test case 2 failed"
    
    # Additional test cases
    assert solution.minMoves2([1,0,0,8,6]) == 14, "Test case 3 failed"
    assert solution.minMoves2([1,2,3,4]) == 4, "Test case 4 failed"
    assert solution.minMoves2([1]) == 0, "Test case 5 failed"
    
    print("All test cases passed!")

# Run the tests
test_minMoves2()
