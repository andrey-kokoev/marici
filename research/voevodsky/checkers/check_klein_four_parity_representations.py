#!/usr/bin/env python3
"""Enumerate Klein-four actions on F2^2 and torsion in the four lift presentations."""
from hashlib import sha256
from itertools import product
from math import gcd
from pathlib import Path
import json
import sympy as s
R=Path(__file__).resolve().parents[3];P=R/'research/voevodsky/klein_four_symmetry_can_leave_a_unique_nonzero_parity_only_conditionally.md';AUTO=R/'research/voevodsky/results/quartic_automorphism_obstruction.json';LOCAL=R/'research/benincasa/local-pl-parity-ambiguity.md';OUT=R/'research/voevodsky/results/klein_four_parity_representations.json';I=s.eye(2)
def eq2(A,B):return all(int(x)%2==0 for x in A-B)
gl=[]
for z in product((0,1),repeat=4):
 M=s.Matrix(2,2,z)
 if int(M.det())%2:gl.append(M)
invol=[M for M in gl if eq2(M*M,I)];pairs=[];vectors=[s.Matrix(v) for v in product((0,1),repeat=2)];nonzero=vectors[1:]
for A in invol:
 for B in invol:
  if eq2(A*B,B*A):
   image=[]
   for M in [I,A,B,A*B]:
    if not any(eq2(M,N) for N in image):image.append(M)
   fixed=[tuple(map(int,v)) for v in nonzero if eq2(A*v,v) and eq2(B*v,v)]
   pairs.append({'image_order':len(image),'nonzero_fixed':fixed})
torsion={(a,b):gcd(2,a,b) for a,b in product((0,1),repeat=2)};auto=json.loads(AUTO.read_text());local=LOCAL.read_text();text=P.read_text();checks={'GL2_F2_order_six':len(gl)==6,'involution_count_four':len(invol)==4,'all_images_at_most_two':all(q['image_order']<=2 for q in pairs),'all_have_nonzero_fixed':all(len(q['nonzero_fixed'])>=1 for q in pairs),'nontrivial_image_unique_nonzero_fixed':all(len(q['nonzero_fixed'])==1 for q in pairs if q['image_order']==2),'nonfaithful_Klein_four':all(q['image_order']<4 for q in pairs),'zero_class_torsion_two':torsion[(0,0)]==2,'nonzero_classes_torsion_free':all(torsion[v]==1 for v in [(1,0),(0,1),(1,1)]),'all_four_currently_retained':'all four parity vectors' in local,'prior_ambient_action_missing':auto['disposition']['all_parity_classes_obstructed']=='not established','conditional_scope':'If two new facts were proved' in text};checks={k:bool(v) for k,v in checks.items()};result={'schema':'marici.voevodsky.klein-four-parity-representations.v1','packet_sha256':sha256(P.read_bytes()).hexdigest(),'automorphism_result_sha256':sha256(AUTO.read_bytes()).hexdigest(),'commuting_involution_pair_count':len(pairs),'image_order_counts':{str(k):sum(q['image_order']==k for q in pairs) for k in [1,2]},'presentation_torsion_orders':{str(k):v for k,v in torsion.items()},'checks':checks,'passed':all(checks.values()),'disposition':{'unconditional_unique_parity':'not obtained','conditional_selector':['ambient torsion-free','nontrivial induced involution'],'required_computation':['Picard action matrix','ambient complement torsion audit']}};OUT.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'passed':result['passed'],'checks':checks,'disposition':result['disposition']}));raise SystemExit(0 if result['passed'] else 1)
