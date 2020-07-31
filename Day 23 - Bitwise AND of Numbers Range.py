'''
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Ex:

Input: [5,7]
Output: 4
'''

# Solution

class Solution:
    def rangeBitwiseAnd(self, m, n):
        if m == 0:
            return 0
        
        # Find the power of 2 that is closest but greater than m and less than n
        # Let's use Binary search
        l, r = 0, 32
        
        while l < r:
            mid = l + (r - l) // 2

            if 2 ** mid >= m:
                r = mid
            else:
                l = mid + 1
        
        low_pow = l
        # Check if this power of 2 is less than the upper lim
        use_two = 2 ** low_pow <= n
        
        '''
        Before we continue, we need to check if the bin number of digits in our pow2 number
        is the same as the bin m. If it's longer, return 0.
        '''
        if use_two is True:
            if len(bin(2**low_pow)) > len(bin(m)):
                return 0
                
            
        # Do the same for the upper limit
        r = 32
        while l+1 < r:
            mid = l + (r - l) // 2
            
            if 2 ** mid <= n:
                l = mid
            else:
                r = mid - 1
        
        # We have two elements remaining, check which is valid
        if 2 ** r <= n:
            high_pow = r
        else:
            high_pow = l

        # If we found an inbetween power of 2, let's use it
        if use_two is True:
            if low_pow == high_pow:
                return 2**low_pow
            else:
                return 0
            
        # Otherwise brute force it
        else:
            bwa = m
            for num in range(m+1, n+1):
                bwa = bwa & num
                if bwa == 0:
                    return 0
            return bwa
