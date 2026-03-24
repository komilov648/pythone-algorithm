import math

t = int(input())
for _ in range(t):
    A, B, C = map(int, input().split())
    
    if C <= max(A, B) and C % math.gcd(A, B) == 0:
        print("YES")
    else:
        print("NO")