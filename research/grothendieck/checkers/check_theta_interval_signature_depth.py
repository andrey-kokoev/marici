"""Exact ranks of ordered interval tensors; no numerical theta integration."""
from itertools import permutations, combinations, product
from math import prod
from pathlib import Path
import json
import sympy as sp

primes = (2,3,5,7)
labels = {m:2*prod(primes[j] for j in range(4) if m>>j & 1) for m in range(16)}
position = {m:i for i,m in enumerate(sorted(labels, key=labels.get))}
words = list(permutations(range(4)))
rows = {k:{} for k in range(1,5)}
for col, word in enumerate(words):
    mask = 0
    intervals = []
    for j in word:
        target = mask | 1 << j
        intervals.append(range(position[mask], position[target]))
        mask = target
    for degree in rows:
        for indices in combinations(range(4), degree):
            for key in product(*(intervals[i] for i in indices)):
                rows[degree].setdefault(key, [0]*24)[col] += 1
matrices = {k:sp.Matrix(list(r.values())) for k,r in rows.items()}
cumulative = sp.ones(1,24)
ranks, cumulative_ranks = {}, {}
for k,m in matrices.items():
    ranks[k] = m.rank()
    cumulative = cumulative.col_join(m)
    cumulative_ranks[k] = cumulative.rank()
# A four-factor selector per route: choose the last atom of its first three
# edges and the first atom of its last edge. Rank selection is also certified.
m = matrices[4]
_, selected = m.T.rref()
minor = m[list(selected), :]
assert minor.shape == (24,24) and minor.det() != 0
assert minor.inv()*minor == sp.eye(24)
# Test the previously known collision at each degree, without presuming it survives.
h = sp.zeros(24,1)
for w, sign in [((0,1,2,3),1),((1,0,3,2),1),((0,1,3,2),-1),((1,0,2,3),-1)]:
    h[words.index(w)] = sign
collision = {k: matrices[k]*h == sp.zeros(matrices[k].rows,1) for k in matrices}
result = {'schema':'marici.grothendieck.theta-interval-signature-depth.v1',
          'degree_ranks':ranks,'cumulative_ranks_including_unit':cumulative_ranks,
          'old_collision_annihilated':collision,
          'selected_degree_four_coordinates':[list(list(rows[4])[i]) for i in selected],
          'degree_four_minor_determinant':str(minor.det()),
          'exact_inverse_verified':True,
          'scope':'Finite interval coefficient tensors. Theta transfer conditional on recorded atom injectivity; route-conditioned tensors are additional source data.'}
p = Path(__file__).resolve().parents[1]/'results/theta-interval-signature-depth.json'
p.write_text(json.dumps(result,indent=2)+'\n', encoding='utf-8')
print(json.dumps(result,indent=2))
