lass Solution:
    def productExceptSelf(self, nums, n):
        # Initialize the result array with 1s
        result = [1] * n
        
        # Compute left products
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]
        
        # Compute right products and multiply with left products
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        
        return result
