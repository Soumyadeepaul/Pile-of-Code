#https://www.geeksforgeeks.org/problems/smallest-subarray-with-sum-greater-than-x5651/1

class Solution:
    def smallestSubWithSum(self, x, arr):
        # Your code goes here 
        size=9999999
        for i in range(len(arr)):   #for starting point sliding by 1
            summation=0
            new_size=0
            for j in range(i,len(arr)):    #derive the range, and if sum>target get new value(if) and break the loop
                summation+=arr[j]
                new_size+=1
                if summation>x:
                    if size>new_size:
                        size=new_size
                    break
        return size if size!=9999999 else 0
