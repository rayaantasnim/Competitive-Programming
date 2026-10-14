#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solve() {
    int n;
    cin >> n;
    vector<int> a(n + 1);
    for (int k = 1; k <= n; ++k) {
        cin >> a[k];
    }

    // forbidden[i] will store the number of times element i is forbidden.
    // We use a difference array approach for efficient range updates.
    vector<int> diff(n + 2, 0);

    for (int k = 1; k <= n; ++k) {
        long long start = (long long)a[k] * k;
        long long end = (long long)(a[k] + 1) * k - 1;

        if (start < n) {
            int l = start;
            int r = min((long long)n - 1, end);
            diff[l]++;
            diff[r + 1]--;
        }
    }

    vector<int> B;
    int current_forbidden = 0;
    for (int i = 0; i < n; ++i) {
        current_forbidden += diff[i];
        if (current_forbidden == 0) {
            B.push_back(i);
        }
    }

    // Output results
    cout << B.size() << "\n";
    for (int i = 0; i < B.size(); ++i) {
        cout << B[i] << (i + 1 == B.size() ? "" : " ");
    }
    cout << "\n";
}

int main() {
    // Optimize standard I/O operations for performance
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}
