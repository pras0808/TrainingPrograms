import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    h = [int(x) for x in input_data[1:]]
    dp = [0] * N
    dp[0] = 0
    if N > 1:
        dp[1] = abs(h[1] - h[0])
    for i in range(2, N):
        jump_one = dp[i-1] + abs(h[i] - h[i-1])
        jump_two = dp[i-2] + abs(h[i] - h[i-2])
        dp[i] = min(jump_one, jump_two)
    print(dp[N-1])
if __name__ == '__main__':
    solve()
