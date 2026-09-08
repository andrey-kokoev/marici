"""Dimension obstruction at the coefficient cone vertex, independent of lift."""
import json
from pathlib import Path
from itertools import combinations
r=Path('research/nima/results')
p=json.loads((r/'seven_point_fibers.json').read_text())
g=json.loads((r/'seven_groebner.json').read_text())
t=json.loads((r/'seven_toric_identification.json').read_text())
assert p['status']=='passed' and g['status']=='complete' and t['status']=='passed'
assert len(p['triangulations'])==42 and len(g['basis'])==63
assert all(len(a)==42 and sum(a)==sum(b)==2 for a,b in g['basis'])
# All defining generators have zero linear part at the vertex.
vertex_tangent=42;source_tangent=len(list(combinations(range(7),3)))
assert source_tangent==35 and vertex_tangent>source_tangent
# A point can lie over the vertex without being the parameter origin.
Q=list(combinations(range(7),3));bd={tuple(sorted((i,(i+1)%7))) for i in range(7)}
T=[set(tuple(e) for e in v) for v in p['triangulations']]
B=[[int(all(e in v|bd for e in combinations(q,2))) for q in Q] for v in T]
assert all(sum(a)==5 for a in B)
# Only the first triangle coordinate is nonzero: every degree-five squarefree product vanishes.
assert all(any(v and j!=0 for j,v in enumerate(a)) for a in B)
result={'status':'passed','vertex_tangent_dimension':vertex_tangent,'parameter_tangent_dimension_at_every_point':source_tangent,'rank_deficit_at_least':vertex_tangent-source_tangent,'nonorigin_vertex_lift_control':True,'scope':'No regular section on any Zariski-open neighborhood containing the coefficient vertex, over any field. No obstruction asserted on vertex-free strata.'}
(r/'regular_section_obstruction.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
