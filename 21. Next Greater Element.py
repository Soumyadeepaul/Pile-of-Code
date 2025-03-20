#https://www.geeksforgeeks.org/problems/next-larger-element-1587115620/1

class Solution:
    # Function to find the next greater element for each element of the array.
    def nextLargerElement(self, arr):
        # code here
        result=[]
        #stack is maintained for next largest element
        stack=[]
        for i in range(len(arr)-1,-1,-1):
            # for 3  [5,6,2,1]
            #pop 1,2.... 6 in next largest... append 2 in stack
            # 1, 2 will not be required further
            while stack and stack[-1]<=arr[i]:
                stack.pop()
            if len(stack)==0:
                result.insert(0,-1)
            else:
                result.insert(0,stack[-1])
            stack.append(arr[i])
        return result
