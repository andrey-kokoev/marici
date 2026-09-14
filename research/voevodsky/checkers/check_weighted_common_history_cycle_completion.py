#!/usr/bin/env python3
"""Exact finite-section checks for the weighted history/kernel completion."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/voevodsky/contracts/weighted-common-history-cycle-completion.v1.json'
RESULT=ROOT/'research/voevodsky/results/weighted_common_history_cycle_completion.json'
d=json.loads(CONTRACT.read_text()); checks={}; sections={}
for N in (3,5,10):
 ell=[s.Rational((n%3)+1,n+2) for n in range(N)]
 q=[s.Rational(1,2**(n+1)) for n in range(N)]
 alpha=[ell[n]**2/q[n] for n in range(N)]
 W=s.diag(*alpha); B=s.Matrix([ell]) # collinear worst-case normalized history columns
 Winv=W.inv(); gram=(B*Winv*B.T)[0]
 P=s.eye(N)-Winv*B.T*(B*Winv*B.T).inv()*B
 checks[f'budget_partial_sum_{N}']=sum(q)==1-s.Rational(1,2**N)
 checks[f'operator_norm_squared_{N}']=gram==sum(q)<1
 checks[f'kernel_projection_idempotent_{N}']=P*P==P
 checks[f'kernel_projection_lands_in_kernel_{N}']=B*P==s.zeros(1,N)
 checks[f'weighted_self_adjoint_projection_{N}']=P.T*W==W*P
 checks[f'augmented_observer_faithful_{N}']=B.col_join(P).rank()==N
 sections[str(N)]={'budget':str(sum(q)),'operator_norm_squared':str(gram),'kernel_dimension':N-B.rank()}
# Infinite budget and tail are exact geometric series.
n=s.symbols('n',integer=True,nonnegative=True)
checks['infinite_budget_sum_one']=s.summation(s.Rational(1,2)**(n+1),(n,0,s.oo))==1
for N in (3,5,10): checks[f'tail_budget_{N}']=s.summation(s.Rational(1,2)**(n+1),(n,N,s.oo))==s.Rational(1,2**N)
# Hostile unweighted choice with unit-length collinear columns grows without bound.
checks['unweighted_completion_hostile_diverges']=all(s.Matrix([[1]*N]).norm()>=s.sqrt(N) for N in (3,5,10))
checks['weight_not_source_promoted']=not d['claim_boundary']['weights_source_derived'] and not d['claim_boundary']['source_topology_identified']
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.weighted-common-history-cycle-completion-check.v1','contract_sha256':hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),'checks':checks,'passed':all(checks.values()),'finite_sections':sections,'disposition':{'constructed':'bounded weighted completed synthesis and canonical orthogonal kernel port','bound':'normalized column model has operator norm at most one times the Phi norms','cost':'geometric edge budget depends on enumeration and is not source-derived','next':'source_weight_or_weight_independence_theorem'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'check_count':len(checks),'sections':len(sections)}))
raise SystemExit(0 if result['passed'] else 1)
