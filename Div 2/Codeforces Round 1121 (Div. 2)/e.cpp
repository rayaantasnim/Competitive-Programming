#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;
long long p2[3005];
int R[3005];
int F[3005][3005];
vector<int> pr[3005];

void init() {
    p2[0] = 1;
    for (int i = 1; i <= 3000; i++) {
        p2[i] = (p2[i - 1] * 2) % MOD;
    }

    for (int i = 2; i <= 3000; i++) {
        if (pr[i].empty()) {
            for (int j = i; j <= 3000; j += i) {
                pr[j].push_back(i);
            }
        }
    }

    for (int x = 1; x <= 3000; x++) {
        int y = x + 1;
        while (y <= 3000) {
            bool ok = false;
            for (int p : pr[y]) {
                if (x % p != 0) {
                    ok = true;
                    break;
                }
            }
            if (!ok) break;
            y++;
        }
        R[x] = y - 1;
    }

    for (int M = 1; M <= 3000; M++) {
        F[0][M] = 1;
        for (int m = 1; m <= 3000; m++) {
            F[m][M] = F[m - 1][M];
            if (R[m] >= M) {
                F[m][M] = max(F[m][M], m);
            }
        }
    }
}

void solve() {
    int n;
    if (!(cin >> n)) return;

    vector<int> a(n);
    vector<int> cnt(n + 1, 0);
    bool valid = true;

    for (int i = 0; i < n; i++) {
        cin >> a[i];
        if (a[i] < 1 || a[i] > n) {
            valid = false;
        } else {
            cnt[a[i]]++;
        }
    }

    if (!valid) {
        cout << -1 << "\n";
        return;
    }

    vector<int> pref(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        pref[i] = pref[i - 1] + cnt[i];
    }

    vector<int> vals;
    for (int i = 1; i <= n; i++) {
        if (cnt[i] > 0) {
            vals.push_back(i);
        }
    }

    long long ans = 0;

    for (int i = 0; i < vals.size(); i++) {
        int m = vals[i];
        long long ways = (p2[cnt[m]] - 1 + MOD) % MOD;
        ans = (ans + ways * F[m][m]) % MOD;

        for (int j = i + 1; j < vals.size(); j++) {
            int M = vals[j];
            long long ways_m = (p2[cnt[m]] - 1 + MOD) % MOD;
            long long ways_M = (p2[cnt[M]] - 1 + MOD) % MOD;
            int between = pref[M - 1] - pref[m];
            long long ways_between = p2[between];

            long long total_ways = ways_m * ways_M % MOD * ways_between % MOD;
            ans = (ans + total_ways * F[m][M]) % MOD;
        }
    }

    cout << ans << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    init();
    int t;
    if (cin >> t) {
        while (t--) {
            solve();
        }
    }
    return 0;
}
