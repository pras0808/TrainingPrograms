import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    A = [int(x) for x in input_data[1:]]
    init_c1 = A.count(1)
    init_c2 = A.count(2)
    init_c3 = A.count(3)
    dp = [[[0.0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]
    for c3 in range(N + 1):
        for c2 in range(N + 1):
            for c1 in range(N + 1):
                if c1 + c2 + c3 == 0 or c1 + c2 + c3 > N:
                    continue
                total_expected = N     
                if c1 > 0:
                    total_expected += c1 * dp[c1 - 1][c2][c3]
                if c2 > 0:
                    total_expected += c2 * dp[c1 + 1][c2 - 1][c3]
                if c3 > 0:
                    total_expected += c3 * dp[c1][c2 + 1][c3 - 1]
                dp[c1][c2][c3] = total_expected / (c1 + c2 + c3)
    print(f"{dp[init_c1][init_c2][init_c3]:.14f}")

if __name__ == '__main__':
    solve()
