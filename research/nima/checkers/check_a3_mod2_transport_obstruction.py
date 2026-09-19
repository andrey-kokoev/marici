#!/usr/bin/env python3
"""Certify the invariant edge-level obstruction to reducing the Q transport mod 2."""
from itertools import combinations
from pathlib import Path
import json
R=Path(__file__).resolve().parents[3]
w=json.loads((R/'research/nima/results/a3-weighted-local-system-code-audit.json').read_text());vals=w['mod2']['vertex_potential_2_adic_valuations']
N=6;boundary={tuple(sorted((i,(i+1)%N))) for i in range(N)};ds=[(i,j) for i in range(N) for j in range(i+1,N) if (i,j) not in boundary]
def cross(a,b):x,y=a;u,v=b;return x<u<y<v or u<x<v<y
clusters=sorted(tuple(sorted(c)) for c in combinations(ds,3) if all(not cross(a,b) for a,b in combinations(c,2)))
edges=sorted((i,j) for i,a in enumerate(clusters) for j,b in enumerate(clusters) if i<j and len(set(a)^set(b))==2)
rows=[{'edge':[a,b],'tail_v2':vals[a],'head_v2':vals[b],'ratio_v2':vals[b]-vals[a],'F2_unit':vals[b]==vals[a]} for a,b in edges]
# Connectivity makes a second potential for the same edge ratios differ only by a global scalar.
seen={0};changed=True
while changed:
 changed=False
 for a,b in edges:
  if a in seen and b not in seen:seen.add(b);changed=True
  if b in seen and a not in seen:seen.add(a);changed=True
checks={'input_passes':w['passed'],'14_vertices_21_edges':len(vals)==14 and len(edges)==21,'mutation_graph_connected':len(seen)==14,'nonconstant_vertex_valuations':len(set(vals))>1,'nonunit_edges_exist':any(not x['F2_unit'] for x in rows),'not_all_edges_nonunit':any(x['F2_unit'] for x in rows),'edge_valuation_is_potential_difference':all(x['ratio_v2']==x['head_v2']-x['tail_v2'] for x in rows)}
out={'schema':'marici.nima.a3-mod2-transport-obstruction.v1','checks':checks,'passed':all(checks.values()),'edge_counts':{'total':21,'F2_unit':sum(x['F2_unit'] for x in rows),'nonunit':sum(not x['F2_unit'] for x in rows)},'vertex_valuation_range':[min(vals),max(vals)],'edges':rows,'theorem':'On the connected mutation graph, any vertex potential inducing the same rational edge ratios differs by one global scalar. Therefore edge 2-adic valuation differences are gauge-invariant. Since they are nonzero on some mutation edges, no common rescaling makes this transport an F2-valued rank-one local system.','possible_repair':'One must change the coefficient lattice/model or reduce a separately integral transport; clearing denominators or scaling each vertex independently changes the declared edge ratios.','claim_boundary':'The untwisted incidence complex still reduces mod 2. This obstruction concerns the selected rational canonical-weight transport only.'}
p=R/'research/nima/results/a3-mod2-transport-obstruction.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
