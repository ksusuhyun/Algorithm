t = int(input())

m_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for tc in range(t):
    s = int(input())
    ans = []
    for m in m_list:
        ans.append(s//m)
        s = s%m
    print(f'#{tc+1}')
    print(*ans)
