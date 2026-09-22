"""Separate exact LP/projection verification and Chebyshev-capacity replay.
Does not import the optimizer or reimplement the owning kernel shape proof.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import json,hashlib,copy
from flint import arb,ctx
ctx.prec=256
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def aq(q):return arb(q.numerator)/q.denominator
r=load(R/'ternary-tail-budget-dpc.json');cp=R/'ternary-tail-budget-dpc-contract.json';c=load(cp)
for p,h in r['bindings'].items():assert sha(Path(p))==h
assert sha(cp)==r['contract_sha256']
branch=load(R/'directed-C-only-Abel-branch.json')
for p,h in branch['bindings'].items():assert sha(Path(p))==h
E=branch['finite_pairing_evidence'];assert E['N']==c['N']==1000000
psi=aq(Q(E['psi_N']['lower'])).union(aq(Q(E['psi_N']['upper'])))
caps=list(map(Q,r['atom_capacity_upper']));budget=list(map(Q,r['prefix_budget_upper']));edges=c['integer_bin_edges'];assert edges==[7000000,7500000,8000000,8500000]
# Re-evaluation at a different precision may enclose the exact stored upper
# rational. Prove containment using the old exact psi endpoint that was used
# in its outward construction, with sufficient precision for a strict check.
ctx.prec=768
for i,(l,h) in enumerate(zip(edges,edges[1:])):
 assert aq(caps[i])>arb(h-l)*arb(h).log()
 # The producing psi interval's lower endpoint is exact rational.
 upper_capacity=2*arb(2).log()*h+arb(h).log()+arb(2).log()-aq(Q(E['psi_N']['lower']))
 assert aq(budget[i])>upper_capacity
A=[];b=[]
for i in range(3):A.append([Q(int(j==i)) for j in range(3)]);b.append(caps[i])
for i in range(3):A.append([Q(int(j<=i)) for j in range(3)]);b.append(budget[i])
assert all(a>=0 for row in A for a in row)
pairs=list(combinations(range(3),2));PA=[];Pb=[]
for pair in pairs:
 for row,bound in zip(A,b):PA.append([a if i in pair else Q(0) for i,a in enumerate(row)]);Pb.append(bound)
weights=[(Q(w['lower']),Q(w['upper'])) for w in r['weights']];assert all(a<=b<0 for a,b in weights)
objective=[w[0] for w in weights]
def check_packet(packet,A,b):
 p=list(map(Q,packet['primal']));y=list(map(Q,packet['dual']));v=Q(packet['value'])
 assert len(p)==3 and len(y)==len(b) and all(z>=0 for z in p+y)
 assert all(sum(a*z for a,z in zip(row,p))<=bound for row,bound in zip(A,b))
 assert all(sum(A[i][j]*y[i] for i in range(len(b)))>=-objective[j] for j in range(3))
 assert sum(a*z for a,z in zip(objective,p))==v==-sum(a*z for a,z in zip(b,y))
 return p,v
full,fullvalue=check_packet(r['full_LP'],A,b);pair,pairvalue=check_packet(r['pairwise_LP'],PA,Pb)
for indices,lift in zip(pairs,r['pair_lifts']):
 assert indices==tuple(lift['pair'])
 p=list(map(Q,lift['full_carrier_lift']));assert p==[v if i in indices else Q(0) for i,v in enumerate(pair)]
 assert all(sum(a*z for a,z in zip(row,p))<=bound for row,bound in zip(A,b))
 # Nonnegative-row downward closure establishes that this zero extension
 # characterizes the ENTIRE existential pair projection, not just this point.
assert sum(pair)>budget[-1]
upper=sum(w[1]*p for w,p in zip(weights,pair));assert upper==Q(r['pair_candidate_upper_cost'])
assert fullvalue-upper==Q(r['robust_gap_lower'])>0
threshold=Q(c['block_threshold']);assert upper<threshold<fullvalue
cut=r['cut_omission'];true=budget[-1]-pair[0]-pair[1];relaxed=min(caps[2],budget[-1]-pair[0],budget[-1]-pair[1])
assert true==Q(cut['true_remaining_budget']) and relaxed==Q(cut['pairwise_remaining_budget']) and true<pair[2]<=relaxed
assert Q(cut['proposed_third_mass'])==pair[2] and r['status']=='CORROBORATED'
# Corruption controls: a pairwise witness cannot be promoted to full admission;
# a zeroed dual cannot certify either negative optimum.
bad=copy.deepcopy(r['full_LP']);bad['primal']=r['pairwise_LP']['primal']
try:check_packet(bad,A,b)
except AssertionError:pass
else:raise AssertionError('false global lift accepted')
bad=copy.deepcopy(r['full_LP']);bad['dual']=['0']*len(bad['dual'])
try:check_packet(bad,A,b)
except AssertionError:pass
else:raise AssertionError('invalid dual accepted')
print('PASS: owning capacity bounds, exact pair projections/lifts, both LP primal-dual certificates, robust kernel-box gap, cut omission, corruption rejection')
