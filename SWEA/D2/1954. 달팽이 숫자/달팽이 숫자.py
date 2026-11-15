n = int(input())
for tc in range(n):
    num = int(input())
    num_list = [[0]*num for _ in range(num)]
    check_list = [[0]*num for _ in range(num)]
    
    nx, ny = 0, 0
    s = 1
    check_list[nx][ny] = 1
    num_list[nx][ny] = 1
    now_d = 0
    d = {0:(0,1), 1:(1,0), 2:(0,-1), 3:(-1,0)}
    while s < num*num:
        dx, dy = d[now_d]
        if 0<=nx+dx<num and 0<=ny+dy<num and check_list[nx+dx][ny+dy] != 1:
            s = s+1
            nx, ny = nx+dx, ny+dy
            check_list[nx][ny] = 1
            num_list[nx][ny] = s
        else:
            now_d = (now_d+1)%4
            
    print(f'#{tc+1}')
    for l in num_list:
        print(*l)