

def subsetSum(num):
    # Write your code here.

    def subsetSumFun(num,subset,ans,i):
        if i==len(num):
            #append as list
            ans.append(list(subset))
            #ans is list of list
            return 
            
        #Recursion
        subset.append(num[i]) #choosing the element
        subsetSumFun(num,subset,ans,i+1)
        #Backtracking
        subset.pop() #not choosing the element
        subsetSumFun(num,subset,ans,i+1)
        return ans
        
    ans=[]
    subset=[]
    return subsetSumFun(num,subset,ans,0)
    
ans=subsetSum([1,2,3])
for i in ans:
    print(i)
