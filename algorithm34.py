import collections
import heapq
def network_delay_time(times, n, k):
    graph = collections.defaultdict(list)
    dist = collections.defaultdict(int)
    for u, v, w in times:
        graph[u].append((v, w))
    Q = [(0, k)]
    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))
    if len(dist) == n:
        return max(dist.values())
    return -1
times = [[3, 1, 5], [3, 2, 2], [2, 1, 2], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 1, 1]]
N = 8
K = 3
network_delay_time(times, N, K) # result = 5