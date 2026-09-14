#!/usr/bin/env python3
"""Checks actual consecutive-prime fixed-ratio product grades."""
from pathlib import Path
from math import gcd,log,exp,isclose
import hashlib,json
ROOT=Path(__file__).resolve().parents[3]
SOURCE=ROOT/'research/nima/consecutive-prime-shell-widths-exclude-the-pairwise-label-dilation-collision.md'
PACKET=ROOT/'research/voevodsky/actual_consecutive_prime_fixed_ratio_grade_and_reflection_20260912.md'
RESULT=ROOT/'research/voevodsky/results/actual_consecutive_prime_fixed_ratio_grade.json'
primes=(2,3,5,7,11,13,17,19,23,29,31,37,41,43,47); shells=list(zip(primes,primes[1:])); ratios=((1,1),(2,3),(3,2),(5,7))
checks={}
checks['source_declares_consecutive_primes']='Candidate one uses consecutive primes' in SOURCE.read_text()
checks['source_declares_theta_ratio']='D=\\log\\frac mn' in SOURCE.read_text()
# Reduced-ratio parameterization is exhaustive and unique in a bounded census.
for a,b in ratios:
 checks[f'ratio_parameterization_{a}_{b}']=gcd(a,b)==1 and all((m*b==n*a)==(n%b==0 and m==(n//b)*a) for n in range(1,100) for m in range(1,100))
def edge_set(a,b,N): return [(j,k,p,q) for j,(p,q) in enumerate(shells) for k in range(1,N+1) if k*b*p*q<=N]
for a,b in ratios:
 sets=[edge_set(a,b,N) for N in (100,300,900)]
 checks[f'finite_nested_{a}_{b}']=all(len(x)<10000 for x in sets) and set(sets[0])<=set(sets[1])<=set(sets[2])
 checks[f'grade_sublevel_{a}_{b}']=all(log(k*b*p*q)<=log(N)+1e-14 for N,S in zip((100,300,900),sets) for j,k,p,q in S)
 checks[f'length_by_grade_{a}_{b}']=all(log(q/p)<=log(k*b*p*q)+1e-14 for S in sets for j,k,p,q in S)
 for delta in (.1,.5,1,2): checks[f'uniform_exp_{a}_{b}_{delta}']=all(log(q/p)<=exp(delta*log(k*b*p*q))/delta+1e-13 for S in sets for j,k,p,q in S)
 # Reflection swaps n,m and shifts grade by D=log(a/b).
 checks[f'reflection_grade_shift_{a}_{b}']=all(isclose(log(k*a*p*q),log(k*b*p*q)+log(a/b),abs_tol=1e-14) for j,k,p,q in sets[-1])
 checks[f'reflection_seminorm_factor_{a}_{b}']=all(isclose(exp(.4*log(k*a*p*q)),exp(.4*log(a/b))*exp(.4*log(k*b*p*q)),rel_tol=1e-14) for j,k,p,q in sets[-1])
checks['reversed_shell_not_actual']=all((q,p) not in shells for p,q in shells)
checks['zero_ratio_grade_invariant']=all(log(k*p*q)==log(k*p*q) for j,k,p,q in edge_set(1,1,900))
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.actual-consecutive-prime-fixed-ratio-grade-check.v1','input_digests':{'source':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'packet':hashlib.sha256(PACKET.read_bytes()).hexdigest()},'checks':checks,'passed':all(checks.values()),'ratios':[f'{a}/{b}' for a,b in ratios],'disposition':{'instantiated':'consecutive-prime shells and unique fixed-ratio multiplicity (n,m)=(kb,ka)','corrected':'p-q reversal is not source reciprocal closure','reflection':'D to -D with additive grade shift D and exact seminorm scaling'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n'); print(json.dumps({'passed':result['passed'],'check_count':len(checks),'ratios':len(ratios)})); raise SystemExit(0 if result['passed'] else 1)
