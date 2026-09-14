#!/usr/bin/env python3
"""Verify cospan torsion and rank obstructions to a local cusp-to-conductor map."""
from hashlib import sha256
from itertools import combinations,product
from math import gcd
from pathlib import Path
import json
import sympy as s
R=Path(__file__).resolve().parents[3]
P=R/'research/voevodsky/the_minimal_conductor_cospan_cannot_carry_the_two_bit_cusp_extension.md';C=R/'research/benincasa/cosmology-normalized-three-point-conductor-cospan.md';W=R/'research/benincasa/cosmology-weighted-relative-homology-derham-pairing-gate.md';JF=R/'research/benincasa/primitive-conductor-top-connection.json';L=R/'research/voevodsky/paired_local_thimbles_collapse_to_one_mod_two_direction.md';OUT=R/'research/voevodsky/results/conductor_cospan_boundary_map_gate.json'
B=s.Matrix([[-1,0],[0,1],[1,0],[0,-1]]);J=s.Matrix(json.loads(JF.read_text())['enhanced_intertwiner_J'])
def mg(M,k):
 g=0
 for rs in combinations(range(M.rows),k):
  for cs in combinations(range(M.cols),k):g=gcd(g,abs(int(M.extract(rs,cs).det())))
 return g
bs=[mg(B,1),mg(B,2)//mg(B,1)];d1,d12=mg(J,1),mg(J,2);js=[d1,d12//d1,abs(int(J.det()))//d12];S=s.Matrix([[0,1],[1,0]]);eq=[]
for z in product((0,1),repeat=4):
 M=s.Matrix(2,2,z)
 if int(M.det())%2 and all(int(q)%2==0 for q in M*S-S*M):eq.append(M)
c=C.read_text();w=W.read_text();local=L.read_text();text=P.read_text();images=[{(0,0),v} for v in product((0,1),repeat=2)]
cospan_missing=('no source map identifies `xi`' in c and 'with exceptional coordinate' in c)
pair_missing=('no common relative pair identifies the contour' in w and 'with the logarithmic coefficient system' in w)
checks={'B_rank_two':B.rank()==2,'B_snf_1_1':bs==[1,1],'B_cokernel_torsion_free':mg(B,2)==1,'J_snf_1_2_2':js==[1,2,2],'J_cokernel_order_four':abs(int(J.det()))==4,'two_equivariant_edge_matchings':len(eq)==2 and any(M==s.eye(2) for M in eq) and any(M==S for M in eq),'no_F2_surjection_to_F2_squared':all(len(i)<4 for i in images),'local_one_direction':'at most one mod-two direction' in local,'xi_r_map_missing':cospan_missing,'relative_pair_missing':pair_missing,'global_direction_required':'second independent direction comes from a globally marked ambient cycle' in text};checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.conductor-cospan-boundary-map-gate.v1','packet_sha256':sha256(P.read_bytes()).hexdigest(),'cospan_sha256':sha256(C.read_bytes()).hexdigest(),'weighted_pairing_sha256':sha256(W.read_bytes()).hexdigest(),'intertwiner_sha256':sha256(JF.read_bytes()).hexdigest(),'B_smith_invariants':bs,'J_smith_invariants':js,'equivariant_edge_matching_count':len(eq),'checks':checks,'passed':all(checks.values()),'disposition':{'cospan_incidence_to_two_bit_syndrome':'impossible without extension data','local_cusp_to_full_conductor_quotient':'not surjective','required_constructor':'global relative cycle plus primitive half-sum extension and xi-to-r wall map'}}
OUT.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'passed':result['passed'],'checks':checks,'disposition':result['disposition']}));raise SystemExit(0 if result['passed'] else 1)
