"""Do the images of the full reachable space themselves reproduce the entry automaton? Test all reachable paired states, not just sample words."""
from collections import deque
import json
from pathlib import Path

seeds = json.loads((Path(__file__).resolve().parents[1] / 'results/pne_neutron_continuation_quotient.json').read_text())
for seed in seeds:
    q = seed['q']
    queue = deque([(0, frozenset(range(len(q))))])
    image = {}
    while queue:
        j, a = queue.popleft()
        if j in image:
            assert image[j] == a
            continue
        image[j] = a
        for i in range(2):
            queue.append((q[j]['to'][i], frozenset(q[k]['to'][i] for k in a)))
    assert len(set(image.values())) == len(image) == len(q)
    assert all(j in a for j, a in image.items())
print('Verified on', len(seeds), 'seeds')
for j,a in sorted(image.items()):
    print(q[j]['word'] or 'entry', sorted(a), q[j]['v'])
