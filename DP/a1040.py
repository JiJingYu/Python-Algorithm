def manacher(s):
    s='#'+"#".join(s)+"#"
    max_right = 0
    pos = 0
    max_len = 1
    RL = [1]*len(s)
    for i in range(len(s)):
        if i<max_right:
            RL[i]=min(RL[2*pos-i], max_right-i)
        while i-RL[i]>=0 and i+RL[i]<len(s) and s[i-RL[i]]==s[i+RL[i]]:
            RL[i]+=1
        if i+RL[i]-1>max_right:
            max_right,pos = i+RL[i]-1, i
        max_len = max(max_len, RL[i])
    return max_len-1
print()