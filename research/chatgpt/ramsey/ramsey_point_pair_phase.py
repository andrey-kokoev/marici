"""Test mutual repair directly in Hall191 point/pair coordinates."""
import json
from pathlib import Path
from itertools import combinations
from ramsey_defect_link_constructor import decode, link_defects

D = Path(__file__).parent
A = decode((D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines()[190])
moves = json.loads((D/'ramsey_block_selection_repair_rules.json').read_text())[-1]['switches']
p = json.loads((D/'ramsey_repair_cyclic_phase.json').read_text())[-1]['unique_C5_generator']
points = [1, 2]
while p[points[-1]] != 2:
    points.append(p[points[-1]])
assert set(points) == {v for v in range(22) if A[0] >> v & 1}
labels = {0:'root', **dict(zip(points,'*abcde'))}
for v in range(22):
    if v not in labels:
        labels[v] = ''.join(labels[w] for w in points if A[v] >> w & 1)
assert len(set(labels.values())) == 22

def hits(s, faults):
    return sum(any(I >> u & I >> v & 1 for u,v in s['added']) for I in faults)

def show(s):
    return [[(labels[u],labels[v]) for u,v in s[k]] for k in ('removed','added')]

if __name__ == '__main__':
    templates = json.loads((D/'ramsey_phase_compatibility_templates.json').read_text())['templates']
    orbit = {t['orbit']:t['candidate_indices_in_phase_order'] for t in templates}
    b = moves[orbit[6][0]]
    bs,_ = link_defects(A,[b]); print('B0',show(b),'defect',[[labels[v] for v in range(22) if I>>v&1] for I in bs])
    for j,idx in enumerate(orbit[14]):
        c = moves[idx]; cs,_ = link_defects(A,[c]); print(j,show(c),'overlap',bool(b['support']&c['support']),'B hits',hits(b,cs),'of',len(cs),'C hits',hits(c,bs),'of',len(bs))
        if not b['support']&c['support']:
            mixed,_ = link_defects(A,[b,c]); print('mixed defects',len(mixed))
            if j==2: assert len(cs)==hits(b,cs)==6 and len(bs)==hits(c,bs)==1 and not mixed
