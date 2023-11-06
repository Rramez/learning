# this is the 9999999th try
# i love codeforces
# https://codeforces.com/gym/475813/problem/ZE
n,*choice = map(int,input().split())
choice = sorted(choice)
dp = [-1]*(n+1)
dp[0]=0
for i in range(1,n+1):
    for u in choice:
        if u>i:
            break
        if i==u or dp[i-u]:
            dp[i] = max(dp[i],dp[i-u]+1)
        else:
            dp[i] = max(dp[i],dp[i-u])
print(dp[n] if dp[n] else -1)
