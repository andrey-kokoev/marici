#!/usr/bin/env python3
"""Verify that the logarithmic and blow-up legs close only as a coupled cycle."""
from hashlib import sha256
from math import gcd
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3];PACKET=ROOT/'research/voevodsky/blowup_face_leg_requires_coupled_logarithmic_source.md';RESULT=ROOT/'research/voevodsky/results/coupled_logarithmic_face_legs.json';CONTRACT=ROOT/'research/aspect/contracts/relative-cech-de-rham-interferometer.v1.json'
c=json.loads(CONTRACT.read_text(encoding='utf-8'));D=c['residue_map'];v=c['target_relative_cocycle'];b=[0,1];a=[v[i]-b[i] for i in range(2)]
def mv(M,x,mod=None):
 y=[sum(row[i]*x[i] for i in range(len(x))) for row in M]
 return [z%mod for z in y] if mod else y
Da=mv(D,a);Db=mv(D,b);Dv=mv(D,v);checks={'missing_leg_exact':a==[1,0],'total_closed_integrally':Dv==[0,0,0],'log_leg_nonclosed':Da!=[0,0,0],'face_leg_nonclosed':Db!=[0,0,0],'opposite_residues':all(x==-y for x,y in zip(Da,Db)),'total_primitive':gcd(*map(abs,v))==1}
fields={}
for p in (101,103):
 fields[str(p)]={'D_a':mv(D,a,p),'D_b':mv(D,b,p),'D_total':mv(D,v,p)};checks[f'finite_field_cancellation_{p}']=fields[str(p)]['D_total']==[0,0,0] and fields[str(p)]['D_a']!=[0,0,0] and all((x+y)%p==0 for x,y in zip(fields[str(p)]['D_a'],fields[str(p)]['D_b']))
text=PACKET.read_text(encoding='utf-8');checks['source_gate_retained']='does not construct the missing logarithmic source object' in text;checks={k:bool(x) for k,x in checks.items()}
result={'schema':'marici.voevodsky.coupled-logarithmic-face-legs.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'aspect_contract_sha256':sha256(CONTRACT.read_bytes()).hexdigest(),'logarithmic_leg':a,'blowup_face_leg':b,'total':v,'integral_residues':{'logarithmic':Da,'face':Db,'total':Dv},'finite_fields':fields,'checks':checks,'passed':all(checks.values()),'disposition':{'independent_sphere_maps':'impossible for either leg','minimal_source_shape':'one coupled cycle or a two-leg complex carrying the residue cancellation','missing':'source-derived relative homology-de Rham pairing'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'residues':result['integral_residues'],'checks':checks,'disposition':result['disposition']}));raise SystemExit(0 if result['passed'] else 1)
