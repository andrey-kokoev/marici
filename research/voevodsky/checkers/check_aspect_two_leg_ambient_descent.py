#!/usr/bin/env python3
"""Test extension of the selected Aspect map over the ambient incidence lattice."""
from hashlib import sha256
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3];PACKET=ROOT/'research/voevodsky/aspect_two_leg_map_fails_ambient_incidence_descent.md';RESULT=ROOT/'research/voevodsky/results/aspect_two_leg_ambient_descent.json';SOURCE=ROOT/'research/benincasa/enhanced-conductor-unimodular-gluing.json';TARGET=ROOT/'research/aspect/contracts/relative-cech-de-rham-interferometer.v1.json'
a=json.loads(SOURCE.read_text(encoding='utf-8'));b=json.loads(TARGET.read_text(encoding='utf-8'));K=s.Matrix(a['K']);J=s.Matrix(a['J']);Phi=s.Matrix(a['Phi_exc']);D=s.Matrix(b['residue_map']);L=s.Matrix([[1,1,0],[1,0,-1]]);E=s.Matrix([[1,0],[0,1],[1,0],[1,0]]);F=s.eye(2);obs=L*Phi
checks={
 'source_factorization':Phi==J*K,
 'left_annihilator':L*D==s.zeros(2,2),
 'target_image_rank_one':D.rank()==1,
 'ambient_obstruction_exact':obs==s.Matrix([[2,0,0,-2],[0,0,2,-2]]),
 'ambient_obstruction_rank_two':obs.rank()==2,
 'ambient_extension_impossible':obs!=s.zeros(2,4),
 'selected_chain_boundaries':K*E==s.Matrix([[0,0],[-1,1],[1,-1]]),
 'obstruction_vanishes_on_selection':obs*E==s.zeros(2,2),
 'selected_chain_square':Phi*E==D*F,
 'physical_nonpromotion_retained':'Physical-chain compatibility remains unverified' in PACKET.read_text(encoding='utf-8')};checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.aspect-two-leg-ambient-descent.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'source_sha256':sha256(SOURCE.read_bytes()).hexdigest(),'target_sha256':sha256(TARGET.read_bytes()).hexdigest(),'cokernel_probe':[[1,1,0],[1,0,-1]],'ambient_obstruction':[list(map(int,obs.row(i))) for i in range(obs.rows)],'obstruction_rank':int(obs.rank()),'checks':checks,'passed':all(checks.values()),'disposition':{'selected_subcomplex_map':'exact chain map','ambient_extension':'impossible for fixed degree-zero map J','required_repair':'source-derived restriction/quotient killing obstruction or target enlargement','physical_status':'unverified'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'obstruction':result['ambient_obstruction'],'rank':result['obstruction_rank'],'disposition':result['disposition']}));raise SystemExit(0 if result['passed'] else 1)
