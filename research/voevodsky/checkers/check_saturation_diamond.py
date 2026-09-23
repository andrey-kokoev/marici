"""Exact saturation diamonds for actual A/B continuation observers.

For a carrier P' fixed independently, saturation is union of the fibers of
its restricted observer map. Exhaust all carriers and all evidence subsets.
"""
from pathlib import Path
from itertools import combinations
import subprocess
import sys
import json
import hashlib
ROOT=Path(__file__).resolve().parents[3]
DIR=ROOT/'research/voevodsky/results/continuation-quotient'
subprocess.run([sys.executable,str(Path(__file__).with_name('check_common_continuation_refinement.py'))],check=True,capture_output=True,text=True)
p=DIR/'common-continuation-refinement.json';r=json.loads(p.read_text())
L=r['quotients']['A_only'];M=r['quotients']['B_only'];P=set(L)
def subsets(S):
 s=sorted(S)
 for n in range(len(s)+1):
  for t in combinations(s,n):yield frozenset(t)
def sat(C,Q,carrier):return frozenset(x for x in carrier if any(Q[x]==Q[y] for y in C))
def kernel(Q,carrier):return {(a,b) for a in carrier for b in carrier if Q[a]==Q[b]}
def compose(R,S):return {(a,c) for a,b in R for bb,c in S if b==bb}
full_failures=[];restriction_results=[];equivalence_checks=0
for carrier in subsets(P):
 KL,KM=kernel(L,carrier),kernel(M,carrier)
 LM,ML=compose(KL,KM),compose(KM,KL)
 failures=[]
 for C in subsets(carrier):
  left=sat(sat(C,L,carrier),M,carrier)
  right=sat(sat(C,M,carrier),L,carrier)
  # Fiber saturation is relational image. Sets agree for all C iff singleton
  # images agree, equivalently the composed kernel relations agree.
  assert left==frozenset(b for a,b in LM if a in C)
  assert right==frozenset(b for a,b in ML if a in C)
  if left!=right:failures.append({'C':sorted(C),'L_then_M':sorted(left),'M_then_L':sorted(right)})
  equivalence_checks+=1
 assert (not failures)==(LM==ML)
 restriction_results.append({'carrier':sorted(carrier),'commutes':not failures,'failure_count':len(failures)})
 if carrier==P:full_failures=failures
assert full_failures
C=frozenset({'A'})
assert sat(sat(C,L,P),M,P)==frozenset({'P','A','B'})
assert sat(sat(C,M,P),L,P)==frozenset({'P','A'})
# Witness: A --L--> P --M--> B; no reversed middle witness exists.
assert L['A']==L['P'] and M['P']==M['B']
reverse_middles={x for x in P if M['A']==M[x] and L[x]==L['B']}
assert not reverse_middles
# Alternation to closure recovers the join of the kernel equivalences, not
# the source's primitive evidence merge AB.
fixed={}
for C in subsets(P):
 X=C;rounds=0
 while True:
  Y=sat(sat(X,L,P),M,P);rounds+=1
  if Y==X:break
  X=Y
 fixed[','.join(sorted(C))]={'closure':sorted(X),'rounds':rounds}
 assert sat(X,L,P)==X and sat(X,M,P)==X
# Joint observation is instead the intersection of kernels: here injective.
for C in subsets(P):
 joint=frozenset(x for x in P if any((L[x],M[x])==(L[y],M[y]) for y in C))
 assert joint==C
# Source restrictions can remove obstruction by deleting its middle or end.
assert next(x for x in restriction_results if set(x['carrier'])=={'A','B','AB'})['commutes']
assert all(x['commutes']==(not {'P','A','B'}<=set(x['carrier'])) for x in restriction_results)
report={'passed':True,'input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
 'source_states':sorted(P),'L':L,'M':M,
 'full_source_subset_count':16,'full_source_noncommuting_subsets':full_failures,
 'alternating_witness':{'path':['A','P','B'],'relations':['L','M'],'opposite_order_middle_witnesses':[]},
 'carrier_restrictions_tested':len(restriction_results),'carrier_subset_checks':equivalence_checks,
 'restricted_carrier_results':restriction_results,
 'exact_criterion':'For all evidence subsets C, S_M S_L(C)=S_L S_M(C) iff K_L composed with K_M equals K_M composed with K_L. Every alternating witness then has a reversed-order middle witness (existence, not canonical witness equivalence).',
 'actual_restriction_criterion':'Noncommutation occurs exactly when the restricted source retains P,A,B together.',
 'joint_observation_saturation':'identity on all subsets: paired observations distinguish every source state',
 'alternating_closure_of_A':fixed['A'],
 'distinction':'Alternating saturation forgets distinctions and yields {P,A,B}; jointly retaining the observations preserves {A}. Neither is the primitive-evidence merge AB.',
 'scope':'Exact finite source-bound evidence family. Restricting the source carrier changes the closure operator; performing evidence intersection with the original source fixed is a different operation.'}
(DIR/'saturation-diamond.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ('restricted_carrier_results','full_source_noncommuting_subsets')},indent=2))
