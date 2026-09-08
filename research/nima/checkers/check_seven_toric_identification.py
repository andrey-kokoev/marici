"""Integral lattice bridge from coordinate saturation to toric equality."""
import json
from pathlib import Path
from itertools import combinations
from sympy import Matrix,ZZ
from sympy.matrices.normalforms import smith_normal_form
root=Path('research/nima/results')
p=json.loads((root/'seven_point_fibers.json').read_text())
g=json.loads((root/'seven_groebner.json').read_text())
s=json.loads((root/'seven_saturation.json').read_text())
assert p['status']=='passed' and g['status']=='complete' and s['status']=='passed'
assert len(s['records'])==42 and all(r['regular_certificate'] for r in s['records'])
T=[set(tuple(e) for e in t) for t in p['triangulations']]
bd={tuple(sorted((i,(i+1)%7))) for i in range(7)}
Q=list(combinations(range(7),3))
B=Matrix([[int(all(e in t|bd for e in combinations(q,2))) for q in Q] for t in T])
R=Matrix([[a-b for a,b in zip(v,w)] for v,w in g['basis']])
assert R.shape==(63,42) and B.shape==(42,35)
assert R*B==Matrix.zeros(63,35)
def sf(M):
    d=smith_normal_form(M,domain=ZZ)
    return [abs(int(d[i,i])) for i in range(min(d.shape)) if d[i,i]]
f=sf(R);b=sf(B)
assert f==[1]*21 and len(b)==21
assert len(f)+len(b)==42
assert sf(2*R)==[2]*21 # rank alone misses this nonprimitive rival
result={'status':'passed','local_smith':f,'triangle_smith':b,'lattice_rank':21,'triangle_rank':21,'coordinate_saturation_orders':42,'nonprimitive_control_rejected':True,'conclusion':'The local exponent lattice is the full integral triangle kernel. Together with coordinate saturation this proves equality of polynomial ideals over every field.', 'scope':'Seven-point labelled ideal only; no claim of pointwise parameter surjectivity on boundary strata.'}
(root/'seven_toric_identification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
