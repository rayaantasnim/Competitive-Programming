import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return

    m = int(data[0])
    queries = []
    idx = 1
    for _ in range(m):
        queries.append((int(data[idx]), int(data[idx+1])))
        idx += 2

    valid_sets = []
    for x in range(24):
        valid_sets.append((25, x, 1))
        valid_sets.append((x, 25, 0))
    for x in range(26, 201):
        valid_sets.append((x, x - 2, 1))
        valid_sets.append((x - 2, x, 0))

    fifth_sets = []
    for x in range(14):
        fifth_sets.append((15, x, 1))
        fifth_sets.append((x, 15, 0))
    for x in range(16, 201):
        fifth_sets.append((x, x - 2, 1))
        fifth_sets.append((x - 2, x, 0))

    match_types = [(3, 0), (3, 1), (3, 2), (2, 3), (1, 3), (0, 3)]
    
    best_match = {}
    best_history = {}

    memo = {}

    def get_match_priority(wA, wB):
        if wA == 3 and wB == 0: return 5
        if wA == 3 and wB == 1: return 4
        if wA == 3 and wB == 2: return 3
        if wA == 2 and wB == 3: return 2
        if wA == 1 and wB == 3: return 1
        if wA == 0 and wB == 3: return 0
        return -1

    states = []
    states.append((0, 0, 0, 0, 0, []))
    
    visited = set()
    visited.add((0, 0, 0, 0, 0))

    head = 0
    while head < len(states):
        sets_played, wA, wB, sA, sB, history = states[head]
        head += 1

        if wA == 3 or wB == 3:
            curr_prio = get_match_priority(wA, wB)
            point_pair = (sA, sB)
            if point_pair not in best_match or curr_prio > best_match[point_pair]:
                best_match[point_pair] = curr_prio
                best_history[point_pair] = (wA, wB, history)
            continue

        if sA > 200 or sB > 200:
            continue

        current_choices = fifth_sets if sets_played == 4 else valid_sets
        for pA, pB, wins_A in current_choices:
            nsA = sA + pA
            nsB = sB + pB
            if nsA <= 200 and nsB <= 200:
                nwA = wA + wins_A
                nwB = wB + (1 - wins_A)
                n_state_key = (sets_played + 1, nwA, nwB, nsA, nsB)
                if n_state_key not in visited:
                    visited.add(n_state_key)
                    states.append((sets_played + 1, nwA, nwB, nsA, nsB, history + [(pA, pB)]))

    out = []
    for a, b in queries:
        if (a, b) in best_history:
            wA, wB, history = best_history[(a, b)]
            out.append(f"{wA}:{wB}")
            set_scores = [f"{pA}:{pB}" for pA, pB in history]
            out.append(" ".join(set_scores))
        else:
            out.append("Impossible")

    print("\n".join(out))

if __name__ == '__main__':
    solve()
