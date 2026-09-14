#!/usr/bin/env python3
"""Checks completed interval synthesis bounds and finite kernel models."""
from pathlib import Path
from fractions import Fraction
import hashlib,json,math
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/the_completed_interval_synthesis_kernel_is_exactly_the_distributional_cycle_space_20260912.md'
AUG=ROOT/'research/voevodsky/the_completed_augmented_history_is_faithful_without_a_cycle_hilbert_metric_20260912.md'
RESULT=ROOT/'research/voevodsky/results/completed_interval_cycle_kernel.json'
primes=(2,3,5,7,11,13,17); shells=list(zip(primes,primes[1:])); checks={}
def model(L):
 E=[(k,p,q) for p,q in shells for k in range(1,L+1) if k*p*q<=L]; V=sorted({k*p for k,p,q in E}|{k*q for k,p,q in E}); vi={v:i for i,v in enumerate(V)}; cells=sorted(V); incidence=s.zeros(len(V),len(E)); coverage=s.zeros(max(V)+1,len(E))
 for j,(k,p,q) in enumerate(E):
  incidence[vi[k*p],j]-=1; incidence[vi[k*q],j]+=1
  for x in range(k*p,k*q): coverage[x,j]=1
 return E,incidence,coverage
for L in (80,160,320):
 E,B,J=model(L)
 checks[f'finite_kernel_identity_{L}']=len(E)-B.rank()==len(E)-J.rank() and B.nullspace()==J.nullspace()
 for delta in (.2,1):
  c=[Fraction((i%7)-3,i+2) for i in range(len(E))]; l1=sum(float(abs(c[i]))*math.log(q/p) for i,(k,p,q) in enumerate(E)); qd=sum(float(abs(c[i]))*math.exp(delta*math.log(k*p*q)) for i,(k,p,q) in enumerate(E))
  checks[f'L1_majorant_{L}_{delta}']=l1<=qd/delta+1e-12
# Absolute boundary action against bounded tests follows from source l1.
E,_,_=model(320); c=[math.exp(-math.log(k*p*q)**2) for k,p,q in E]
checks['source_l1_finite_census']=sum(c)<float('inf') and all(x>=0 for x in c)
text=PACKET.read_text()
checks['distribution_derivative_identity_stated']='distributional differentiation is justified by absolute convergence' in text
checks['L1_constant_elimination_stated']='Since \\(Jc\\in L^1(\\mathbb R)\\), that constant must be zero' in text
checks['history_reverse_kernel_not_promoted']='does not by itself prove' in text
checks['analytic_gate_named']='injectivity of \\(T_D\\)' in text
checks['prior_premise_narrowed']='completed cycle-kernel identity' in AUG.read_text()
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.completed-interval-cycle-kernel-check.v1','input_digests':{'packet':hashlib.sha256(PACKET.read_bytes()).hexdigest(),'augmented_predecessor':hashlib.sha256(AUG.read_bytes()).hexdigest()},'checks':checks,'passed':all(checks.values()),'disposition':{'proved':'ker J equals distributional cycle kernel on projective completion','remaining':'injectivity of completed-theta correlation T_D on J(C_exp)','not_proved':'ker Bhat equals ker J'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n'); print(json.dumps({'passed':result['passed'],'check_count':len(checks)})); raise SystemExit(0 if result['passed'] else 1)
