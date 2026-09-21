"""Minimal fourth-degree completion of the second-degree interval observer."""
from itertools import permutations
from pathlib import Path
import importlib.util
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location('theta_signature', ROOT/'research/grothendieck/theta_interval_signature.py')
t = importlib.util.module_from_spec(spec)
spec.loader.exec_module(t)
words = list(permutations(range(4)))
observations = [t.observe_route(w) for w in words]
keys2 = sorted(set().union(*(set(o[2]) for o in observations)))
keys4 = sorted(set().union(*(set(o[4]) for o in observations)))
def matrix(degree, keys):
    return sp.Matrix([[o[degree].get(key, 0) for o in observations] for key in keys])
m2, m4 = matrix(2, keys2), matrix(4, keys4)
_, piv2 = m2.T.rref()
base = m2[list(piv2), :]
assert base.rows == 18
_, piv = base.col_join(m4).T.rref()
assert tuple(piv[:18]) == tuple(range(18))
selected4 = [i-18 for i in piv[18:]]
assert len(selected4) == 6
m = base.col_join(m4[selected4, :])
inverse = m.inv()
assert inverse*m == sp.eye(24)
# Every admissible route and every cut, including paths starting above the root.
count = 0
for start in range(16):
    unused = [j for j in range(4) if not start & (1 << j)]
    for length in range(len(unused)+1):
        for word in permutations(unused, length):
            full = t.observe_route(word, start)
            for cut in range(length+1):
                mask = start
                for j in word[:cut]: mask |= 1 << j
                assert t.concatenate(t.observe_route(word[:cut], start),
                                     t.observe_route(word[cut:], mask)) == full
            count += 1
assert count == 168
# Signed mixture is linear, and its recovered coefficient vector is exact.
weights = [sp.Rational((i%7)-3, i+1) for i in range(24)]
mixed = t.observe_mixture([(w,0,p) for w,p in zip(weights,words)])
selected_keys2 = [keys2[i] for i in piv2]
selected_keys4 = [keys4[i] for i in selected4]
readout = sp.Matrix([mixed[2].get(k,0) for k in selected_keys2]
                    +[mixed[4].get(k,0) for k in selected_keys4])
assert inverse*readout == sp.Matrix(weights)
# Composition of linear mixtures requires carrying the degree-zero mass.
x = t.observe_mixture([(2,0,(0,1)),(-1,0,(1,0))])
y = t.observe_mixture([(3,3,(2,3)),(4,3,(3,2))])
expected = t.observe_mixture([(6,0,(0,1,2,3)),(8,0,(0,1,3,2)),
                             (-3,0,(1,0,2,3)),(-4,0,(1,0,3,2))])
assert t.concatenate(x,y) == expected
try: t.observe_route((0,0))
except ValueError: pass
else: raise AssertionError('invalid route accepted')
result = {'schema':'marici.grothendieck.minimal-theta-four-point-completion.v1',
          'passed': True, 'paths_checked':count,
          'second_degree_rank':18,'added_fourth_degree_coordinates':6,
          'second_degree_coordinates':selected_keys2,
          'fourth_degree_coordinates':selected_keys4,
          'determinant':str(m.det()),
          'inverse_matrix':[[str(x) for x in inverse.row(i)] for i in range(24)],
          'route_order':[list(w) for w in words],
          'checks':{'exact_inverse':True,'all_path_cuts':True,
                    'signed_mixture_reconstruction':True,'bilinear_mixture_composition':True,
                    'invalid_route_rejected':True},
          'scope':'Finite pre-aggregation interval signature; no physical source segmentation or theta Gram conditioning certificate.'}
path = ROOT/'research/grothendieck/results/minimal-theta-four-point-completion.json'
path.write_text(json.dumps(result,indent=2)+'\n', encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ('inverse_matrix','route_order')},indent=2))
