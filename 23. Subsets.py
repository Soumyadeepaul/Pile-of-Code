

def subset(num):
    # Write your code here.

    def subsetFun(num,subset1,ans,i):
        if i==len(num):
            #append as list
            ans.append(list(subset1))
            #ans is list of list
            return 
            
        #Recursion
        subset1.append(num[i]) #choosing the element
        subsetFun(num,subset1,ans,i+1)
        #Backtracking
        subset1.pop() #not choosing the element
        subsetFun(num,subset1,ans,i+1)
        return ans
        
    ans=[]
    subset1=[]
    return subsetFun(num,subset1,ans,0)
    
ans=subset([1,2,3])
for i in ans:
    print(i)
