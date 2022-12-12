def treemaker(part_list):
    lst1 = part_list
    while len(lst1) > 1:
        for i in lst1:
            a = []
            if type(i[1]) == float:
                for j in lst1:
                    if type(j[1]) == float:
                        pass
                    else:
                        for s in range(1, len(j)):
                            if i[0] == j[s][1]:
                                iin = lst1.index(i)
                                jin = lst1.index(j)
                                lst1[jin].insert(s+1, i)
                                lst1[jin][s+1][0] = lst1[jin][s]
                                lst1[jin].remove(lst1[jin][s])
                                lst1.remove(lst1[iin])
            else:
                for s in range(1, len(i)):
                    for j in lst1:
                        if i[s][1] == j[0]:
                            a.append("var")
                        else:
                            a.append("yok")
                if "var" in a:
                    pass
                if "var" not in a:
                    for j in lst1:
                        if type(j[1]) == float:
                            pass
                        else:
                            for s in range(1, len(j)):
                                if j[s][1] == i[0]:
                                    jin = lst1.index(j)
                                    iin = lst1.index(i)
                                    lst1[jin].insert(s+1, i)
                                    lst1[jin][s+1][0] = lst1[jin][s]
                                    lst1[jin].remove(lst1[jin][s])
                                    lst1.remove(lst1[iin])
    lst1 = lst1[0]
    lst1[0] = (1, lst1[0])
    return lst1


def calculate_price(part_list):
    c = treemaker(part_list)

    def solver(x):
        if len(x) == 0:
            return 0
        if len(x) == 2:
            if type(x[1]) == float:
                return x[0][0]*x[1]
        if type(x[0]) == tuple:
            return x[0][0] * (solver(x[1]) + solver(x[2:]))
        else:
            return solver(x[0]) + solver(x[1:])
    return solver(c)


def required_parts(part_list):
    a = treemaker(part_list)

    def solver(x):
        if len(x) == 0:
            return []
        if len(x) == 1 and type(x[0]) == tuple:
            return []

        if len(x) == 2 and type(x[1]) == float:
            return [x[0]]

        if type(x[0]) == tuple:
            if type(x[1]) == float:
                return x[0]
            return solver([(x[0][0]*x[1][0][0], x[1][0][1])]+x[1][1:]) + solver([x[0]]+x[2:])

        else:
            return solver(x[0]) + solver(x[1:])
    return solver(a)


def stock_check(part_list, stock_list):
    a = required_parts(part_list)
    b = [0]*len(a)
    c = []
    d = []
    for i in range(len(a)):
        b[i] = a[i][0]
    for i in a:
        c.append(i[1])
    for i in stock_list:
        if i[1] in c:
            f = c.index(i[1])
            b[f] -= i[0]
    for i in range(len(b)):
        if b[i] > 0:
            d.append((c[i], b[i]))
    return d
