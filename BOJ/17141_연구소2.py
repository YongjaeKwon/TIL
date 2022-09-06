from itertools import combinations
from collections import deque


delta = [(-1,0),(0,1),(1,0),(-1,0)]
#bfs 정의하기
def bfs(virus_M):
    global wall
    visited = [[False]*N for _ in range(N)]
    for i,j in virus_M:
        visited[i][j] = True

    count = len(virus_M)
    time = 0
    while virus_M:
        for _ in range(len(virus_M)):
            x,y = virus_M.popleft()
            for i in range(len(delta)):
                nx, ny = x + delta[i][0], y + delta[i][1]
                # 이동하는 값이 연구소 안에 있고 벽이 아닌경우
                if 0<= nx < N and 0<= ny < N and arr[nx][ny] !=1:
                    visited[nx][ny] = True
                    virus_M.append((nx,ny))
                    count +=1
        time +=1

N,M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

# 0: 빈칸 / 1: 벽 / 2: 바이러스를 놓을 수 있는 칸


# 바이러스를 심을 수 있는 좌표 M 개 만큼의 부분집합(조합)을 구한다.
virus = []
wall = 0 
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus.append((i,j)) 
        if arr[i][j] == 1:
            wall +=1

virus_M = deque(combinations(virus, M))
for comb in combinations(virus, M):
    virus_M = deque()
    for covid in comb:
        virus_M.append(covid)

min_time = N**2
count, time = bfs(virus_M)
if count + wall == N**2:
    min_time = min(min_time, time)

if min_time == N**2:
    print(-1)
else:
    print(min_time)
