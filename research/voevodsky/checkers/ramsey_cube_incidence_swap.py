"""Replay a path-independent incidence transposition that fails the empty-support test."""
from itertools import combinations, product
from math import comb
import json
from pathlib import Path


def check(w):
    m = w // 2
    corners = ((1, 4, 7), (1, 5, 7))
    incident = [[], []]
    for t in combinations(range(1, w), 3):
        if min(t[1]-t[0], t[2]-t[1]) < 3:
            continue
        for i, s in enumerate(corners):
            if all(v-u in (0, 1) for u, v in zip(t, s)):
                incident[i].append(t)
    assert incident == [[(1, 4, 7)], [(1, 4, 7)]]
    dom = [sum((b << j) for j, b in enumerate(bs)) for bs in product(range(2), repeat=w) if not any(a and b for a, b in zip(bs,bs[1:]))]
    # Generate maximum independent sets directly, not from the cut classifier.
    top = [u for u in dom if u.bit_count() == m]
    counts = [sum(all((t|sum(1<<(v-1) for v in s)) & u for u in top) for t in dom) for s in corners]
    assert counts == [len(dom),len(dom)-(1<<m)]
    return dict(width=w,cubes=comb(w-5,3),incident=incident,continuations=counts)

if __name__=='__main__':
    rows=[check(w) for w in range(8,17,2)]
    print([(r['width'],r['continuations']) for r in rows]);(Path(__file__).resolve().parents[1]/'results'/'ramsey_cube_incidence_swap.json').write_text(json.dumps(rows,indent=1)+'\n')
