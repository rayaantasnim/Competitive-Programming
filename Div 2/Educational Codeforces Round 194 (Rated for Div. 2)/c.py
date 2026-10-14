t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    s = x + y
    
    cur = {(0, 0): (0, 0)}
    for i in range(30, -1, -1):
        sb = (s >> i) & 1
        xb = (x >> i) & 1
        nxt = {}
        
        for (l, c), (vx, nx) in cur.items():
            tot = sb + (c << 1)
            for a in range(2):
                if not l and a > xb: 
                    continue
                nl = 1 if (l or a < xb) else 0
                
                for b in range(2):
                    nc = tot - a - b
                    if nc == 0 or nc == 1:
                        nv = (vx << 1) | (a ^ b)
                        nn = (nx << 1) | a
                        k = (nl, nc)
                        if k not in nxt or (nv, nn) > nxt[k]:
                            nxt[k] = (nv, nn)
        cur = nxt
        
    best_xor, best_x = -1, -1
    for (l, c), (vx, nx) in cur.items():
        if c == 0:
            if vx > best_xor or (vx == best_xor and nx > best_x):
                best_xor, best_x = vx, nx
                
    print(best_xor, x - best_x)
