'''
1
9
1 1 3 2 0 0 0 0 0
3 2 5 2 0 0 0 0 0
2 3 3 1 0 0 0 0 0
0 0 0 0 4 5 5 3 1
1 2 5 0 3 6 4 2 1
2 3 6 0 2 1 1 4 2
0 0 0 0 4 2 3 1 1
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0

1
8
1 2 3 0 0 4 5 0 
6 7 8 0 0 0 0 0 
9 1 2 0 0 3 0 0 
4 5 6 0 0 7 0 0 
0 0 0 0 0 8 0 0 
9 1 2 3 0 4 0 0 
5 6 7 8 0 9 0 0 
0 0 0 0 0 0 0 0
'''


T = int(input())
for test_case in range(1, T+1):
    n = int(input())                  #  행렬 크기
    arr = [list(map(int,input().split())) for _ in range(n)]

    q = []
    cnt_list = []
    for i in range(n):
        count = 0   
        for j in range(n):
            if arr[i][j] != 0:
                q.append([i,j])
                count += 1 
        cnt_list.append(count)
    print(cnt_list)
    
    # new_arr = []
    # while q:
    #     a = q.pop(0)
    #     if a[0] == q[0][0] and a[1] + 1 == q[0][1]:
    #         q.pop(0)
    #     else:
            