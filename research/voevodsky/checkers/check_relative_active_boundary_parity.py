#!/usr/bin/env python3
"""Verify the labelled mod-two cokernel character of the relative matrix."""
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3];PACKET=ROOT/'research/voevodsky/relative_intersection_defect_is_the_active_boundary_endpoint_parity.md';RESULT=ROOT/'research/voevodsky/results/relative_active_boundary_parity.json';PAGE=ROOT/'references/extractions/pdf-search-all/cosmology-meets-cohomology-2308-03753/pdf-page-0021.txt';INTER=ROOT/'research/benincasa/orientation-twisted-conductor-rees-intertwiner.json'
C=s.Matrix([[0,-1,1,0],[1,0,0,0],[1,1,0,1],[-1,0,1,-1]]);lrel=s.Matrix([[1,0,1,1]]);chars=[]
for bits in product((0,1),repeat=4):
 if any(bits) and all(int(v)%2==0 for v in s.Matrix([bits])*C):chars.append(bits)
J1=s.Matrix([[2,0,1],[0,1,0],[0,0,1]]);J2=s.Matrix([[1,0,0],[0,2,1],[0,0,1]]);l1=s.Matrix([[1,0,1]]);l2=s.Matrix([[0,1,1]]);J=J1*J2;checks={'relative_character_annihilates':all(int(v)%2==0 for v in lrel*C),'relative_character_unique':chars==[(1,0,1,1)],'relative_mod2_rank_three':C.rank(iszerofunc=lambda x:int(x)%2==0)==3,'omitted_S12_coefficient_zero':lrel[0,1]==0,'active_endpoint_coefficients_one':tuple(lrel)==(1,0,1,1),'conductor_factor_1_character':all(int(v)%2==0 for v in l1*J1),'conductor_factor_2_character':all(int(v)%2==0 for v in l2*J2),'product_equal_parity':all(all(int(v)%2==0 for v in ell*J) for ell in (l1,l2)),'integral_gate_retained':'conditional on those differential-form bases carrying source-authorized integral lattices' in PACKET.read_text(encoding='utf-8'),'not_physical_record':'not an already physical binary record' in PACKET.read_text(encoding='utf-8')};checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.relative-active-boundary-parity.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'source_page_sha256':sha256(PAGE.read_bytes()).hexdigest(),'conductor_source_sha256':sha256(INTER.read_bytes()).hexdigest(),'relative_basis':['delta3(phi1)','delta12(1)','delta23(1)','delta13(1)'],'relative_cokernel_character':[1,0,1,1],'conductor_characters':[[1,0,1],[0,1,1]],'checks':checks,'passed':all(checks.values()),'disposition':{'relative_parity':'active boundary plus two incident endpoints','S12':'excluded','conductor_target':'two wall-labelled transported characters','physical_status':'unverified'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':checks,'disposition':result['disposition']}));raise SystemExit(0 if result['passed'] else 1)
