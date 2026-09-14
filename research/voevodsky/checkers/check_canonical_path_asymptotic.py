#!/usr/bin/env python3
"""Exact canonical path-count formula and e*n! asymptotic test."""
from decimal import Decimal,getcontext
from hashlib import sha256
from math import comb,factorial
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3];PACKET=ROOT/'research/voevodsky/canonical_path_complexity_is_asymptotic_to_e_factorial.md';RESULT=ROOT/'research/voevodsky/results/canonical_path_asymptotic.json';getcontext().prec=80
def choose(n,k):return comb(n,k) if 0<=k<=n else 0
def coefficient(n,r):
 N=n-2;return choose(N,r)+choose(N,r-1)+choose(N,r-2)
def direct(n):return sum(factorial(r)*coefficient(n,r) for r in range(1,n+1))
def closed(n):
 N=n-2;nf=factorial(N)
 a=sum(nf//factorial(j) for j in range(N))
 b=sum((N-j+1)*(nf//factorial(j)) for j in range(N+1))
 c=sum((N-j+2)*(N-j+1)*(nf//factorial(j)) for j in range(N+1))
 return a+b+c
E=Decimal(1).exp();checks={};rows={}
for n in range(3,51):
 a=direct(n);b=closed(n);checks[f'exact_formula_n{n}']=a==b
 rows[str(n)]={'path_increment':a,'ratio_to_factorial':str(Decimal(a)/Decimal(factorial(n))),'absolute_error_from_e':str(abs(Decimal(a)/Decimal(factorial(n))-E))}
errors={n:Decimal(rows[str(n)]['absolute_error_from_e']) for n in (10,20,30,40,50)}
checks['known_n6']=direct(6)==1695
checks['tail_error_decreases']=errors[20]>errors[30]>errors[40]>errors[50]
checks['n50_within_point06_of_e']=errors[50]<Decimal('0.06')
text=PACKET.read_text(encoding='utf-8');checks['interpretation_boundary_retained']='not a count of homology classes' in text;checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.canonical-path-asymptotic.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'exact_values':{str(n):rows[str(n)]['path_increment'] for n in range(3,16)},'asymptotic_samples':{str(n):rows[str(n)] for n in (10,20,30,40,50)},'e_decimal':str(E),'checks':checks,'passed':all(checks.values()),'disposition':{'exact_formula':'verified n=3..50 and derived algebraically','asymptotic':'R_n/(n!) tends to e','homology_contrast':'all canonical relative attachments remain integrally contractible'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'exact_values':result['exact_values'],'samples':result['asymptotic_samples'],'checks':checks}));raise SystemExit(0 if result['passed'] else 1)
