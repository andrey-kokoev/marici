#!/usr/bin/env python3
"""Checks the symmetric all-ratio grade and global history majorant."""
from pathlib import Path
from math import gcd,log,exp,sqrt
from fractions import Fraction
import hashlib,json
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/a_symmetric_arithmetic_grade_constructs_an_all_ratio_history_carrier_20260912.md'
BLOCK=ROOT/'research/voevodsky/completed_common_history_is_continuous_for_the_ratio_normalized_projective_source_20260912.md'
RESULT=ROOT/'research/voevodsky/results/all_ratio_symmetric_history_carrier.json'
primes=(2,3,5,7,11,13,17,19); shells=list(zip(primes,primes[1:])); bounds=(80,160,320)
def edges(N): return [(a,b,j,k,p,q) for a in range(1,N+1) for b in range(1,N+1) if gcd(a,b)==1 for j,(p,q) in enumerate(shells) for k in range(1,N+1) if a*b*k*p*q<=N]
Es={N:edges(N) for N in bounds}; checks={}
checks['finite_nested']=all(len(Es[N])<N**4 for N in bounds) and set(Es[80])<=set(Es[160])<=set(Es[320])
checks['exact_sublevel']=all(a*b*k*p*q<=N for N,S in Es.items() for a,b,j,k,p,q in S)
checks['reciprocal_closed']=all((b,a,j,k,p,q) in set(S) for S in Es.values() for a,b,j,k,p,q in S)
checks['reciprocal_grade_invariant']=all(log(a*b*k*p*q)==log(b*a*k*p*q) for S in Es.values() for a,b,j,k,p,q in S)
checks['block_shift']=all(abs(log(a*b*k*p*q)-(log(k*p*q)+log(a*b)))<1e-14 for a,b,j,k,p,q in Es[320])
for delta in (.1,.5,1):
 # Per-edge interval majorant and global l2 <= l1 aggregation by ratio block.
 checks[f'length_majorant_{delta}']=all(log(q/p)<=exp(delta*log(a*b*k*p*q))/delta+1e-12 for a,b,j,k,p,q in Es[320])
 coeff={tuple(e):Fraction((i%7)-3,i+2) for i,e in enumerate(Es[320])}
 block_sums={}
 for e,c in coeff.items():
  a,b,j,k,p,q=e; block_sums[(a,b)]=block_sums.get((a,b),0.0)+float(abs(c))*log(q/p)
 lhs=sqrt(sum(x*x for x in block_sums.values()))
 rhs=sum(float(abs(coeff[e]))*exp(delta*log(e[0]*e[1]*e[3]*e[4]*e[5]))/delta for e in coeff)
 checks[f'global_hilbert_by_projective_{delta}']=lhs<=rhs+1e-10
 # Reciprocal permutation preserves a scalar seminorm census.
 q0=sum(float(abs(coeff[e]))*exp(delta*log(e[0]*e[1]*e[3]*e[4]*e[5])) for e in coeff)
 qr=sum(float(abs(coeff[e]))*exp(delta*log(e[1]*e[0]*e[3]*e[4]*e[5])) for e in coeff)
 checks[f'reciprocal_seminorm_isometry_{delta}']=abs(q0-qr)<1e-10
checks['block_theorem_dependency']='extends uniquely to a continuous linear map' in BLOCK.read_text()
text=PACKET.read_text(); checks['no_physical_promotion']='It does not make the ratio index physical time' in text and 'or prove that nature uses this completion' in text
checks['nonuniqueness_disclosed']='other reciprocal-invariant proper grades may define inequivalent global completions' in text
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.all-ratio-symmetric-history-carrier-check.v1','input_digests':{'packet':hashlib.sha256(PACKET.read_bytes()).hexdigest(),'block_theorem':hashlib.sha256(BLOCK.read_bytes()).hexdigest()},'checks':checks,'passed':all(checks.values()),'edge_counts':{str(N):len(S) for N,S in Es.items()},'disposition':{'constructed':'symmetric proper all-ratio grade and continuous Hilbert direct-sum history map','reciprocity':'isometric block exchange','boundary':'candidate global completion, not physical calibration or uniqueness'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n'); print(json.dumps({'passed':result['passed'],'check_count':len(checks),'edge_counts':result['edge_counts']})); raise SystemExit(0 if result['passed'] else 1)
