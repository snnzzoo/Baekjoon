import sys
import heapq

heap = []
N = int(sys.stdin.readline())

for _ in range(N):
    n = int(sys.stdin.readline())

    if n != 0:
        heapq.heappush(heap, n)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
