t = int(input())
for tc in range(1, t + 1):
    n = int(input())

bus_stop = [int(input()) for _ in range(p)]
print(f"#{tc}", end=' ')
for i in bus_stop:
    print(counts[i], end=' ')
