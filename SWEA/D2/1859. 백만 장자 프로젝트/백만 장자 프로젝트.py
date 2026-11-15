n_test = int(input())
for tc in range(n_test):
    n_len = int(input())
    num_list = list(map(int, input().split()))
    
    s, ans = 0, 0
    while s < n_len:
        idx_max = s
        for i in range(s+1, n_len):
            if num_list[i] > num_list[idx_max]:
                idx_max = i
        for j in range(s, idx_max):
            ans += num_list[idx_max] - num_list[j]
        s = idx_max+1
    print(f"#{tc+1} {ans}")