for x in range(100, 999):
    soma = 0
    vec = list(str(x))
    for y in vec:
        soma += int(y) ** 3
    if soma == x:
        print("{} é um número Armstrong, pois {}³+{}³+{}³ = {}+{}+{} = {}"
              .format(x, vec[0], vec[1], vec[2], int(vec[0]) ** 3, int(vec[1]) ** 3, int(vec[2]) ** 3, soma))