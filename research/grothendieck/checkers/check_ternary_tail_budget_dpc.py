"""Higher-arity loss in an owning Chebyshev-derived three-bin moment carrier."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import json,hashlib,runpy
from flint import arb
from sympy import Rational
from sympy.solvers.simplex import linprog
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
cp=R/'ternary-tail-budget-dpc-contract.json';contract=load(cp);ch=sha(cp)
z=runpy.run_path(str(HERE/'check_combined_tail_single_valley.py'));assert z['status']=='CORROBORATED'
x=z['x'];aq=x['aq'];ends=x['ends'];kernel=x['kernel'];ts=x['ts'];root=aq(z['root'][0]).union(aq(z['root'][1]))
def K(u):
 i=next(i for i in range(len(ts)-1) if aq(ts[i])<u<aq(ts[i+1]));return kernel(u,i)[0]
psi=aq(x['psi'][0]).union(aq(x['psi'][1]));edges=contract['integer_bin_edges'];assert edges==[7000000,7500000,8000000,8500000]
weights=[];caps=[];budgets=[]
for l,r in zip(edges,edges[1:]):
 lo=arb(l).log();hi=arb(r).log();values=[K(lo),K(hi)]
 # Single-valley theorem gives exact locations of all extrema on the bin.
 if lo<root<hi:values.append(K(root))
 else:assert root<lo or hi<root
 weights.append((min(ends(v)[0] for v in values),max(ends(v)[1] for v in values)))
 caps.append(ends(arb(r-l)*hi)[1]);budgets.append(ends(x['capacity'](hi)-psi)[1])
assert all(a<=b<0 for a,b in weights)
A=[];b=[]
for i in range(3):A.append([Q(int(i==j)) for j in range(3)]);b.append(caps[i])
for i in range(3):A.append([Q(int(j<=i)) for j in range(3)]);b.append(budgets[i])
# All rows are nonnegative upper bounds: every pair projection is exactly
# obtained by setting the omitted coordinate to zero. This proves both
# directions of existential projection, not only necessary pair inequalities.
pairs=list(combinations(range(3),2));PA=[];Pb=[]
for pair in pairs:
 for row,bound in zip(A,b):PA.append([v if i in pair else Q(0) for i,v in enumerate(row)]);Pb.append(bound)
def sp(q):return Rational(q.numerator,q.denominator)
def packet(AA,bb,c):
 value,p=linprog(list(map(sp,c)),[list(map(sp,row)) for row in AA],list(map(sp,bb)))
 _,y=linprog(list(map(sp,bb)),[[-sp(AA[i][j]) for i in range(len(AA))] for j in range(3)],list(map(sp,c)))
 p=[Q(str(t)) for t in p];y=[Q(str(t)) for t in y];v=Q(str(value))
 assert all(t>=0 for t in p+y) and all(sum(a*t for a,t in zip(row,p))<=bound for row,bound in zip(AA,bb))
 assert all(sum(AA[i][j]*y[i] for i in range(len(AA)))>=-c[j] for j in range(3))
 assert sum(a*t for a,t in zip(c,p))==v==-sum(a*t for a,t in zip(bb,y))
 return {'value':str(v),'primal':list(map(str,p)),'dual':list(map(str,y))}
lower=[v[0] for v in weights];upper=[v[1] for v in weights]
full=packet(A,b,lower);pair=packet(PA,Pb,lower);candidate=list(map(Q,pair['primal']))
assert sum(candidate)>budgets[-1]
lifts=[]
for indices in pairs:
 lift=[v if i in indices else Q(0) for i,v in enumerate(candidate)]
 assert all(sum(a*t for a,t in zip(row,lift))<=bound for row,bound in zip(A,b))
 lifts.append({'pair':list(indices),'full_carrier_lift':list(map(str,lift))})
# Even the pair candidate's UPPER kernel cost is below the full carrier's
# LOWER cost. This robust gap is not an artefact of choosing interval endpoints.
pair_upper=sum(a*t for a,t in zip(upper,candidate));full_lower=Q(full['value']);gap=full_lower-pair_upper
threshold=Q(contract['block_threshold']);status='CORROBORATED' if pair_upper<threshold<full_lower else 'UNRESOLVED'
assert gap>0
# After first two masses, source admission requires remaining total budget,
# not merely each pair's budget. The candidate witnesses failure of omission.
remaining=budgets[-1]-candidate[0]-candidate[1]
pair_remaining=min(caps[2],budgets[-1]-candidate[0],budgets[-1]-candidate[1])
assert candidate[2]>remaining and candidate[2]<=pair_remaining
assert sha(cp)==ch
out={'schema':'ternary-tail-budget-dpc-result.v1','status':status,'contract_sha256':ch,'weights':[x['enc'](w) for w in weights],'atom_capacity_upper':list(map(str,caps)),'prefix_budget_upper':list(map(str,budgets)),'full_LP':full,'pairwise_LP':pair,'pair_lifts':lifts,'pair_candidate_upper_cost':str(pair_upper),'robust_gap_lower':str(gap),'block_threshold':str(threshold),'cut_omission':{'true_remaining_budget':str(remaining),'pairwise_remaining_budget':str(pair_remaining),'proposed_third_mass':str(candidate[2])},'bindings':{str(p):sha(p) for p in (Path(__file__),cp,HERE/'check_combined_tail_single_valley.py',R/'combined-tail-single-valley.json',R/'directed-C-only-Abel-branch.json')},'scope':'Exact pair projections of the declared rational moment relaxation, not projections of actual prime-realizable measures. Local block separation only.'}
(R/'ternary-tail-budget-dpc.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':status,'full_lower':float(full_lower),'pair_candidate_upper':float(pair_upper),'robust_gap':float(gap),'threshold':float(threshold)},indent=2))
