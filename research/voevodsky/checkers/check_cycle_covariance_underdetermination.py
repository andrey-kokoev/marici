#!/usr/bin/env python3
"""Exact nonuniqueness check for coherent cycle metrics."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/structural_coherence_does_not_select_a_cycle_covariance_20260912.md'
RESULT=ROOT/'research/voevodsky/results/cycle_covariance_underdetermination.json'
primes=(2,3,5,7,11,13,17); shells=list(zip(primes,primes[1:])); L=240
E=sorted([(k*p*q,k,p,q) for p,q in shells for k in range(1,L+1) if k*p*q<=L]); V=sorted({k*p for w,k,p,q in E}|{k*q for w,k,p,q in E}); vi={v:i for i,v in enumerate(V)}; B=s.zeros(len(V),len(E))
for j,(w,k,p,q) in enumerate(E): B[vi[k*p],j]-=1; B[vi[k*q],j]+=1
def forest(reverse=False):
 order=sorted(range(len(E)),key=lambda j:(E[j][0],(-E[j][1],-E[j][2]) if reverse else (E[j][1],E[j][2]))); parent=list(range(len(V)))
 def find(x):
  while parent[x]!=x: parent[x]=parent[parent[x]]; x=parent[x]
  return x
 T=[]
 for j in order:
  w,k,p,q=E[j]; a,b=find(vi[k*p]),find(vi[k*q])
  if a!=b: parent[a]=b; T.append(j)
 K=[j for j in range(len(E)) if j not in T]; cols=[]
 for qidx in K:
  x=s.zeros(len(E),1); x[qidx]=1; sol=list(s.linsolve((B[:-1,T],-B[:-1,qidx])))[0]
  for j,v in zip(T,sol): x[j]=v
  cols.append(x)
 return s.Matrix.hstack(*cols),K
FT,KT=forest(False); FU,KU=forest(True); C=FU.gauss_jordan_solve(FT)[0]
W0=s.eye(len(E)); W1=s.diag(*[e[0] for e in E]); Q0T=FT.T*W0*FT; Q1T=FT.T*W1*FT; Q0U=FU.T*W0*FU; Q1U=FU.T*W1*FU
checks={
 'cycle_dimension_nontrivial':FT.cols>1 and B*FT==s.zeros(B.rows,FT.cols),
 'unweighted_positive_definite':FT.rank()==FT.cols and W0.is_positive_definite is True,
 'arithmetic_positive_definite':FT.rank()==FT.cols and W1.is_positive_definite is True,
 'unweighted_forest_congruence':Q0T==C.T*Q0U*C,
 'arithmetic_forest_congruence':Q1T==C.T*Q1U*C,
 'integral_presentation_change':all(x.q==1 for x in C) and abs(C.det())==1,
}
# Scalar proportionality would force every corresponding nonzero entry ratio equal.
ratios={s.cancel(Q1T[i,j]/Q0T[i,j]) for i in range(Q0T.rows) for j in range(Q0T.cols) if Q0T[i,j]!=0}
checks['forms_not_scalar_proportional']=len(ratios)>1
# Old-edge blocks of global diagonal forms are exactly cutoff restrictions.
small=[i for i,e in enumerate(E) if e[0]<=120]
checks['cutoff_restriction_W0']=W0.extract(small,small)==s.eye(len(small))
checks['cutoff_restriction_W1']=W1.extract(small,small)==s.diag(*[E[i][0] for i in small])
text=PACKET.read_text(); checks['physical_selection_not_claimed']='Neither is called physical' in text
checks['authority_blocker_recorded']='covariance branch reaches an authority blocker' in text
checks['reopening_condition_typed']='source-derived readout or covariance is supplied' in text
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.cycle-covariance-underdetermination-check.v1','input_digest':hashlib.sha256(PACKET.read_bytes()).hexdigest(),'checks':checks,'passed':all(checks.values()),'cycle_dimension':FT.cols,'distinct_entry_ratios':len(ratios),'disposition':{'refuted':'structural coherence uniquely selects cycle covariance','witnesses':['unit edge form','arithmetic product edge form'],'remaining':'independently sourced cycle readout/covariance'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n'); print(json.dumps({'passed':result['passed'],'check_count':len(checks),'cycle_dimension':FT.cols,'ratio_count':len(ratios)})); raise SystemExit(0 if result['passed'] else 1)
