"""Scoped (3,7) pilot: forget the order inside a witnessed terminal swap.
A fixed labeled exterior probe tests both triangle and blue-seven avoidance.
No catalogue, threshold lookup, or graph-code input.
"""
from itertools import combinations


def legal(edges):
    e = {tuple(sorted(p)) for p in edges}
    return not any(all(p in e for p in combinations(s, 2)) for s in combinations(range(1, 10), 3)) and not any(all(p not in e for p in combinations(s, 2)) for s in combinations(range(1, 10), 7))


def main():
    sites = set(range(1, 8))
    rows = {frozenset(c) for c in combinations(sorted(sites), 3) if min(c[1]-c[0], c[2]-c[1]) >= 2}
    path = {(i, i+1) for i in range(1, 7)}
    def probes(s):
        inside = path | {(v, 8) for v in s}
        return frozenset(j for j in sites if legal(inside | {(j, 9), (8, 9)}))
    keys = {s: probes(s) for s in rows}
    assert len(rows) == 10 and all(key == sites-s for s, key in keys.items())
    cases = []
    for a,b in [(1,2),(7,6)]:
        for s in rows:
            t = s ^ {a,b}
            if a in s and t in rows:
                assert keys[s] ^ keys[t] == {a,b}
                cases.append((sorted(s), sorted(t), sorted(keys[s] ^ keys[t])))
    assert len(cases) == 6 and len(set(keys.values())) == len(rows)
    assert all(keys[frozenset(8-i for i in s)] == {8-i for i in keys[s]} for s in rows)
    print(*sorted(cases), sep='\n')

if __name__ == '__main__':
    main()
