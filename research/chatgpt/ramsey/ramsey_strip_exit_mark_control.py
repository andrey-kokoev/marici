"""Distinguish a mark-based handoff within the exit block from reflecting that mark to the next block in the constructed cycle."""
import json
from collections import Counter
from pathlib import Path
from ramsey_strip_marked_boundary_overlap import E,P,blocks

B_fan = {E.index((1, 2)), E.index((1, 3))}
def reflect(v):
    perm = {1: 1, 2: 3, 3: 2, 4: 4}
    return E.index(tuple(sorted(perm[x] for x in E[v])))

data = json.loads(Path(__file__).with_name('ramsey_strip_closure_control.json').read_text())
counts = Counter()
for case in data:
    p = case['path']
    if (p[0], p[1], p[-1]) != (0, 16, 29): continue
    d = set(P[p[-2]])
    opposite = bool(d & blocks(0)[0]); counts[opposite, case['closes']] += 1
    if opposite:
        x, = d & blocks(0)[0]; y, = d & B_fan
        assert x != y and (reflect(x), reflect(y)) == (E.index((3,4)), E.index((1,2)))
        assert reflect(x) not in d and {reflect(x),reflect(y)} == blocks(0)[1]
assert sorted(counts.values()) == [2,2,3,3];print('opposite exit, closes:', counts)
