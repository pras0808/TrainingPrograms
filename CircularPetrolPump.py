def find_start(petrol, dist, n):
    start = 0
    balance = 0
    deficit = 0
    for i in range(n):
        balance += petrol[i] - dist[i]
        if balance < 0:
            deficit += balance
            start = i + 1
            balance = 0
    return start if (balance + deficit) >= 0 else -1

n = int(input())
petrol = list(map(int, input().split()))
dist = list(map(int, input().split()))
print(find_start(petrol, dist, n))
