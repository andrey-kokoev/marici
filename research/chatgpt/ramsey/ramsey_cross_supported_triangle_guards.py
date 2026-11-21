"""Independently verify counterexample to EXTERNAL-to-both-supports guard explanation. Does not refute admissible-switch closure: each switch creates a triangle."""
from pathlib import Path
from itertools import combinations
import json
from ramsey_hall_center_conjecture import decode
from ramsey_mutual_repair_conjecture import apply
D=Path(__file__).parent;e=json.loads((D/'ramsey_external_triangle_guard.json').read_text())['first_outside_guard_counterexample'];A=decode((D/'pauli-realization-catalogues'/'r37_22.g6').read_bytes().splitlines()[e['record']-1]);moves=e['switches'];states=[]
for mask in range(4):
 B=A[:]
 for k,s in enumerate(moves):
  if mask>>k&1:B=apply(B,s['removed'],s['added'])
 triangles=[I for I in combinations(range(22),3) if all(B[i]>>j&1 for i,j in combinations(I,2))];bad=[I for I in combinations(range(22),7) if all(not(B[i]>>j&1) for i,j in combinations(I,2))];states.append({'mask':mask,'triangles':triangles,'independent_sevens':bad})
assert [len(s['independent_sevens']) for s in states]==[0,1,1,2];assert [len(s['triangles']) for s in states]==[0,1,1,2]
repairs=[]
for k in range(2):
 I=states[1<<k]['independent_sevens'][0];hits=[edge for edge in moves[1-k]['added'] if set(edge)<=set(I)];assert hits;repairs.append({'defect_from_switch':k,'seven':I,'repair_edges':hits})
result={'source':e['record'],'switches':moves,'states':states,'blue_repairs':repairs};(D/'ramsey_cross_supported_triangle_guards.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
