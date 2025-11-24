def count():
    l = [int(item) for item in input().split(',')]
    n = int(input())
    c = 0
    for i in l:
        if i == n:
            c += 1
    print(f"{n} occurs {c} times in the list.")
count()
