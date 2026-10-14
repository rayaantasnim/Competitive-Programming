#include <iostream>
#include <vector>

using namespace std;

void solve() {
    int n, k;
    cin >> n >> k;

    if (k < n || k > 2 * n - 1) {
        cout << -1 << "\n";
        return;
    }

    vector<vector<int>> grid(n, vector<int>(n, 0));
    int val = 1;

    int shared = 2 * n - k;
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j && i < shared) {
                grid[i][j] = val++;
            }
        }
    }

    for (int i = shared; i < n; i++) {
        grid[i][0] = val++;
    }
    for (int j = shared; j < n; j++) {
        grid[0][j] = val++;
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 0) {
                grid[i][j] = val++;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << grid[i][j] << " ";
        }
        cout << "\n";
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
