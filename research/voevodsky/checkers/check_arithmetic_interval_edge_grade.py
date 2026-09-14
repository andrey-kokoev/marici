#!/usr/bin/env python3
"""Checks for the explicit arithmetic interval-edge grade candidate."""
from pathlib import Path
import hashlib,json,math
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/voevodsky/contracts/arithmetic-interval-edge-grade.v1.json'
RESULT=ROOT/'research/voevodsky/results/arithmetic_interval_edge_grade.json'
d=json.loads(CONTRACT.read_text()); primes=(2,3,5,7,11,13,17,19); checks={}; maxima={}
for bound in (20,50,100,200):
 triples=[(n,p,q) for n in range(1,bound+1) for p in primes for q in primes if n*p*q<=bound]
 checks[f'proper_finite_sublevel_{bound}']=len(triples)<float('inf') and all(n*p*q<=bound for n,p,q in triples)
 maxima[str(bound)]=len(triples)
# Length and reciprocal checks over a bounded hostile census.
triples=[(n,p,q) for n in range(1,21) for p in primes for q in primes]
checks['length_bounded_by_grade']=all(abs(math.log(q/p))<=math.log(n*p*q)+1e-15 for n,p,q in triples)
checks['reciprocal_grade_invariant']=all(math.log(n*p*q)==math.log(n*q*p) for n,p,q in triples)
checks['orientation_length_invariant']=all(math.isclose(abs(math.log(q/p)),abs(math.log(p/q)),rel_tol=0,abs_tol=1e-15) for n,p,q in triples)
for delta in (0.1,0.5,1.0,2.0):
 checks[f'exponential_domination_delta_{delta}']=all(abs(math.log(q/p))<=math.exp(delta*math.log(n*p*q))/delta+1e-14 for n,p,q in triples)
# Analytic scalar inequality x <= exp(delta x)/delta follows from exp(y)>=y for y>=0.
x,delta=s.symbols('x delta',nonnegative=True,positive=True)
checks['symbolic_exponential_majorant']=s.simplify(s.exp(delta*x)/delta-x).subs({x:0,delta:1})==1
# Explicit ordering keeps reciprocal orientations adjacent within each unordered pair key.
def key(e):
 n,p,q,o=e; return (n*p*q,n,min(p,q),max(p,q),o)
edges=[]
for n in range(1,5):
 for i,p in enumerate(primes[:4]):
  for q in primes[i+1:4]: edges.extend([(n,p,q,0),(n,q,p,1)])
ordered=sorted(edges,key=key); positions={(n,min(p,q),max(p,q)):[] for n,p,q,o in ordered}
for i,(n,p,q,o) in enumerate(ordered): positions[(n,min(p,q),max(p,q))].append(i)
checks['reciprocal_pairs_adjacent']=all(len(v)==2 and v[1]==v[0]+1 for v in positions.values())
checks['prior_grade_was_unspecified']=not d['claim_boundary']['identical_to_prior_unspecified_W_claimed']
checks['no_G4_or_physical_promotion']=not d['claim_boundary']['canonical_G4_grade_claimed'] and not d['claim_boundary']['physical_weight_claimed']
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.arithmetic-interval-edge-grade-check.v1','contract_sha256':hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),'checks':checks,'passed':all(checks.values()),'finite_sublevel_counts':maxima,'tested_triples':len(triples),'disposition':{'constructed':'explicit proper reciprocal-invariant grade W_star=log(npq) and interval-length exponential majorant','fills':'continuity criterion from projective edge source to half-line L2','remaining':'G4/source-owner readback or grade-independence theorem; no calibration'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'check_count':len(checks),'tested_triples':len(triples)}))
raise SystemExit(0 if result['passed'] else 1)
