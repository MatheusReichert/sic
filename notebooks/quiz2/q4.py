for x in range(2, 12):
    ehPrimo = True
    for y in range(2, 12):
        if x % y == 0 and x != y:
            ehPrimo = False
            break
    print(x, "é primo") if ehPrimo else print(x, "é composto")