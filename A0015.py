t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    pos = k

    # mapping
    pos = n - 1 - pos

    for i in range(1, n):
        if pos >= i:
            pos = i + (n - 1 - pos)
    
    print(pos)