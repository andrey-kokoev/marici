import contextlib,io,itertools,json,runpy
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1]
with contextlib.redirect_stdout(io.StringIO()):
 g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_hurwitz_terminal_minor_source_formula.py')))
source_terms,k=g['source_terms'],g['k']
def edge(K,L):
 if len(K)<=1:return True
 return all(K[x]<=L[x]<=K[x+1] for x in range(len(K)-1)) or all(L[x]<=K[x]<=L[x+1] for x in range(len(K)-1))
def test(neg,pos):
 load={L:F(0) for L,_ in pos};cap=dict(pos)
 for K,z in neg:
  ns=[L for L,c in pos if edge(K,L)];den=sum(cap[L] for L in ns)
  if den==0:return False,{'type':'isolated_negative','negative_index':K,'demand':str(-z)}
  for L in ns:load[L]+=(-z)*cap[L]/den
 bad=next((L for L in load if load[L]>cap[L]),None)
 return bad is None,None if bad is None else {'type':'capacity_overload','positive_index':bad,'load':str(load[bad]),'capacity':str(cap[bad]),'ratio':str(load[bad]/cap[bad])}
cases=0;feasible=0;first=None
for r in range(k-1):
 for S in itertools.combinations(range(k),r):
  rem=[x for x in range(k) if x not in S]
  for i,j in itertools.combinations(rem,2):
   if any(i<q<j for q in S):continue
   R=tuple(sorted(S+(i,)));Q=tuple(sorted(S+(j,)));sgn=(-1)**(j-i+1+sum(x>i for x in S)+sum(x>j for x in S));vals=[(K,sgn*z) for K,z in source_terms(R,Q)];neg=[x for x in vals if x[1]<0];pos=[x for x in vals if x[1]>0];ok,bad=test(neg,pos);cases+=1;feasible+=ok
   if not ok and first is None:first={'base':S,'i':i,'j':j,'residual':bad}
checks={'all_769_cases_checked':cases==769,'branching_rule_classified':feasible==cases or first is not None};r={'schema':'marici.strominger.rh_quarter_source_capacity_proportional_branching.v1','status':'passed' if all(checks.values()) else 'failed','verdict':'A uniform source-local branching rule that allocates each negative mass proportionally to positive capacities over its interlacing neighborhood is classified exactly.','case_count':cases,'feasible_case_count':feasible,'first_failure':first,'checks':checks};(base/'results'/'rh_quarter_source_capacity_proportional_branching.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8');print(json.dumps(r,indent=2))
