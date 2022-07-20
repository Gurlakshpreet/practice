def min(h):
    x = h[0]
    y = 0
    for i in range(len(h)):
        if h[i] < x:
            x = h[i]
            y = i
        if i == len(h) - 1:
            return([x, y])

def form(h):
    a = []
    b = []
    m = ""
    n = ""
    for i in range(len(h)):
        if i % 2 == 0:
            a.append(h[i])
        else:
            b.append(h[i])
    for i in range(len(a)):
        m = m + str(a[i])
    for i in range(len(b)):
        n = n + str(b[i])
    m, n = int(m), int(n)
    return(m + n)

def iden(h):
    i = 0
    o = []
    while i < len(h):
        w = min(h)
        del h[w[1]]
        o.append(w[0])
    form(o)

iden([6, 8, 4, 5, 2, 3])