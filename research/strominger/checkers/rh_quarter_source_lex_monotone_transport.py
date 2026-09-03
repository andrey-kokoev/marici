import contextlib,io,itertools,json,runpy
from pathlib import Path
base=Path(__file__).parents[1]
with contextlib.redirect_stdout(io.StringIO()):
 g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_hurwitz_terminal_minor_source_formula.py')))
source_terms,k=g['source_terms'],g['k']
def edge(K,L):
 if len(K)<=1:return True
 return all(K[x]<=L[x]<=K[x+1] for x in range(len(K)-1)) or all(L[x]<=K[x]<=L[x+1] for x in range(len(K)-1))
def monotone(neg,pos):
 neg=[[K,-z] for K,z in sorted(neg)];pos=[[K,z] for K,z in sorted(pos)];i=j=0;support=[]
 while i<len(neg) and j<len(pos):
  q=min(neg[i][1],pos[j][1]);support.append((neg[i][0],pos[j][0],q,edge(neg[i][0],pos[j][0])));neg[i][1]-=q;pos[j][1]-=q
  if neg[i][1]==0:i+=1
  if pos[j][1]==0:j+=1
 return support,i==len(neg)
cases=0;feasible=0;first=None;capacity_cases=0
for r in range(k-1):
 for S in itertools.combinations(range(k),r):
  rem=[x for x in range(k) if x not in S]
  for i,j in itertools.combinations(rem,2):
   if any(i<q<j for q in S):continue
   R=tuple(sorted(S+(i,)));Q=tuple(sorted(S+(j,)));sgn=(-1)**(j-i+1+sum(x>i for x in S)+sum(x>j for x in S));vals=[(K,sgn*z) for K,z in source_terms(R,Q)];neg=[x for x in vals if x[1]<0];pos=[x for x in vals if x[1]>0];support,balanced=monotone(neg,pos);capacity_ok=sum(-z for _,z in neg)<=sum(z for _,z in pos);ok=balanced and all(x[3] for x in support);cases+=1;feasible+=ok;capacity_cases+=capacity_ok
   if not ok and first is None:
    bad=next((x for x in support if not x[3]),None);first={'base':S,'i':i,'j':j,'balanced':balanced,'forbidden_transport':None if bad is None else {'negative_index':bad[0],'positive_index':bad[1],'mass':str(bad[2])}}
checks={'all_769_cases_checked':cases==769,'negative_demand_within_positive_capacity':capacity_cases==cases,'lex_monotone_rival_classified':feasible==cases or first is not None}
r={'schema':'marici.strominger.rh_quarter_source_lex_monotone_transport.v1','status':'passed' if all(checks.values()) else 'failed','verdict':'The canonical lexicographic monotone coupling is tested directly against source interlacing, independently of neighborhood convexity.','case_count':cases,'feasible_case_count':feasible,'first_failure':first,'checks':checks};(base/'results'/'rh_quarter_source_lex_monotone_transport.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8');print(json.dumps(r,indent=2))
