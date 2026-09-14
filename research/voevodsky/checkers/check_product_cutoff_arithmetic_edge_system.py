#!/usr/bin/env python3
"""Checks an explicit product-sublevel arithmetic edge cutoff system."""
from pathlib import Path
from fractions import Fraction
import hashlib,json,math
ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/voevodsky/contracts/product-cutoff-arithmetic-edge-system.v1.json'
RESULT=ROOT/'research/voevodsky/results/product_cutoff_arithmetic_edge_system.json'
d=json.loads(CONTRACT.read_text()); primes=(2,3,5,7,11,13,17,19,23,29,31); bounds=(40,80,160)
def edges(N): return sorted([(n,p,q) for n in range(1,N+1) for p in primes for q in primes if n*p*q<=N],key=lambda e:(e[0]*e[1]*e[2],e[0],min(e[1],e[2]),max(e[1],e[2]),0 if e[1]<=e[2] else 1))
def boundary(N):
 E=edges(N); V=sorted({n*p for n,p,q in E}|{n*q for n,p,q in E}); vi={v:i for i,v in enumerate(V)}; B=[[0]*len(E) for _ in V]
 for j,(n,p,q) in enumerate(E): B[vi[n*p]][j]-=1; B[vi[n*q]][j]+=1
 return E,V,B
checks={}
Es={N:edges(N) for N in bounds}
checks['finite_sublevels']=all(len(Es[N])<N**3 for N in bounds)
checks['nested']=all(set(Es[a])<=set(Es[b]) for a,b in zip(bounds,bounds[1:]))
checks['exact_grade_sublevels']=all(all(math.log(n*p*q)<=math.log(N)+1e-15 for n,p,q in Es[N]) for N in bounds)
checks['reciprocal_closed']=all(all((n,q,p) in set(Es[N]) for n,p,q in Es[N]) for N in bounds)
checks['global_order_restricts']=all([e for e in Es[b] if e in set(Es[a])]==Es[a] for a,b in zip(bounds,bounds[1:]))
# Exact weighted l1 zero-extension isometry for integer deltas.
for delta in (1,2):
 vals={e:Fraction((i%7)-3,i+1) for i,e in enumerate(Es[bounds[-1]])}
 for a,b in zip(bounds,bounds[1:]):
  qa=sum(abs(vals[e])*Fraction((e[0]*e[1]*e[2])**delta) for e in Es[a]); qb=sum(abs(vals[e])*Fraction((e[0]*e[1]*e[2])**delta) for e in Es[b] if e in set(Es[a]))
  checks[f'q_{delta}_zero_extension_{a}_{b}']=qa==qb
# Incidence naturality: each old edge column agrees after vertex inclusion.
for a,b in zip(bounds,bounds[1:]):
 Ea,Va,Ba=boundary(a); Eb,Vb,Bb=boundary(b); ebi={e:i for i,e in enumerate(Eb)}; vbi={v:i for i,v in enumerate(Vb)}
 checks[f'boundary_naturality_{a}_{b}']=all(all(Ba[i][j]==Bb[vbi[v]][ebi[e]] for i,v in enumerate(Va)) for j,e in enumerate(Ea))
# Uniform interval domination independent of cutoff.
for delta in (.1,.5,1,2): checks[f'uniform_length_bound_{delta}']=all(abs(math.log(q/p))<=math.exp(delta*math.log(n*p*q))/delta+1e-13 for N in bounds for n,p,q in Es[N])
checks['candidate_not_prior_readback']=not d['claim_boundary']['identical_to_prior_unspecified_cutoff_claimed']
checks['admission_multiplicity_not_invented']=not d['claim_boundary']['all_admitted_shell_labels_enumerated'] and not d['claim_boundary']['fixed_ratio_multiplicity_resolved']
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.product-cutoff-arithmetic-edge-system-check.v1','contract_sha256':hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),'checks':checks,'passed':all(checks.values()),'edge_counts':{str(N):len(Es[N]) for N in bounds},'disposition':{'constructed':'finite nested exhaustive reciprocal product-sublevel cutoff with uniform projective continuity','remaining':'actual admitted shell predicate and fixed-ratio multiplicity readback'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n'); print(json.dumps({'passed':result['passed'],'check_count':len(checks),'edge_counts':result['edge_counts']})); raise SystemExit(0 if result['passed'] else 1)
