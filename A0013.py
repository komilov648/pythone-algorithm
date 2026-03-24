s = input().strip()

mod = 0
for ch in s:
    mod = (mod * 10 + int(ch)) % 86400

h = mod // 3600
m = (mod % 3600) // 60
sec = mod % 60

print(f"{h}:{m:02d}:{sec:02d}")