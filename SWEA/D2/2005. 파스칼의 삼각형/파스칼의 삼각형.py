t = int(input())

for tc in range(t):
    n = int(input())

    if n == 1:
        ans = [[0,1,0]]
    else:
        ans = [[0,1,0]]
        for i in range(1, n):
            f_i = i-1
            ans_i = []
            for j in range(len(ans[f_i])-1):
                ans_i.append(ans[f_i][j]+ans[f_i][j+1])
            ans.append([0]+ans_i+[0])
	
    print(f'#{tc+1}')
    for row in ans:
        print(*row[1:-1])