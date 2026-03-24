a = list(map(int, input().split()))

total = sum(a)
mn = min(a)
mx = max(a)

print(total - mx, total - mn)