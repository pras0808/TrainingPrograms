def searchMatrix(mat, n, m, x):
    row = 0
    col = m - 1
    while row < n and col >= 0:
        if mat[row][col] == x:
            return 1
        elif mat[row][col] > x:
            col -= 1
        else:
            row += 1
    return 0

n, m = map(int, input("Enter rows and columns: ").split())
mat = []
print("Enter matrix:")
for _ in range(n):
    mat.append(list(map(int, input().split())))
x = int(input("Enter X: "))
print(searchMatrix(mat, n, m, x))
