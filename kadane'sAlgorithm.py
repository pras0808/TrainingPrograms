def max_sum_submatrix(mat, R, C):
    max_sum = float('-inf')
    for left in range(C):
        temp = [0] * R
        for right in range(left, C):
            for i in range(R):
                temp[i] += mat[i][right]
            curr = temp[0]
            best = temp[0]
            for i in range(1, R):
                curr = max(temp[i], curr + temp[i])
                best = max(best, curr)
            max_sum = max(max_sum, best)
    return max_sum

R, C = map(int, input().split())
mat = []
for _ in range(R):
    mat.append(list(map(int, input().split())))
print(max_sum_submatrix(mat, R, C))
