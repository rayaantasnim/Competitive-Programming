#include <iostream>
#include <vector>

using namespace std;

// Global precomputed tables up to N = 400
long long MOD;
long long F[405];       // F[n] = n!
long long I[405];       // Indecomposable permutations
long long D[405][405];  // D[n][k]: partitioning n into k components weighted by F[j]
long long A[405];       // A[n]: Interval-free permutations

void precompute() {
    // 1. Compute factorials modulo P
    F[0] = 1;
    for (int i = 1; i <= 400; ++i) {
        F[i] = (F[i - 1] * i) % MOD;
    }

    // 2. Compute I[n] (indecomposable permutations) using F[n] = sum_{k=1..n} I[k] * F[n-k]
    for (int i = 1; i <= 400; ++i) {
        long long sum = 0;
        for (int k = 1; k < i; ++k) {
            sum = (sum + I[k] * F[i - k]) % MOD;
        }
        I[i] = (F[i] - sum + MOD) % MOD;
    }

    // 3. Compute D[n][k]: number of sequences of k components summing up to size n (weighted by F[j])
    D[0][0] = 1;
    for (int i = 1; i <= 400; ++i) {
        for (int k = 1; k <= i; ++k) {
            long long sum = 0;
            for (int j = 1; j <= i; ++j) {
                sum = (sum + D[i - j][k - 1] * F[j]) % MOD;
            }
            D[i][k] = sum;
        }
    }

    // 4. Compute A[n] (Interval-free permutations)
    // Base cases
    A[1] = 1;
    A[2] = 2;
    A[3] = 0;
    
    for (int i = 4; i <= 400; ++i) {
        long long sum = 0;
        for (int k = 4; k < i; ++k) {
            sum = (sum + A[k] * D[i][k]) % MOD;
        }
        // Perfect structural formula: A[i] = 2*I[i] - F[i] - sum
        long long ans = (2 * I[i] - F[i] - sum) % MOD;
        A[i] = (ans + 2 * MOD) % MOD; // Shielding from negative results before modulo
    }
}

int main() {
    // Fast I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    if (cin >> t >> MOD) {
        precompute();
        while (t--) {
            int n;
            cin >> n;
            cout << A[n] << "\n";
        }
    }
    return 0;
}
