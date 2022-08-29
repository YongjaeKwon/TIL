'''
13 12
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0
0 1 1 1 0 0 0 1 1 0 0 0
0 1 1 1 1 1 1 0 0 0 0 0
0 1 1 1 1 1 0 1 1 0 0 0
0 1 1 1 1 0 0 1 1 0 0 0
0 0 1 1 0 0 0 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
'''
def bfs():
    q = []
    # 벽에서 출발
    q.append((0,0))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    visited = [([0] * (M+2)) for _ in range(N+2)]
    cheeze = 0
    while q:
        x,y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < N+2 and 0 <= ny < M+2:
                if arr[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                    
                elif arr[nx][ny] ==1:
                    arr[nx][ny] =0
                    cheeze +=1
                    visited[nx][ny] = 1
    return cheeze


N, M = map(int,input().split())
arr = [[0]*(M+2)]+[[0] + list(map(int,input().split())) + [0] for _ in range(N)] + [[0]*(M+2)]
time = 0
result = []
while True:
    cheeze = bfs()
    result.append(cheeze)
    # 치즈가 1개도 없다면 모두 녹은것
    if cheeze == 0:
        break
    time += 1

# 다 녹기 전 단계니까 마지막은 pop
result.pop()
# 다 녹는데 걸리는 시간
print(time)
# 마지막 남아있던 치즈 개수
print(result[-1])
    