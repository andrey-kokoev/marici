#!/usr/bin/env python3
"""Oriented facet incidence of the certified seven-point parity cellulation."""
import collections,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];src=json.loads((ROOT/'research/nima/results/seven-point-history-parity-cell-matching.json').read_text());cells=[tuple(m['simplex']) for m in sorted(src['matches'],key=lambda x:x['history_index'])];facets=collections.defaultdict(list)
for ci,C in enumerate(cells):
 for r in range(5):facets[C[:r]+C[r+1:]].append((ci,1 if r%2==0 else -1))
internal={f:v for f,v in facets.items() if len(v)==2};exterior={f:v for f,v in facets.items() if len(v)==1};bad={f:v for f,v in facets.items() if len(v)>2}
# Choose cell orientation signs so every shared facet cancels.
signs={0:1};queue=[0];consistent=True
adj=[]
while queue:
 a=queue.pop(0)
 for f,inc in internal.items():
  ids=[x[0] for x in inc]
  if a not in ids:continue
  ia=ids.index(a);b=ids[1-ia];sa=inc[ia][1];sb=inc[1-ia][1];required=-signs[a]*sa*sb
  adj.append((a,b,f))
  if b in signs and signs[b]!=required:consistent=False
  elif b not in signs:signs[b]=required;queue.append(b)
residual={f:sum(signs.get(ci,0)*sgn for ci,sgn in inc) for f,inc in internal.items()};checks={'six_certified_cells':len(cells)==6,'all_facets_manifold_like':not bad,'orientation_extends_to_all_cells':len(signs)==6 and consistent,'all_internal_facets_cancel':all(v==0 for v in residual.values()),'exterior_boundary_nonempty':len(exterior)>0}
out={'schema':'marici.nima.seven-point-cellulation-incidence.v1','cells':[list(c) for c in cells],'cell_orientation_signs':signs,'internal_facets':[{'labels':list(f),'incidences':v} for f,v in internal.items()],'exterior_facets':[list(f) for f in exterior],'adjacency_edges':sorted({tuple(sorted((a,b))) for a,b,f in adj}),'counts':{'cells':len(cells),'internal_facets':len(internal),'exterior_facets':len(exterior)},'checks':checks,'passed':all(checks.values()),'meaning':'Internal canonical-form residues cancel by oriented facet incidence; exterior facets carry the physical boundary.'};p=ROOT/'research/nima/results/seven-point-cellulation-incidence.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
