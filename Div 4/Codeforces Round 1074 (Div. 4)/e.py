import bisect
import sys


def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return

    idx = 0
    t = int(data[idx])
    idx += 1

    out = []
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        k = int(data[idx + 2])
        idx += 3

        a = [int(x) for x in data[idx : idx + n]]
        idx += n

        b = [int(x) for x in data[idx : idx + m]]
        idx += m
        b.sort()

        s = data[idx]
        idx += 1

        first_reach_left = {}
        first_reach_right = {}

        curr = 0
        max_l = 0
        max_r = 0

        for i in range(k):
            if s[i] == "L":
                curr -= 1
            else:
                curr += 1

            if curr < 0 and -curr > max_l:
                max_l = -curr
                if max_l not in first_reach_left:
                    first_reach_left[max_l] = i + 1
            elif curr > 0 and curr > max_r:
                max_r = curr
                if max_r not in first_reach_right:
                    first_reach_right[max_r] = i + 1

        dead_time = [0] * (k + 2)

        for robot in a:
            pos = bisect.bisect_left(b, robot)
            t_left = float("inf")
            t_right = float("inf")

            if pos > 0:
                dist = robot - b[pos - 1]
                if dist in first_reach_left:
                    t_left = first_reach_left[dist]

            if pos < m:
                dist = b[pos] - robot
                if dist in first_reach_right:
                    t_right = first_reach_right[dist]

            death = min(t_left, t_right)
            if death != float("inf"):
                dead_time[death] += 1

        ans = []
        alive = n
        for i in range(1, k + 1):
            alive -= dead_time[i]
            ans.append(str(alive))

        out.append(" ".join(ans))

    print("\n".join(out))


if __name__ == "__main__":
    solve()
