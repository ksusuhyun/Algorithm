# 시작 위치와 m을 주면 현재 m에 해당하는 숫자의 합을 반환하는 함수
def m_sum(s, n, m):
    i, j = s[0], s[1]
    catch = 0
    for dx in range(m):
        for dy in range(m):
            nx, ny = i+dx, j+dy
            if 0<=nx<n and 0<=ny<n:
                catch += p_list[nx][ny]
    return catch

t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    p_list = []
    for _ in range(n):
        p_list.append(list(map(int, input().split())))
        
    ans = 0
    for i in range(n):
        for j in range(n):
            catch = m_sum((i,j), n, m)
            if ans < catch:
                ans = catch
            catch = 0
    print(f'#{tc+1} {ans}')