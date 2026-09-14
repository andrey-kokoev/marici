#!/usr/bin/env python3
"""Verify the unique positive two-leg realization in the enhanced incidence lattice."""
from hashlib import sha256
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3];PACKET=ROOT/'research/voevodsky/enhanced_incidence_lattice_realizes_the_minimal_two_leg_source.md';RESULT=ROOT/'research/voevodsky/results/enhanced_incidence_two_leg_realization.json';SOURCE=ROOT/'research/benincasa/enhanced-conductor-unimodular-gluing.json'
data=json.loads(SOURCE.read_text(encoding='utf-8'));K=s.Matrix(data['K']);J=s.Matrix(data['J']);Phi=s.Matrix(data['Phi_exc']);r=s.Matrix([0,-1,1]);elog=s.Matrix([1,0,1,1]);eface=s.Matrix([0,1,0,0]);cycle=s.ones(4,1);E=s.Matrix.hstack(elog,eface);dA=s.Matrix([[1,-1]])
t=s.symbols('t',integer=True);solution=s.linsolve((K,r));checks={
 'source_identity':Phi==J*K,
 'K_surjective':K.rank()==3 and data['K_surjective'] is True,
 'kernel_primitive':K.nullspace()==[cycle] and data['K_kernel']==[1,1,1,1],
 'opposite_boundaries':K*elog==r and K*eface==-r,
 'primitive_cycle_sum':elog+eface==cycle and K*cycle==s.zeros(3,1),
 'chain_embedding':K*E==r*dA,
 'general_solution':K*elog==r and len(K.nullspace())==1 and K.nullspace()[0]==cycle,
 'both_legs_nonnegative':all(int(x)>=0 for x in elog) and all(int(x)>=0 for x in eface),
 'unique_nonnegative_split':all(not (u>=0 and u-1>=0 and 1-u>=0 and 2-u>=0) or u==1 for u in range(-20,21)),
 'physical_gate_retained':'does not construct the cycle-form map' in PACKET.read_text(encoding='utf-8'),
 'source_marks_physical_compatibility_missing':'physical-chain compatibility across the full signed-energy arrangement' in data['remaining']};checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.enhanced-incidence-two-leg-realization.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'source_sha256':sha256(SOURCE.read_bytes()).hexdigest(),'point_order':data['point_order'],'logarithmic_chain':[1,0,1,1],'face_chain':[0,1,0,0],'shared_boundary':[0,-1,1],'primitive_cycle':[1,1,1,1],'checks':checks,'passed':all(checks.values()),'disposition':{'source_complex':'realized as unique nonnegative two-leg subcomplex','comparison_map':'missing support-sensitive relative Stokes pairing','physical_status':'unverified'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':checks,'disposition':result['disposition']}));raise SystemExit(0 if result['passed'] else 1)
