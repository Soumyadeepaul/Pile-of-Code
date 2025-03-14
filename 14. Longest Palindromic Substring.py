#https://www.naukri.com/code360/problems/longest-palindromic-substring_758900

def longestPalinSubstring(str: str) -> str:
    # write your code here
    s=str
    maxx=s[0]
    maxxLength=1
    for i in range(len(s)-1):
        # if 2 consequetive alphabets are same, check for even length palindrome
        if s[i]==s[i+1]:
            #if previous length is less then 2
            if maxxLength<2:
                maxx=s[i:i+2]
                maxxLength=2
            #[a,b,b,c]
            # j     z
            j=i-1
            z=i+2
          ################################################
            #edge case
            while j>=0 and z<=len(s)-1:
                if s[j]==s[z]:
                    #only update when larger than previous
                    if maxxLength<z-j+1:
                        maxxLength=z-j+1
                        maxx=s[j:z+1]
                    j-=1
                    z+=1
                else:
                    break
            ################################################
        #always check for odd length
        j=i-1
        z=i+1
      ###################################################
        while j>=0 and z<=len(s)-1:
            if s[j]==s[z]:
                if maxxLength<z-j+1:
                    maxxLength=z-j+1
                    maxx=s[j:z+1]
                j-=1
                z+=1
            else:
                break
      #################################################
    return maxx
