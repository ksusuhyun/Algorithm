n = int(input())
for _ in range(n):
    tc = int(input())
    nums = list(map(int, input().split()))
    nums_set = set(nums)
    cnt, ans = 0, 0
    for n in nums_set:
        n_cnt = nums.count(n)
        if n_cnt > cnt:
            cnt = n_cnt
            ans = n
        elif n_cnt == cnt and n > ans:
            ans = n
    print(f'#{tc} {ans}')