#!/usr/bin/env python3
"""Checks for coarse grade equivalence and the properness hostile boundary."""
from pathlib import Path
import hashlib,json,math
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/voevodsky/contracts/projective-edge-grade-equivalence-class.v1.json'
RESULT=ROOT/'research/voevodsky/results/projective_edge_grade_equivalence_class.json'
d=json.loads(CONTRACT.read_text()); primes=(2,3,5,7,11,13,17,19); triples=[(n,p,q) for n in range(1,31) for p in primes for q in primes]
checks={}
checks['sum_grade_equals_reference']=all(math.isclose(math.log(n)+math.log(p)+math.log(q),math.log(n*p*q),abs_tol=1e-14) for n,p,q in triples)
checks['max_lower_bound']=all(max(math.log(n),math.log(p),math.log(q))<=math.log(n*p*q)+1e-14 for n,p,q in triples)
checks['max_upper_comparison']=all(math.log(n*p*q)<=3*max(math.log(n),math.log(p),math.log(q))+1e-14 for n,p,q in triples)
checks['max_grade_reciprocal_invariant']=all(max(math.log(n),math.log(p),math.log(q))==max(math.log(n),math.log(q),math.log(p)) for n,p,q in triples)
# Finite seminorm transport for V between aW-A and bW+B.
for N in (8,16,32):
 W=[math.log((i+1)*2*3) for i in range(N)]; V=[max(math.log(i+1),math.log(2),math.log(3)) for i in range(N)]; c=[(-1)**i/(i+1)**2 for i in range(N)]; delta=.4
 qV=sum(abs(c[i])*math.exp(delta*V[i]) for i in range(N)); qWb=sum(abs(c[i])*math.exp(delta*W[i]) for i in range(N))
 qW=sum(abs(c[i])*math.exp(delta*W[i]) for i in range(N)); qV3=sum(abs(c[i])*math.exp(3*delta*V[i]) for i in range(N))
 checks[f'seminorm_V_by_W_{N}']=qV<=qWb+1e-13
 checks[f'seminorm_W_by_V_{N}']=qW<=qV3+1e-13
# Proper slow grade hostile: transformed W terms fail even to tend to zero.
n=s.symbols('n',positive=True,integer=True)
checks['slow_grade_proper']=s.limit(s.log(1+n),n,s.oo)==s.oo
checks['witness_not_in_reference_exp_space']=s.limit(s.exp(n-s.sqrt(n)),n,s.oo)==s.oo
for power in (1,2,5):
 checks[f'witness_term_decays_in_slow_grade_power_{power}']=s.limit((1+n)**power*s.exp(-s.sqrt(n)),n,s.oo)==0
# Integral comparison after n=u^2: polynomial times exp(-u) is integrable.
u=s.symbols('u',positive=True)
checks['slow_grade_witness_summability_majorant']=all(s.integrate(2*u*(1+u**2)**power*s.exp(-u),(u,1,s.oo))<s.oo for power in (1,2,5))
checks['properness_not_equivalence_disclosed']=not d['claim_boundary']['prior_unspecified_W_in_class_proved']
checks['no_order_or_metric_promotion']=not d['claim_boundary']['edge_order_independence_proved'] and not d['claim_boundary']['physical_or_noise_weight_selected']
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.projective-edge-grade-equivalence-class-check.v1','contract_sha256':hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),'checks':checks,'passed':all(checks.values()),'tested_triples':len(triples),'disposition':{'constructed':'cofinal affine grade class preserving projective topology and continuous history/cycle maps','included':['log(npq)','max(log n,log p,log q)'],'excluded_without_more_evidence':'arbitrary proper grades such as log(1+W_star)','next':'prior_grade_comparability_readback'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'check_count':len(checks),'tested_triples':len(triples)}))
raise SystemExit(0 if result['passed'] else 1)
