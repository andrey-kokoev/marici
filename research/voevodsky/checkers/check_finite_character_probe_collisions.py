#!/usr/bin/env python3
"""Exact finite-character rank and constructive route-collision test."""
from hashlib import sha256
from pathlib import Path
import json
import sys
import sympy as s
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[3];PACKET=ROOT/'research/voevodsky/finite_character_probes_have_constructive_route_collisions.md';RESULT=ROOT/'research/voevodsky/results/finite_character_probe_collisions.json'
def primes(n):
 a=bytearray(b'\1')*(n+1);a[:2]=b'\0\0'
 for p in range(2,int(n**.5)+1):
  if a[p]:a[p*p:n+1:p]=b'\0'*(((n-p*p)//p)+1)
 return [i for i in range(2,n+1) if a[i]]
PS=primes(100);x=s.symbols('x');checks={};cases={}
for m in range(1,9):
 rank_cases=[]
 for R in range(m+1,21):
  M=s.Matrix([[a**i for i in range(R)] for a in range(1,m+1)]);Q=M.T*M
  ok=M.rank()==m and Q.rank()==m and len(Q.nullspace())==R-m
  checks[f'rank_m{m}_R{R}']=ok;rank_cases.append({'shell_cutoff':R,'rank':M.rank(),'radical_dimension':R-m})
 P=s.Poly(s.prod(x-a for a in range(1,m+1)),x);coeff=list(reversed([int(c) for c in P.all_coeffs()]));u=[max(c,0) for c in coeff];v=[max(-c,0) for c in coeff]
 read_u=[sum(c*a**i for i,c in enumerate(u)) for a in range(1,m+1)];read_v=[sum(c*a**i for i,c in enumerate(v)) for a in range(1,m+1)]
 base=1
 for i,(a,b) in enumerate(zip(u,v)):base*=PS[i]**max(a,b)
 def endpoint(route):
  numerator=base
  for i,c in enumerate(route):numerator=numerator*PS[i+1]**c//PS[i]**c
  return numerator
 eu,ev=endpoint(u),endpoint(v)
 def digest_integer(n):
  raw=str(n);return {'decimal_digits':len(raw),'sha256':sha256(raw.encode()).hexdigest()}
 collision={'coefficients':coeff,'positive_route':u,'negative_route':v,'route_length':sum(u),'readouts':read_u,'common_base':digest_integer(base),'positive_endpoint':digest_integer(eu),'negative_endpoint':digest_integer(ev),'distinct_endpoints':eu!=ev}
 checks[f'collision_m{m}']=u!=v and read_u==read_v and sum(u)==sum(v) and eu!=ev and all(base%PS[i]**max(a,b)==0 for i,(a,b) in enumerate(zip(u,v)))
 cases[str(m)]={'rank_cases':rank_cases,'collision':collision}
# Directly test joint separation on all nonzero coefficient vectors with entries -1,0,1 and support <=5 using first six settings.
from itertools import product
separated=True
for R in range(1,6):
 for c in product((-1,0,1),repeat=R):
  if any(c) and all(sum(c[i]*a**i for i in range(R))==0 for a in range(1,7)):separated=False
checks['bounded_countable_separation_sample']=separated
text=PACKET.read_text(encoding='utf-8');checks['nonlinear_scope_retained']='does not prove that every possible nonlinear or noncharacter readout is nonfaithful' in text;checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.finite-character-probe-collisions.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'cases':cases,'checks':checks,'passed':all(checks.values()),'disposition':{'finite_family':'nonfaithful with explicit same-length route collision for every m=1..8','general_character_result':'Vandermonde rank proves every finite m has radical beyond shell m','countable_family':'joint faithfulness proved by polynomial root bound'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':len(checks),'collisions':{m:{k:v for k,v in q['collision'].items() if k in ('route_length','common_base','positive_endpoint','negative_endpoint')} for m,q in cases.items()}}));raise SystemExit(0 if result['passed'] else 1)
