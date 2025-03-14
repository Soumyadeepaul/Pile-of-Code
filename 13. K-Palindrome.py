#https://www.geeksforgeeks.org/problems/k-palindrome/1

#longest palindrome subsequence
def iskPalindrome(string, n):
    #Code here
    s=string
    dp=[[0 for _ in range(len(s))] for _ in range(len(s))]
    i=-1
    start=0
    l=len(s)
    while i<l:
        for j in range(start,len(s)):
            i+=1
            if i==j:
                dp[i][j]=1
            elif s[i]==s[j]:
                dp[i][j]=2+dp[i+1][j-1]  # 2 because new 2 alphabet get added
            else:
                dp[i][j]=max(dp[i][j-1],dp[i+1][j])
        start+=1
        i=-1
        l-=1
    val=len(string)-dp[0][len(s)-1]   #length - longest palindrome subsequence..... [val = number of alphabet to be deleted]
    if n>=val:
        return 1
    return 0
