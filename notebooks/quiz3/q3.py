list = [5, 6, 3, 9, 2, 12, 3, 8, 7]
bigValue = list[1]

for x in list:
    if x > bigValue:
        bigValue = x

list.remove(bigValue)
list.append(bigValue)

print(list)