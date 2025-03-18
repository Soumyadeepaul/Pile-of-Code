#https://www.geeksforgeeks.org/problems/power-of-2-1587115620/1

class Solution:
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self, n):
        # code here
        i=1
        value=1
        while value<=n:
            if n==value:
                return True
            value=value<<i
        return False
