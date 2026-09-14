#!/usr/bin/env python3
"""Exact audit of contraction descent, residual necessity, and nonsufficiency."""
from hashlib import sha256
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3];PACKET=ROOT/'research/voevodsky/descent_residual_represents_the_induced_homology_map.md';RESULT=ROOT/'research/voevodsky/results/descent_residual_theorem.json'
BASE=ROOT/'research/voevodsky/checkers/check_canonical_relative_chain_contractions.py';scope={'__file__':str(BASE)};exec(BASE.read_text(encoding='utf-8').split('checks={};dimensions={}')[0],scope);cells,D=scope['complex_at'](6);dims=[len(cells[k]) for k in range(7)]
# Reconstruct split-basis contraction in original cell coordinates.
B={};S={};P={}
for k in range(7):
 B[k]=D[k+1].columnspace() if k<6 else [];piv=D[k].rref()[1] if k else ();S[k]=[s.eye(dims[k]).col(j) for j in piv];P[k]=s.Matrix.hstack(*(B[k]+S[k]))
Dp={k:P[k-1].inv()*D[k]*P[k] for k in range(1,7)};Hp={};H={}
for k in range(6):
 bk=len(B[k]);bn=len(B[k+1]);A=Dp[k+1][:bk,bn:];h=s.zeros(dims[k+1],dims[k])
 if bk:h[bn:bn+bk,0:bk]=A.inv()
 Hp[k]=h;H[k]=P[k+1]*h*P[k].inv()
checks={};degrees={}
for k in range(7):
 identity=s.eye(dims[k]);dh=D[k+1]*H[k] if k<6 else s.zeros(dims[k]);hd=H[k-1]*D[k] if k else s.zeros(dims[k]);residual=identity-dh-hd
 checks[f'descended_residual_zero_k{k}']=residual==s.zeros(dims[k]);degrees[str(k)]={'dimension':dims[k],'descended_residual_rank':residual.rank(),'zero_homotopy_residual_rank':identity.rank()}
# Full target homology is zero despite residual I for the deliberately wrong h_S=0.
ranks={k:D[k].rank() for k in range(1,7)};betti=[dims[k]-ranks.get(k,0)-ranks.get(k+1,0) for k in range(7)]
checks['wrong_h_nonzero_residual_but_zero_homology']=all(x==0 for x in betti) and all(x['zero_homotopy_residual_rank']==x['dimension'] for x in degrees.values())
# Skeletal projections are graded maps but fail the chain-map equation exactly at the omitted block.
off=[0]
for n in dims:off.append(off[-1]+n)
dtotal=s.zeros(off[-1])
for k in range(1,7):dtotal[off[k-1]:off[k],off[k]:off[k+1]]=D[k]
trunc={}
for r in range(6):
 Q=s.diag(*([1]*off[r+1]+[0]*(off[-1]-off[r+1])));defect=Q*dtotal-dtotal*Q;trunc[str(r)]={'chain_map_defect_rank':defect.rank(),'omitted_boundary_rank':ranks[r+1]};checks[f'truncation_defect_is_omitted_boundary_r{r}']=defect.rank()==ranks[r+1]
text=PACKET.read_text(encoding='utf-8');checks['physical_gate_retained']='source-derived physical sector chain map' in text;checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.descent-residual-theorem.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'degrees':degrees,'target_betti':betti,'skeletal_boundary_cases':trunc,'checks':checks,'passed':all(checks.values()),'disposition':{'proved':'residual represents induced homology class; descended contraction forces zero','rejected':'raw nonzero matrix residual as sufficient sector evidence','missing':'source-derived physical sector chain map'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'target_betti':betti,'degrees':degrees,'checks':checks}));raise SystemExit(0 if result['passed'] else 1)
