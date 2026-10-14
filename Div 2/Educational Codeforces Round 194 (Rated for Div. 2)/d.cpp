#include <bits/stdc++.h>
using namespace std;

struct Interval {
    long long l, r;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int qrTNum;
    if (!(cin >> qrTNum)) return 0;
    while (qrTNum--) {
        int n;
        string s;
        cin >> n >> s;

        if (s[0] == '0' || s.find("00") != string::npos) {
            cout << -1 << "\n";
            continue;
        }

        int low = 1, high = n, ans = -1;
        
        vector<Interval> current_intervals;
        vector<Interval> nxt;
        current_intervals.reserve(2005);
        nxt.reserve(4005);

        while (low <= high) {
            int mid = (low + high) / 2;
            bool possible = true;

            current_intervals.clear();
            current_intervals.push_back({0, 0});

            for (char ch : s) {
                nxt.clear();
                
                for (const auto &pr : current_intervals) {
                    long long l = pr.l, r = pr.r;
                    if (l == r) {
                        nxt.push_back({l - mid, l - 1});
                        nxt.push_back({l + 1, l + mid});
                    } else {
                        nxt.push_back({l - mid, r + mid});
                    }
                }

                sort(nxt.begin(), nxt.end(), [](const Interval& a, const Interval& b) {
                    if (a.l != b.l) return a.l < b.l;
                    return a.r < b.r;
                });

                long long L, R;
                if (ch == '+') { L = 1; R = 2e18; }
                else if (ch == '-') { L = -2e18; R = -1; }
                else { L = 0; R = 0; }

                current_intervals.clear();
                for (const auto &inter : nxt) {
                    long long cl = max(inter.l, L);
                    long long cr = min(inter.r, R);

                    if (cl <= cr) {
                        if (!current_intervals.empty() && cl <= current_intervals.back().r + 1) {
                            current_intervals.back().r = max(current_intervals.back().r, cr);
                        } else {
                            current_intervals.push_back({cl, cr});
                        }
                    }
                }

                if (current_intervals.empty()) {
                    possible = false;
                    break;
                }
            }

            if (possible) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        cout << ans << "\n";
    }
    return 0;
}
