#!/usr/bin/env python3
"""Compare skeletal projection defect with exposed top homology."""
from hashlib import sha256
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3];PACKET=ROOT/'research/voevodsky/truncation_obstruction_equals_exposed_top_homology.md';RESULT=ROOT/'research/voevodsky/results/truncation_descent_obstruction.json'
BASE=ROOT/'research/voevodsky/checkers/check_canonical_relative_chain_contractions.py';scope={'__file__':str(BASE)};exec(BASE.read_text(encoding='utf-8').split('checks={};dimensions={}')[0],scope);cells,D=scope['complex_at'](6)
dims=[len(cells[k]) for k in range(7)];ranks={k:D[k].rank() for k in range(1,7)};checks={};truncations={}
for r in range(7):
 betti=[]
 for k in range(r+1):
  incoming=ranks.get(k,0);outgoing=ranks.get(k+1,0) if k<r else 0;betti.append(dims[k]-incoming-outgoing)
 defect_rank=ranks.get(r+1,0)
 top_betti=betti[r]
 rec={'retained_degrees':[0,r],'betti':betti,'top_betti':top_betti,'projection_commutator_rank':defect_rank,'omitted_boundary_block':f'd_{r+1}' if r<6 else None}
 if r<6:checks[f'defect_equals_top_homology_r{r}']=defect_rank==top_betti
 else:checks['full_complex_acyclic_and_defect_free']=defect_rank==0 and betti==[0]*7
 truncations[str(r)]=rec
# Direct matrix realization of P d-d P on total graded space.
import sympy as s
off=[0]
for n in dims:off.append(off[-1]+n)
total=off[-1];dtotal=s.zeros(total)
for k in range(1,7):dtotal[off[k-1]:off[k],off[k]:off[k+1]]=D[k]
for r in range(6):
 P=s.diag(*([1]*off[r+1]+[0]*(total-off[r+1])));comm=P*dtotal-dtotal*P
 checks[f'direct_commutator_rank_r{r}']=comm.rank()==ranks[r+1]
text=PACKET.read_text(encoding='utf-8');checks['physical_boundary_retained']='not source-derived physical sector maps' in text;checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.truncation-descent-obstruction.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'full_cell_dimensions':dims,'full_boundary_ranks':[ranks[k] for k in range(1,7)],'truncations':truncations,'checks':checks,'passed':all(checks.values()),'disposition':{'mechanism':'projection commutator rank exactly equals truncation-exposed top homology','restoration':'next chain degree supplies the omitted image','physical_status':'nonphysical algebraic negative control'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'truncations':truncations,'checks':checks}));raise SystemExit(0 if result['passed'] else 1)
