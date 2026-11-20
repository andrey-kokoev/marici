"""Three middle-band tests on opposite-edge depths; no colour or convolution assumption."""
import json
from itertools import permutations
from pathlib import Path
c=json.loads((Path(__file__).resolve().parents[2]/'voevodsky/results/esd7_explicit_analytical_census.json').read_text());vs={v['id']:v['barycentric'] for v in c['vertices']};ts={t['id']:set(t['vertices']) for t in c['tetrahedra']}
for order in permutations((1,2,3)):
    s=set(vs);counts=[]
    for j in order:
        s={v for v in s if vs[v][0]+vs[v][j] in (3,4)};cells=[t for t,x in ts.items() if x<=s];counts.append((len(s),len(cells)))
    assert cells==['T184'] and len(s)==4;print(order,counts)
