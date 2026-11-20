"""Recover the central lattice cell by accumulating four corner distance readings."""
from itertools import permutations
from pathlib import Path
import json
c=json.loads((Path(__file__).resolve().parents[2]/'voevodsky/results/esd7_explicit_analytical_census.json').read_text());vertices={v['id']:v['barycentric'] for v in c['vertices']};answers=set()
for order in permutations(range(4)):
    scores={v:0 for v in vertices}
    for i in order:
        for v,x in vertices.items():scores[v]+=sum((a-7*(j==i))**2 for j,a in enumerate(x))
    answers.add(tuple(sorted(v for v,s in scores.items() if s==min(scores.values()))))
assert len(answers)==1;w,=answers;cells=[t['id'] for t in c['tetrahedra'] if set(t['vertices'])==set(w)];assert cells==['T184'];print(w,cells,'minimum total squared distance',min(scores.values()))
