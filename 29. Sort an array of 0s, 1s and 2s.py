#https://www.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1

class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        i=0  #for 0
        j=len(arr)-1  #for 2
        k=0 #for traversing
        
        while k<=j:
            #i maintaing 0's from begaining
            if arr[k]==0:
                arr[i],arr[k]=arr[k],arr[i]
                i+=1
                k+=1
            #let 1 is already in its position
            elif arr[k]==1:
                pass
                k+=1
            #j is maintaining 2 from  the end
            #k is not uodated here becox it needed to get checked once as it got swaped
            else:
                arr[j],arr[k]=arr[k],arr[j]
                j-=1
