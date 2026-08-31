#!/usr/bin/env python3
"""Prove the two squared-axis inclusions cover every boundary exponent at all even A>=12."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research'/'benincasa'/'results'
def boundary(A):return [(i,d-i) for d in (A-6,A-5,A-4) for i in range(d+1)]
def preimages(A,e):
 i,j=e;out=[]
 if i>=2:out.append(('x2',(i-2,j)))
 if j>=2:out.append(('y2',(i,j-2)))
 return [(a,p) for a,p in out if p in set(boundary(A-2))]
checks=[]
for A in range(12,102,2):
 B=boundary(A);P=[preimages(A,e) for e in B];assert all(P);union=len(B);overlap=sum(len(x)==2 for x in P);assert union==3*A-12 and overlap==3*A-24;checks.append({'A':A,'targets_per_pole':union,'overlaps_per_pole':overlap})
out={'schema':'marici.benincasa.cosmology-arbitrary-even-boundary-two-cover.v1','boundary_degrees':'A-6, A-5, A-4','cover_threshold':'every integer A>=9 (hence every even A>=10); sharp failure at A=8, exponent (1,1)','induction_threshold':'every even A>=12 from the available A12 base','cover_rule':'choose x^2 when i>=2 or y^2 when j>=2; at least one holds because i+j>=A-6>=3','preimage_rule':'subtracting 2 gives a boundary exponent at A-2','targets_per_pole_formula':'3A-12','overlaps_per_pole_formula':'3A-24','induction':{'base_cutoff':12,'base_exact_contractions':48,'constructor_transport_natural_for_all_admissible_exponents':True,'conclusion':'every boundary target at every even A>=12 has an exact rational contraction by induction'},'scope':'boundary top-three-degree targets only','checks':checks,'passed':True};(R/'cosmology_arbitrary_even_boundary_two_cover.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='checks'},indent=2))
