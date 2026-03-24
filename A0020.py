import sys
input = sys.stdin.readline

MOD = 10**9 + 7
MAX = 2000

# factorial
fact = [1] * (MAX + 1)
for i in range(1, MAX + 1):
    fact[i] = fact[i-1] * i % MOD

# inverse factorial
inv_fact = [1] * (MAX + 1)
inv_fact[MAX] = pow(fact[MAX], MOD-2, MOD)
for i in range(MAX, 0, -1):
    inv_fact[i-1] = inv_fact[i] * i % MOD

def C(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n-r] % MOD


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(C(n + k - 1, k))