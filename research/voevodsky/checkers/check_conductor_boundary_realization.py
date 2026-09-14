#!/usr/bin/env python3
"""Verify conductor-lattice realization of the minimal source boundary vector."""
from hashlib import sha256
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3];PACKET=ROOT/'research/voevodsky/conductor_intertwiner_realizes_the_shared_boundary_vector.md';RESULT=ROOT/'research/voevodsky/results/conductor_boundary_realization.json';SOURCE=ROOT/'research/benincasa/orientation-twisted-conductor-rees-intertwiner.json'
data=json.loads(SOURCE.read_text(encoding='utf-8'));J=s.Matrix(data['intertwiner_matrix_row_major']);target=s.Matrix([1,-1,1]);preimage=s.Matrix([0,-1,1]);sol=J.inv()*target;checks={
 'basis_exact':data['conductor_basis']==['g101','g110','g111_tilde'],
 'matrix_exact':J==s.Matrix([[2,0,1],[0,2,1],[0,0,1]]),
 'determinant_four':J.det()==4,
 'target_equal_parity':len({int(x)%2 for x in target})==1,
 'integral_solution_exact':sol==preimage,
 'matrix_replay':J*preimage==target,
 'solution_unique_over_Q':len(J.nullspace())==0,
 'audited_inverse_matches':data['integral_inverse_on_image']=={'a':'(u-w)/2','b':'(v-w)/2','c':'w'},
 'comparison_source_twisted':data['classification']['comparison']=='canonical after source orientation twist',
 'remaining_gate_retained':data['classification']['remaining']=='bulk relative Stokes scalar and support-sensitive extension',
 'degree_one_boundary_retained':'does not construct the two degree-one chains' in PACKET.read_text(encoding='utf-8')};checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.conductor-boundary-realization.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'source_sha256':sha256(SOURCE.read_bytes()).hexdigest(),'intertwiner':data['intertwiner_matrix_row_major'],'required_target_boundary':[1,-1,1],'conductor_preimage':[0,-1,1],'typed_expression':'-g110 + g111_tilde','checks':checks,'passed':all(checks.values()),'disposition':{'degree_zero_object':'realized in audited orientation-twisted conductor lattice','degree_one_objects':'missing','remaining':'two opposite-boundary labelled chains and residue-compatible relative Stokes pairing'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'preimage':result['conductor_preimage'],'checks':checks,'disposition':result['disposition']}));raise SystemExit(0 if result['passed'] else 1)
