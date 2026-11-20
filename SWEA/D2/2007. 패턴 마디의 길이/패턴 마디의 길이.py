t = int(input())
for tc in range(t):
    s = list(input())

    now = s[0]
    next = ''
    for i in range(1, 30):
        next = next+s[i]

        for j in range(len(next)):
            if now[j] != next[j]:
                now = now+next
                next = ''
                break

        if len(now) == len(next):
            break

    print(f'#{tc+1} {len(now)}')