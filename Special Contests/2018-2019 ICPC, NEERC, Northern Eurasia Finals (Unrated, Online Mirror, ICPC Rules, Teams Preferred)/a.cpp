#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Structure to hold reconstruction details for each DP state
struct State {
    bool reachable = false;
    short prev_a = 0;
    short prev_b = 0;
    short score_a = 0;
    short score_b = 0;
};

// Global DP table: dp[sets_a][sets_b][points_a][points_b]
State dp[4][4][201][201];

struct Score {
    int a, b;
};

void precompute() {
    // Generate valid point scores for sets 1-4
    vector<Score> normal_A_wins, normal_B_wins;
    for (int y = 0; y <= 23; ++y) {
        normal_A_wins.push_back({25, y});
        normal_B_wins.push_back({y, 25});
    }
    for (int x = 26; x <= 200; ++x) {
        normal_A_wins.push_back({x, x - 2});
        normal_B_wins.push_back({x - 2, x});
    }

    // Generate valid point scores for set 5
    vector<Score> fifth_A_wins, fifth_B_wins;
    for (int y = 0; y <= 13; ++y) {
        fifth_A_wins.push_back({15, y});
        fifth_B_wins.push_back({y, 15});
    }
    for (int x = 16; x <= 200; ++x) {
        fifth_A_wins.push_back({x, x - 2});
        fifth_B_wins.push_back({x - 2, x});
    }

    // Base Case
    dp[0][0][0][0].reachable = true;

    // Ordered sequence of layers by non-terminal set configurations
    vector<vector<pair<int, int>>> layers = {
        {{0, 0}},
        {{1, 0}, {0, 1}},
        {{2, 0}, {1, 1}, {0, 2}},
        {{2, 1}, {1, 2}}, // 3:0 and 0:3 are terminal, so they are excluded from transitioning forward
        {{2, 2}}         // 3:1 and 1:3 are terminal, so they are excluded
    };

    for (int layer = 0; layer < 5; ++layer) {
        for (auto& p : layers[layer]) {
            int sa = p.first;
            int sb = p.second;
            bool is_fifth = (sa + sb == 4);

            const auto& a_wins = is_fifth ? fifth_A_wins : normal_A_wins;
            const auto& b_wins = is_fifth ? fifth_B_wins : normal_B_wins;

            for (int pa = 0; pa <= 200; ++pa) {
                for (int pb = 0; pb <= 200; ++pb) {
                    if (!dp[sa][sb][pa][pb].reachable) continue;

                    // Transition 1: A wins the next set
                    if (sa + 1 <= 3) {
                        for (const auto& score : a_wins) {
                            int npa = pa + score.a;
                            int npb = pb + score.b;
                            if (npa <= 200 && npb <= 200) {
                                if (!dp[sa + 1][sb][npa][npb].reachable) {
                                    dp[sa + 1][sb][npa][npb].reachable = true;
                                    dp[sa + 1][sb][npa][npb].prev_a = pa;
                                    dp[sa + 1][sb][npa][npb].prev_b = pb;
                                    dp[sa + 1][sb][npa][npb].score_a = score.a;
                                    dp[sa + 1][sb][npa][npb].score_b = score.b;
                                }
                            }
                        }
                    }

                    // Transition 2: B wins the next set
                    if (sb + 1 <= 3) {
                        for (const auto& score : b_wins) {
                            int npa = pa + score.a;
                            int npb = pb + score.b;
                            if (npa <= 200 && npb <= 200) {
                                if (!dp[sa][sb + 1][npa][npb].reachable) {
                                    dp[sa][sb + 1][npa][npb].reachable = true;
                                    dp[sa][sb + 1][npa][npb].prev_a = pa;
                                    dp[sa][sb + 1][npa][npb].prev_b = pb;
                                    dp[sa][sb + 1][npa][npb].score_a = score.a;
                                    dp[sa][sb + 1][npa][npb].score_b = score.b;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

void solve() {
    int a, b;
    cin >> a >> b;

    // Alice's optimal preference ordering (best to worst score difference)
    vector<pair<int, int>> outcomes = {
        {3, 0}, {3, 1}, {3, 2}, {2, 3}, {1, 3}, {0, 3}
    };

    for (const auto& out : outcomes) {
        int sa = out.first;
        int sb = out.second;

        if (dp[sa][sb][a][b].reachable) {
            cout << sa << ":" << sb << "\n";
            
            // Reconstruct the set sequence backwards
            vector<string> match_sets;
            int curr_sa = sa, curr_sb = sb;
            int curr_a = a, curr_b = b;

            while (curr_sa > 0 || curr_sb > 0) {
                State& s = dp[curr_sa][curr_sb][curr_a][curr_b];
                match_sets.push_back(to_string(s.score_a) + ":" + to_string(s.score_b));
                
                int next_a = s.prev_a;
                int next_b = s.prev_b;
                if (s.score_a > s.score_b) curr_sa--;
                else curr_sb--;
                
                curr_a = next_a;
                curr_b = next_b;
            }

            // Print sets in forward chronological order
            reverse(match_sets.begin(), match_sets.end());
            for (size_t i = 0; i < match_sets.size(); ++i) {
                cout << match_sets[i] << (i + 1 == match_sets.size() ? "" : " ");
            }
            cout << "\n";
            return;
        }
    }

    cout << "Impossible\n";
}

int main() {
    // Fast I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    precompute();

    int m;
    if (cin >> m) {
        while (m--) {
            solve();
        }
    }
    return 0;
}
