while True:
    aumento, exp = map(int, (input().split()))

    if aumento == 0 and exp == 0:
        break

    print(aumento*exp)
