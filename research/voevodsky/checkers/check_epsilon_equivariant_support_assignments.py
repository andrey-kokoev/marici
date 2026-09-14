#!/usr/bin/env python3
"""Verify conductor orbits and count equivariant signed support assignments."""
from hashlib import sha256
from itertools import permutations,product
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3];PACKET=ROOT/'research/voevodsky/epsilon_equivariance_reduces_the_relative_support_assignment_fiber.md';RESULT=ROOT/'research/voevodsky/results/epsilon_equivariant_support_assignments.json';SOURCE=ROOT/'research/benincasa/enhanced-conductor-unimodular-gluing.json';ACTION=ROOT/'research/benincasa/orientation-twisted-conductor-rees-intertwiner.json'
a=json.loads(SOURCE.read_text(encoding='utf-8'));act=json.loads(ACTION.read_text(encoding='utf-8'));Phi=s.Matrix(a['Phi_exc']);De=s.diag(*act['enhanced_character_action']['epsilon_flip']);Dd=s.diag(*act['enhanced_character_action']['delta_flip']);q1=Phi[:,0];q2=Phi[:,2];labels=(0,1);all_assignments=[];equivariant=[]
for perm in permutations(labels):
 for signs in product((-1,1),repeat=2):
  item=(perm,signs);all_assignments.append(item)
  # Both domain and codomain involutions swap their two elements without sign.
  if signs[0]==signs[1]:equivariant.append(item)
checks={'epsilon_swaps_selected_pair':De*q1==q2 and De*q2==q1,'delta_reaches_complement':Dd*q1==Phi[:,1] and Dd*q2==Phi[:,3],'full_columns_distinct':len({tuple(Phi[:,j]) for j in range(4)})==4,'unsigned_bijections_two':len(list(permutations(labels)))==2,'signed_assignments_eight':len(all_assignments)==8,'equivariant_assignments_four':len(equivariant)==4,'common_sign_condition':all(z[1][0]==z[1][1] for z in equivariant),'hypothesis_retained':'explicit hypothesis that epsilon swap models site exchange' in PACKET.read_text(encoding='utf-8'),'full_symmetry_not_claimed':'full four-point orbit' in PACKET.read_text(encoding='utf-8')};checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.epsilon-equivariant-support-assignments.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'source_sha256':sha256(SOURCE.read_bytes()).hexdigest(),'epsilon_orbit':['Phi_++','Phi_-+'],'delta_image':['Phi_+-','Phi_--'],'unconstrained_signed_assignments':len(all_assignments),'epsilon_equivariant_assignments':len(equivariant),'checks':checks,'passed':all(checks.values()),'disposition':{'assignment_fiber':'four conditional equivariant candidates','epsilon_site_exchange':'unverified hypothesis','common_orientation_sign':'unfixed','full_two_swap_equivariance':'fails on selected pair'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':checks,'disposition':result['disposition']}));raise SystemExit(0 if result['passed'] else 1)
