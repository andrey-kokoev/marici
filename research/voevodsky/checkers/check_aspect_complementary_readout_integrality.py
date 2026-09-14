#!/usr/bin/env python3
"""Audit integral faithfulness of the Aspect complementary readout."""
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
ROOT=Path(__file__).resolve().parents[3];PACKET=ROOT/'research/voevodsky/aspect_complementary_readout_is_complex_faithful_but_loses_one_integral_parity.md';RESULT=ROOT/'research/voevodsky/results/aspect_complementary_readout_integrality.json';SOURCE=ROOT/'research/aspect/contracts/relative-cech-de-rham-interferometer.v1.json'
a=json.loads(SOURCE.read_text(encoding='utf-8'));dark=s.Matrix(a['readouts']['scalar_dark_port']);R=s.Matrix(a['readouts']['complementary_phase_sensitive']);SR=smith_normal_form(R,domain=ZZ);z=s.Matrix(a['target_relative_cocycle']);outputs=[(u,v) for u,v in product(range(-3,4),repeat=2) if (u-v)%2==0];checks={'dark_exact':dark==s.Matrix([[1,-1]]),'complementary_exact':R==s.Matrix([[1,-1],[1,1]]),'determinant_two':R.det()==2,'smith_12':[abs(int(SR[i,i])) for i in range(2)]==[1,2],'inverse_half_integral':R.inv()==s.Matrix([[s.Rational(1,2),s.Rational(1,2)],[s.Rational(-1,2),s.Rational(1,2)]]),'mod2_rank_one':R.rank(iszerofunc=lambda x:int(x)%2==0)==1,'same_parity_image_samples':all(all(v.q==1 for v in R.inv()*s.Matrix([u,v])) for u,v in outputs),'closed_readout':R*z==s.Matrix([0,2]),'dark_closed_zero':dark*z==s.zeros(1,1),'primitive_maps_nonprimitive':s.gcd_list([int(v) for v in R*z])==2,'simulation_scope_retained':'simulation-only structural classifier' in a['scope'],'typed_space_gate_retained':'different typed spaces' in PACKET.read_text(encoding='utf-8')};checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.aspect-complementary-readout-integrality.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'source_sha256':sha256(SOURCE.read_bytes()).hexdigest(),'readout_matrix':a['readouts']['complementary_phase_sensitive'],'smith_invariants':[1,2],'image_condition':'output coordinates have equal parity','closed_class_readout':[0,2],'checks':checks,'passed':all(checks.values()),'disposition':{'characteristic_zero':'faithful','integral_cokernel':'Z/2','mod_two_rank':1,'conductor_parity_requirement':'not satisfied','physical_status':'simulation only'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':checks,'disposition':result['disposition']}));raise SystemExit(0 if result['passed'] else 1)
