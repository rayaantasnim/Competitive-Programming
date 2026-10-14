# টোকেনাইজড ইনপুট রিডার (লাইন ব্রেক বা অতিরিক্ত স্পেসের সমস্যা এড়াতে)
tokens = []
token_ptr = 0

# প্রথম টোকেন (T) পড়া
while token_ptr >= len(tokens):
    try:
        line = input()
        if not line:
            continue
        tokens = line.split()
        token_ptr = 0
    except EOFError:
        break

if token_ptr < len(tokens):
    t = int(tokens[token_ptr])
    token_ptr += 1
    
    for _ in range(t):
        # N পড়া
        while token_ptr >= len(tokens):
            tokens = input().split()
            token_ptr = 0
        n = int(tokens[token_ptr])
        token_ptr += 1
        
        # অ্যারের উপাদানগুলো পড়া
        a = []
        freq = {}
        for i in range(n):
            while token_ptr >= len(tokens):
                tokens = input().split()
                token_ptr = 0
            val = int(tokens[token_ptr])
            token_ptr += 1
            a.append(val)
            
            if val not in freq:
                freq[val] = []
            freq[val].append(i)
            
        # সংশোধন: যদি ০ উপাদানটি অ্যারেতে ২ বারের কম থাকে, তবে উত্তর নিশ্চিত NO
        if 0 not in freq or len(freq[0]) < 2:
            print("NO")
            continue
            
        # ০ কমপক্ষে ২ বার থাকলে উত্তর নিশ্চিত YES
        k = 0
        while k in freq and len(freq[k]) >= 2:
            k += 1
            
        ans = ['C'] * n
        
        # ০ থেকে k-1 পর্যন্ত সংখ্যা বন্টন
        for v in range(k):
            indices = freq[v]
            ans[indices] = 'A'
            for idx in indices[1:]:
                ans[idx] = 'B'
                
        print("YES")
        print("".join(ans))
