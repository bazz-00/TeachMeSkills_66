def rover(n: list):
    mass = []
    if len(n) == 1:
        while n[0] != 0:
            n[0] = n[0] - 1
            mass.append(n[0])
        mass.reverse()
    elif len(n) == 2:
        while n[1] != n[0]:
            n[1] = n[1] - 1
            mass.append(n[1])
        mass.reverse()
    elif len(n) == 3:
        mass.append(n[0])
        x = n[2]
        while n[0] + x < n[1]:
            mass.append(n[0] + n[2])
            n[0] += n[2]

    return mass



n = list(map(int, input().split(',')))
for i in rover(n):
    print(i)

