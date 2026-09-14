#!/usr/bin/env python3
"""Audit the exact algebraic content of the speculative relative-boundary enlargement."""
from hashlib import sha256
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3];PACKET=ROOT/'research/voevodsky/speculative_relative_boundary_enlargement_for_aspect_descent.md';RESULT=ROOT/'research/voevodsky/results/speculative_relative_boundary_enlargement.json';INC=ROOT/'research/benincasa/enhanced-conductor-unimodular-gluing.json';TARGET=ROOT/'research/aspect/contracts/relative-cech-de-rham-interferometer.v1.json'
a=json.loads(INC.read_text(encoding='utf-8'));b=json.loads(TARGET.read_text(encoding='utf-8'));J=s.Matrix(a['J']);K=s.Matrix(a['K']);Phi=s.Matrix(a['Phi_exc']);D=s.Matrix(b['residue_map']);r=D[:,0];q1=Phi[:,0];q2=Phi[:,2];Dext=s.Matrix.hstack(D,q1,q2);P=s.Matrix([[0,0,0,1],[0,1,0,0],[1,0,0,-1],[0,0,1,-1]]);E=s.Matrix([[1,0],[0,1],[1,0],[1,0]]);I=s.Matrix.vstack(s.eye(2),s.zeros(2,2));B=s.Matrix.hstack(r,q1,q2);L=s.Matrix([[1,1,0],[1,0,-1]])
checks={
 'ambient_source_identity':Phi==J*K,
 'old_target_rank_one':D.rank()==1,
 'obstruction_rank_two':(L*Phi).rank()==2 and L*D==s.zeros(2,2),
 'support_vectors_exact':q1==s.Matrix([1,1,1]) and q2==s.Matrix([1,-1,-1]),
 'extended_rank_three':Dext.rank()==3,
 'ambient_factorization':Dext*P==Phi,
 'selected_assignment_preserved':P*E==I,
 'selected_square_preserved':Phi*E==D,
 'equal_parity_lattice_index_four':abs(int(B.det()))==4 and abs(int(J.det()))==4,
 'support_claim_unverified':'Source support assignment and physical interpretation remain unverified' in PACKET.read_text(encoding='utf-8')};checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.speculative-relative-boundary-enlargement.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'source_digests':{'incidence':sha256(INC.read_bytes()).hexdigest(),'aspect_target':sha256(TARGET.read_bytes()).hexdigest()},'extended_differential':[list(map(int,Dext.row(i))) for i in range(Dext.rows)],'ambient_comparison':[list(map(int,P.row(i))) for i in range(P.rows)],'new_support_vectors':[list(map(int,q1)),list(map(int,q2))],'checks':checks,'passed':all(checks.values()),'disposition':{'algebraic_extension':'verified minimal rank-two completion','source_support_assignment':'missing','physical_status':'unverified'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':checks,'disposition':result['disposition']}));raise SystemExit(0 if result['passed'] else 1)
