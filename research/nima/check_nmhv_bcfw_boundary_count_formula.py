#!/usr/bin/env python3
"""Exact finite-range census of physical and spurious NMHV BCFW divisors."""
import json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def canonical(q):return tuple(sorted(q))
def denominators(q):return [canonical(q[i+1:]+q[:i]) for i in range(5)]
def physical(q,n):
 S=set(q);adj=[{i,i%n+1} for i in range(1,n+1)]
 return any(a<=S and b<=S and a.isdisjoint(b) for a in adj for b in adj)
rows=[];passed=True
for n in range(6,51):
 terms=tuple((n,i-1,i,j-1,j) for i in range(2,n-1) for j in range(i+2,n))
 incidence=Counter(d for q in terms for d in denominators(q));phys={q for q in incidence if physical(q,n)};spur={q for q,k in incidence.items() if not physical(q,n)}
 checks={'bcfw_terms':len(terms)==(n-3)*(n-4)//2,'physical_divisors':len(phys)==n*(n-3)//2,'spurious_divisors':len(spur)==(n-5)*(n-3),'every_physical_divisor_is_external_incidence_one':all(incidence[q]==1 for q in phys),'every_spurious_divisor_is_internal_incidence_two':all(incidence[q]==2 for q in spur),'boundary_incidence_balance':5*len(terms)==len(phys)+2*len(spur),'all_denominators_classified':len(phys|spur)==len(incidence)}
 ok=all(checks.values());passed &= ok;rows.append({'multiplicity':n,'terms':len(terms),'physical_divisors':len(phys),'spurious_divisors':len(spur),'physical_incidence_histogram':{str(k):sum(incidence[q]==k for q in phys) for k in sorted(set(incidence[q] for q in phys))},'spurious_incidence_histogram':{str(k):sum(incidence[q]==k for q in spur) for k in sorted(set(incidence[q] for q in spur))},'checks':checks,'passed':ok})
out={'schema':'marici.nima.nmhv-bcfw-boundary-count-formula.v1','benchmark':{'result':'codimension-one boundary census of the standard NMHV momentum-twistor BCFW representation','context':'positive Grassmannian/amplituhedron triangulation'},'range':{'min_multiplicity':6,'max_multiplicity':50},'formulas':{'bcfw_terms':'(n-3)(n-4)/2','physical_divisors':'n(n-3)/2','spurious_divisors':'(n-5)(n-3)','incidence_balance':'5 N_BCFW = N_physical + 2 N_spurious'},'geometric_interpretation':'Each five-bracket is a simplex with five facets; physical facets occur once on the exterior and spurious facets occur twice as glued internal boundaries.','results':rows,'passed':passed,'scope':'Exact combinatorial verification for every integer n=6,...,50; not an inductive proof for arbitrary n.'}
p=ROOT/'research/nima/results/nmhv-bcfw-boundary-count-formula.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':passed,'range':[6,50],'last':rows[-1]},indent=2));raise SystemExit(0 if passed else 1)
