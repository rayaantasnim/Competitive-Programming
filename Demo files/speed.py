import sys

# সাধারণ input() কে ফাস্টreadline দিয়ে রিপ্লেস করা
input = sys.stdin.readline

def solve():
    # ১. সিঙ্গেল ইন্টিজার ইনপুট (যেমন: অ্যারের সাইজ N)
    n = int(input())
    
    # ২. এক লাইনে স্পেস দিয়ে আলাদা করা একাধিক ইন্টিজার (যেমন: অ্যারের উপাদানগুলো)
    arr = list(map(int, input().split()))
    
    # ৩. যদি ইনপুট একটি স্ট্রিং হয় (লাইনের শেষের \n কাটার জন্য .strip() আবশ্যক)
    # s = input().strip()
    
    # --- এখানে তোমার প্রবলেমের আসল লজিক বা ক্যালকুলেশন হবে ---
    total_sum = sum(arr)
    
    # ৪. ফাস্ট প্রিন্ট ট্রিক
    print(total_sum)

def main():
    # টেস্টকেসের সংখ্যা রিড করা (যেমন: T)
    try:
        t = int(input())
        for _ in range(t):
            solve()
    except Exception:
        return

if __name__ == '__main__':
    main()
