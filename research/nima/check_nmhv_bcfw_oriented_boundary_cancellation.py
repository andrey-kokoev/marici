#!/usr/bin/env python3
"""Oriented boundary cancellation for NMHV BCFW five-bracket cells."""
import json
from collections import defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def canonical_with_sign(q):
 inv=sum(q[i]>q[j] for i in range(len(q)) for j in range(i+1,len(q)))
 return tuple(sorted(q)),(-1)**inv
def physical(q,n):
 S=set(q);adj=[{i,i%n+1} for i in range(1,n+1)]
 return any(a<=S and b<=S and a.isdisjoint(b) for a in adj for b in adj)
rows=[];passed=True
for n in range(6,51):
 cells=tuple((n,i-1,i,j-1,j) for i in range(2,n-1) for j in range(i+2,n));boundary=defaultdict(list)
 for cell in cells:
  for omitted in range(5):
   facet=cell[:omitted]+cell[omitted+1:];key,perm=canonical_with_sign(facet)
   boundary[key].append(((-1)**omitted)*perm)
 phys={q:v for q,v in boundary.items() if physical(q,n)};spur={q:v for q,v in boundary.items() if not physical(q,n)}
 checks={'physical_facets_have_unit_oriented_coefficient':all(len(v)==1 and abs(sum(v))==1 for v in phys.values()),'spurious_facets_cancel_with_opposite_orientations':all(len(v)==2 and sorted(v)==[-1,1] and sum(v)==0 for v in spur.values()),'oriented_boundary_contains_only_physical_facets':all(sum(v)==0 for v in spur.values()) and all(sum(v)!=0 for v in phys.values())}
 ok=all(checks.values());passed &= ok;rows.append({'multiplicity':n,'cells':len(cells),'physical_facets':len(phys),'cancelled_internal_facets':len(spur),'checks':checks,'passed':ok})
out={'schema':'marici.nima.nmhv-bcfw-oriented-boundary-cancellation.v1','benchmark':{'result':'oriented cancellation of internal facets in the NMHV BCFW triangulation','context':'canonical forms of the positive Grassmannian/amplituhedron'},'orientation_convention':'Boundary of [v0 v1 v2 v3 v4] is sum_i (-1)^i [v0 ... omit vi ... v4], then facets are sorted with permutation sign.','range':{'min_multiplicity':6,'max_multiplicity':50},'results':rows,'passed':passed,'scope':'Exact oriented simplicial-chain computation for n=6,...,50; not an arbitrary-n proof.'}
p=ROOT/'research/nima/results/nmhv-bcfw-oriented-boundary-cancellation.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':passed,'range':[6,50],'last':rows[-1]},indent=2));raise SystemExit(0 if passed else 1)
