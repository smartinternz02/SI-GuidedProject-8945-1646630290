def solve(n):
    if not n:
        return
    return solve(n-1)

for i in range (9):
    solve(2)