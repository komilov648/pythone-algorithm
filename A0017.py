import math

t = int(input())
for _ in range(t):
    n = int(input())
    
    if n % 2 == 1:
        print(0)
        continue
    
    m = n // 2
    
    cnt = 0
    for i in range(1, int(math.sqrt(m)) + 1):
        if m % i == 0:
            cnt += 1
            if i != m // i:
                cnt += 1
    
    print(cnt)