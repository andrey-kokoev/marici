#!/usr/bin/env python3
"""Classify site-symmetric linear readouts of the two-bit parity defect."""
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3];PACKET=ROOT/'research/voevodsky/site_symmetric_scalar_readout_cannot_detect_both_parity_defects.md';RESULT=ROOT/'research/voevodsky/results/site_symmetric_parity_readouts.json';Sigma=s.Matrix([[0,1],[1,0]]);I=s.eye(2);vectors=[s.Matrix(v) for v in product((0,1),repeat=2)];functionals=[]
for a,b in product((0,1),repeat=2):
 row=s.Matrix([[a,b]]); invariant=all(int(x)%2==0 for x in row*Sigma-row); kernel=[list(map(int,v)) for v in vectors if int((row*v)[0])%2==0];functionals.append({'row':[a,b],'invariant':invariant,'kernel':kernel})
invariant=[f for f in functionals if f['invariant']];nonzero=[f for f in invariant if f['row']!=[0,0]];N=Sigma-I;checks={'invariant_functionals_two':len(invariant)==2,'unique_nonzero_invariant':len(nonzero)==1 and nonzero[0]['row']==[1,1],'symmetric_kernel_exact':nonzero[0]['kernel']==[[0,0],[1,1]],'nilpotent_difference':(N*N).applyfunc(lambda x:int(x)%2)==s.zeros(2,2),'swap_nontrivial_mod2':Sigma!=I,'difference_rank_one_mod2':N.rank(iszerofunc=lambda x:int(x)%2==0)==1,'faithful_scalar_impossible':all(len(f['kernel'])>=2 for f in functionals),'identity_readout_faithful':len({tuple(v) for v in vectors})==4,'physical_gate_retained':'Physical realization remains absent' in PACKET.read_text(encoding='utf-8')};checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.site-symmetric-parity-readouts.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'defect_space':'F2^2','wall_exchange':[[0,1],[1,0]],'linear_scalar_functionals':functionals,'minimal_faithful_output_rank':2,'checks':checks,'passed':all(checks.values()),'disposition':{'symmetric_scalar':'detects b1+b2 only','invisible_nonzero_class':[1,1],'faithful_readout':'two wall-labelled channels','physical_status':'unverified'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':checks,'disposition':result['disposition']}));raise SystemExit(0 if result['passed'] else 1)
