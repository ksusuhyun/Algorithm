n = int(input())
p_dict = {}
p_order = []
for _ in range(n*n):
    p = list(map(int, input().split()))
    p_dict[p[0]] = p[1:]
    p_order.append(p[0])

# arr 초기화
arr = [[0]*n for _ in range(n)]
love_arr = [[0]*n for _ in range(n)]
empty_arr = [[0]*n for _ in range(n)]

# 자 이제 이걸 모든 사람에 대해 하면 된다
for i in range(n*n):
    # arr 돌면서 love_arr, empty_arr 업데이트 및 1을 만족하는 위치 찾기
    max_num_love = 0
    max_num_love_list = []
    for x in range(n):
        for y in range(n):
            num_love = 0
            num_empty = 0
            for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                new_x, new_y = x+dx, y+dy
                if 0<=new_x<n and 0<=new_y<n:
                    if arr[new_x][new_y] in p_dict[p_order[i]]:
                        num_love += 1
                    elif arr[new_x][new_y] == 0:
                        num_empty += 1
            love_arr[x][y] = num_love
            empty_arr[x][y] = num_empty

            if max_num_love == num_love and arr[x][y] == 0:
                max_num_love_list.append((x,y))
            elif max_num_love < num_love and arr[x][y] == 0:
                max_num_love_list = []
                max_num_love_list.append((x,y))
                max_num_love = num_love

    # max_num_love_list 돌면서
    # 빈칸이 가장 많은 칸 찾기
    max_num_empty = 0
    max_num_empty_list = []
    for x, y in max_num_love_list:
        if max_num_empty == empty_arr[x][y]:
            max_num_empty_list.append((x,y))
        elif max_num_empty < empty_arr[x][y]:
            max_num_empty_list = []
            max_num_empty_list.append((x,y))
            max_num_empty = empty_arr[x][y]

    # 람다함수로 정렬
    sorted_final_list = sorted(max_num_empty_list, key=lambda x:(x[0], x[1]))

    final_x, final_y = sorted_final_list[0][0], sorted_final_list[0][1]
    arr[final_x][final_y] = p_order[i]

# 만족도 계산
ans = 0
for x in range(n):
    for y in range(n):
        cnt = 0
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            new_x, new_y = x+dx, y+dy
            if 0<=new_x<n and 0<=new_y<n:
                if arr[new_x][new_y] in p_dict[arr[x][y]]:
                    cnt += 1

        if cnt-1 >= 0:
            ans += 10**(cnt-1)

print(ans)