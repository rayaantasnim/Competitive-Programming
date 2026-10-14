#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 1000000007;

void solve() {
    int n;
    cin >> n;
    
    vector<int> a(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
    }
    
    // ১. নিষিদ্ধ (Forbidden) উপাদানগুলো সঠিকভাবে রেঞ্জ ধরে চিহ্নিত করা
    vector<bool> forbidden(n + 1, false);
    for (int k = 1; k <= n; k++) {
        long long start = (long long)a[k] * k;
        long long end = (long long)(a[k] + 1) * k - 1;
        
        // n এর সীমা পর্যন্ত সমস্ত উপাদান নিষিদ্ধ মার্ক করব
        if (start <= n) {
            long long lim = min(end, (long long)n);
            for (long long i = start; i <= lim; i++) {
                forbidden[i] = true;
            }
        }
    }
    
    // ২. বৈধ (Allowed) উপাদানগুলোর তালিকা তৈরি করা (০ থেকে n-1 পর্যন্ত)
    vector<int> allowed;
    for (int i = 0; i < n; i++) {
        if (!forbidden[i]) {
            allowed.push_back(i);
        }
    }
    
    int m = allowed.size();
    
    // ৩. বাধ্যতামূলক ইন্টারভ্যাল ট্র্যাকিং (১-বেসড ইনডেক্সিং এর জন্য m + 2 সাইজ)
    vector<int> max_l_at_r(m + 2, 0);
    
    for (int k = 1; k <= n; k++) {
        for (int v = 0; v < a[k]; v++) {
            long long L_val = (long long)v * k;
            long long R_val = (long long)(v + 1) * k - 1;
            
            // binary search দিয়ে allowed এর ইনডেক্স রেঞ্জ বের করা (1-based index)
            auto it1 = lower_bound(allowed.begin(), allowed.end(), L_val);
            auto it2 = upper_bound(allowed.begin(), allowed.end(), R_val);
            
            int l_idx = distance(allowed.begin(), it1) + 1;
            int r_idx = distance(allowed.begin(), it2); 
            
            if (l_idx > r_idx) {
                // কোনো বাধ্যতামূলক ইন্টারভ্যালে বৈধ উপাদান না থাকলে সেট গঠন অসম্ভব
                cout << 0 << "\n";
                return;
            }
            
            // ডান সীমানা r_idx এ শেষ হওয়া ইন্টারভ্যালের সর্বোচ্চ বাম সীমানা ট্র্যাক করা
            max_l_at_r[r_idx] = max(max_l_at_r[r_idx], l_idx);
        }
    }
    
    // ৪. L_need[j] বের করা (j এর বামে শেষ হওয়া সব ইন্টারভ্যালের সর্বোচ্চ বাম সীমানা)
    vector<int> L_need(m + 2, 0);
    int current_max_l = 0;
    for (int j = 1; j <= m + 1; j++) {
        current_max_l = max(current_max_l, max_l_at_r[j - 1]);
        L_need[j] = current_max_l;
    }
    
    // ৫. DP এবং Prefix Sum দিয়ে দ্রুত সাবসেট গণনা করা
    vector<long long> dp(m + 2, 0);
    vector<long long> pref_sum(m + 3, 0);
    
    // বেস কেস সঠিকভাবে সেট করা
    dp[0] = 1;
    pref_sum[1] = 1;
    
    for (int j = 1; j <= m; j++) {
        int left = L_need[j];
        int right = j - 1;
        
        if (left <= right) {
            dp[j] = (pref_sum[right + 1] - pref_sum[left] + MOD) % MOD;
        } else {
            // যদি কোনো আগের বাধ্যবাধকতা ভেঙে যায় তবে কারেন্ট ডিপি ০ হবে না, এটি পূর্ববর্তী ভ্যালিড ডিপি ক্যারি করতে পারে
            if (left == 0) dp[j] = dp[0]; 
            else dp[j] = 0;
        }
        
        // প্রতিটি উপাদানের স্বাধীন চয়েসের জন্য ২ দিয়ে গুণ হবে (কারণ এটি ফ্রি উপাদান হতে পারে)
        dp[j] = (dp[j] * 2) % MOD;
        
        pref_sum[j + 1] = (pref_sum[j] + dp[j]) % MOD;
    }
    
    // শেষ উপাদানের পর সমস্ত ইন্টারভ্যাল কাভার হয়েছে কিনা তা নিশ্চিত করে উত্তর নেওয়া
    long long ans = 0;
    int target_left = L_need[m + 1];
    
    for (int j = target_left; j <= m; j++) {
        // যদি j থেকে m পর্যন্ত কোনো নতুন কন্ডিশন ব্রেক না করে, তবে ডিপি যোগ হবে
        if (L_need[m + 1] <= j) {
            ans = (ans + dp[j]) % MOD;
        }
    }
    
    // যদি কোনো এলিমেন্টই রিকোয়ার্ড না থাকে (সব ফ্রি), বেস কেস ১ যোগ হবে
    if (target_left == 0) {
        ans = (ans + dp[0]) % MOD;
    }
    
    cout << ans << "\n";
}

int main() {
    // Fast I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    
    return 0;
}
