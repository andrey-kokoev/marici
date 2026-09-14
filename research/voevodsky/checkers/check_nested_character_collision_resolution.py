#!/usr/bin/env python3
"""Exact test that setting m+1 resolves the P_m character collision."""
from hashlib import sha256
from math import factorial
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3];PACKET=ROOT/'research/voevodsky/one_added_character_resolves_each_constructed_collision.md';RESULT=ROOT/'research/voevodsky/results/nested_character_collision_resolution.json'
x=s.symbols('x');checks={};cases={}
for m in range(1,11):
 coeff=list(reversed([int(c) for c in s.Poly(s.prod(x-a for a in range(1,m+1)),x).all_coeffs()]));u=[max(c,0) for c in coeff];v=[max(-c,0) for c in coeff]
 def read(route,a):return sum(c*a**i for i,c in enumerate(route))
 old_u=[read(u,a) for a in range(1,m+1)];old_v=[read(v,a) for a in range(1,m+1)];new_difference=read(u,m+1)-read(v,m+1)
 M_old=s.Matrix([[a**i for i in range(m+1)] for a in range(1,m+1)]);M_new=s.Matrix([[a**i for i in range(m+1)] for a in range(1,m+2)]);Q_old=M_old.T*M_old;Q_new=M_new.T*M_new
 rec={'support_shells':m+1,'route_length':sum(u),'old_readouts_equal':old_u==old_v,'new_readout_difference':new_difference,'expected_difference':factorial(m),'old_evaluation_rank':M_old.rank(),'new_evaluation_rank':M_new.rank(),'old_gram_nullity':len(Q_old.nullspace()),'new_gram_nullity':len(Q_new.nullspace()),'new_vandermonde_determinant':int(M_new.det())}
 checks[f'collision_then_resolution_m{m}']=u!=v and sum(u)==sum(v) and old_u==old_v and new_difference==factorial(m) and rec['old_evaluation_rank']==m and rec['new_evaluation_rank']==m+1 and rec['old_gram_nullity']==1 and rec['new_gram_nullity']==0 and rec['new_vandermonde_determinant']!=0;cases[str(m)]=rec
text=PACKET.read_text(encoding='utf-8');checks['scope_retained']='does not show that every ambiguity is resolved by one arbitrary added probe' in text;checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.nested-character-collision-resolution.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'cases':cases,'checks':checks,'passed':all(checks.values()),'disposition':{'constructed_ambiguities':'each is exactly resolved by setting m+1 for m=1..10','rank_transition':'nullity one to zero on fixed support','global_boundary':'new shells restore ambiguity for every finite family'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':len(checks),'differences':{m:r['new_readout_difference'] for m,r in cases.items()}}));raise SystemExit(0 if result['passed'] else 1)
