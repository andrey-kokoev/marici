#!/usr/bin/env python3
"""CRT/rational reconstruction of the history-13 quartic candidate."""
from pathlib import Path
import json,itertools,random
from fractions import Fraction
from sympy.ntheory.modular import crt
from sympy.polys.modulargcd import _integer_rational_reconstruction
from sympy.polys.domains import ZZ
ROOT=Path(__file__).resolve().parents[3];primes=[1000003,1000033,1000037,1000039,1000081]
data=[json.loads((ROOT/f'research/nima/results/n8-history13-quartic-degree-{p}.json').read_text()) for p in primes]
def key(z):return tuple(z['exponents'])
maps=[{key(z):z['coefficient_mod_p']%p for z in d['quartic_kernel']} for p,d in zip(primes,data)];keys=sorted(set().union(*[set(m) for m in maps]));M=1
for p in primes:M*=p
coeff={};failed=[]
for k in keys:
 c=int(crt(primes,[m.get(k,0) for m in maps])[0]);q=_integer_rational_reconstruction(c,M,ZZ)
 if q is None:failed.append(k)
 else:coeff[k]=Fraction(int(q.numerator),int(q.denominator))
# Exact rational holdout through C Z and the target [1,2] affine chart.
def target(v):
 a1,a2,a3,a5,a6,a7,a8=map(Fraction,v);G=[[1,a1,a2+a3,(a2+a3)*a5,a3*a6,0,0],[0,0,1,a5,a6,a7,a8]];support=[1,2,4,5,6,7,8];C=[[Fraction(0) for _ in range(8)] for _ in range(2)]
 for j,lab in enumerate(support):C[0][lab-1]=G[0][j];C[1][lab-1]=G[1][j]
 Z=[[Fraction(t**k) for k in range(6)] for t in range(1,9)];Y=[[sum(C[i][r]*Z[r][j] for r in range(8)) for j in range(6)] for i in range(2)];d=Y[0][0]*Y[1][1]-Y[0][1]*Y[1][0];N=[[ (Y[1][1]*Y[0][j]-Y[0][1]*Y[1][j])/d for j in range(6)], [(-Y[1][0]*Y[0][j]+Y[0][0]*Y[1][j])/d for j in range(6)]];return [N[i][j] for i in range(2) for j in range(2,6)]
def evaluate(cv):
 z=Fraction(0)
 for e,c in coeff.items():
  t=c
  for i,k in enumerate(e):t*=cv[i]**k
  z+=t
 return z
rng=random.Random(314159);tests=[evaluate(target([rng.randrange(1,15) for _ in range(7)])) for _ in range(20)] if not failed else []
checks={'five_prime_kernels_unique':all(d['nullity']==1 for d in data),'all_coefficients_rationally_reconstructed':not failed,'exact_rational_holdout_vanishes':bool(tests) and all(v==0 for v in tests)}
out={'schema':'marici.nima.n8-history13-quartic-reconstruction.v1','primes':primes,'crt_modulus':M,'support_size':len(keys),'reconstructed_coefficients':len(coeff),'failed_coefficients':len(failed),'exact_holdout_samples':len(tests),'exact_holdout_nonzero':sum(v!=0 for v in tests),'quartic_coefficients':[{'exponents':list(k),'coefficient':str(v)} for k,v in coeff.items() if v],'checks':checks,'passed':all(checks.values()),'claim_boundary':'The reconstructed quartic passes exact rational point tests. A formal identity still requires symbolic pullback reduction or elimination.'};p=ROOT/'research/nima/results/n8-history13-quartic-reconstruction.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='quartic_coefficients'},indent=2));raise SystemExit(0 if out['passed'] else 1)
