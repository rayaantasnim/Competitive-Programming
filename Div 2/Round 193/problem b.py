import sys

_input = sys.stdin.read().split()
if _input:
    TestsNumT = int(_input[0])
    _idx = 1
    for _ in range(TestsNumT):
        n = int(_input[_idx])
        _idx += 1
        a = []
        for _ in range(n):
            a.append(int(_input[_idx]))
            _idx += 1
        
        b = []
        for x in a:
            if not b or b[-1] != x:
                b.append(x)
                
        def ok(s):
            for i in range(len(s) - 1):
                if s[i] == s[i+1]:
                    return False
            return True
            
        def fix(s):
            v = []
            for i in range(len(s) - 1):
                if s[i] == s[i+1]:
                    v.append(i)
            if not v:
                return True
            if len(v) > 1:
                return False
            j = v[0]
            s[j], s[j+1] = s[j+1], s[j]
            res = ok(s)
            s[j], s[j+1] = s[j+1], s[j]
            return res

        seen = {}
        for x in a:
            seen[x] = 1
            
        found = False
        for val in seen:
            for i in range(len(b) + 1):
                new_b = b[:i] + [val] + b[i:]
                if fix(new_b):
                    found = True
                    break
            if found:
                break
                
        if found:
            print(len(b) + 1)
        else:
            print(len(b))