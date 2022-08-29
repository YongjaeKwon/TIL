def bfs(N,M): # N 세로 / M : 가로
    visited = [[0]*M for _ in range(N)]
    q = []
    for i in range(N):
        for j in range(M):
            