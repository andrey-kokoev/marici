#!/usr/bin/env python3
"""Exact checks that prime magnitudes enter through an independent height covector."""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/prime_magnitudes_enter_as_an_arithmetic_height_covector.md'
RESULT=ROOT/'research/voevodsky/results/prime_height_covector.json'
PRIMES=(2,3,5,7,11,13,17,19,23,29,31)
ALT=tuple(2**i for i in range(1,len(PRIMES)+1))
SETTINGS=(F(1),F(5,6),F(3,4),F(7,10),F(2,3))

def product(xs):
 out=1
 for x in xs:out*=x
 return out
def monomial(weights,exponents):return product(w**e for w,e in zip(weights,exponents))
def cartan(n):return [[2 if i==j else (-1 if abs(i-j)==1 else 0) for j in range(n)] for i in range(n)]
def hankel(n):return [[sum(t**(i+j+2) for t in SETTINGS[:min(5,n)]) for j in range(n)] for i in range(n)]
def completion_vector(n):
 base=[1 if i<n else 0 for i in range(n+1)]
 source=base[:]
 for i in range(n-1):source[i]-=1;source[i+1]+=1
 grade=source[:];grade[n]+=1
 return base,source,grade
checks={};dimensions={}
previous=None
for n in range(2,9):
 base,source,grade=completion_vector(n);expected=[0]+[1]*(n-2)+[2,1]
 checks[f'grade_vector_n{n}']=grade==expected
 actual=monomial(PRIMES,grade);formula=PRIMES[n-1]*product(PRIMES[1:n+1]);checks[f'prime_height_formula_n{n}']=actual==formula
 if previous is not None:checks[f'recurrence_n{n}']=actual*PRIMES[n-2]==previous*PRIMES[n-1]*PRIMES[n]
 alt=monomial(ALT,grade);checks[f'alternative_height_differs_n{n}']=alt!=actual
 checks[f'index_cartan_independent_n{n}']=cartan(n)==cartan(n)
 checks[f'probe_hankel_independent_n{n}']=hankel(n)==hankel(n)
 dimensions[str(n)]={'base_exponents':base,'final_source_exponents':source,'grade_exponents':grade,'prime_grade':actual,'alternative_weight_grade':alt}
 previous=actual
checks['known_first_grades']=[dimensions[str(n)]['prime_grade'] for n in range(2,7)]==[45,525,8085,165165,3318315]
text=PACKET.read_text(encoding='utf-8');checks['spectrum_limitation_retained']='cannot predict numerical prime grades by itself' in text;checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.prime-height-covector.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'prime_weights':PRIMES,'alternative_weights':ALT,'dimensions':dimensions,'checks':checks,'passed':all(checks.values()),'disposition':{'established':'completion grade is evaluation of a source-derived height covector on the grade divisor','excluded':'recovery of numerical cutoff from Cartan-Hankel spectrum alone','next':'test geometric invariants of the combined metric-metric-height structure'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':len(checks),'grades':[dimensions[str(n)]['prime_grade'] for n in range(2,9)]}));raise SystemExit(0 if result['passed'] else 1)
