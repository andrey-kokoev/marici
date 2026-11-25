"""Enumerate maps on neutron decision states induced by common continuations."""
from collections import Counter, deque
import json
from pathlib import Path

seeds = json.loads((Path(__file__).resolve().parents[1] / 'results/pne_neutron_continuation_quotient.json').read_text())
for seed in seeds:
    q = seed['q']
    identity = tuple(range(len(q)))
    seen = {identity: ''}
    queue = deque([identity])
    while queue:
        f = queue.popleft()
        for i, letter in enumerate('SX'):
            g = tuple(q[j]['to'][i] for j in f)
            if g not in seen:
                seen[g] = seen[f] + letter
                queue.append(g)
    ranks = Counter(len(set(f)) for f in seen)
    resets = [(f[0], w) for f, w in seen.items() if len(set(f)) == 1]
    assert ranks == {7: 2, 4: 8, 2: 9, 1: 1} and resets == [(5, 'XXX')]
print('Verified for', len(seeds), 'seeds:', sorted(ranks.items()), resets)
