import contextlib,io,itertools,json,runpy
from pathlib import Path
base=Path(__file__).parents[1]
with contextlib.redirect_stdout(io.StringIO()):
 g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_hurwitz_terminal_minor_source_formula.py')))
source_terms,k=g['source_terms'],g['k']
def edge(K,L):
 if len(K)<=1:return True
 return all(K[x]<=L[x]<=K[x+1] for x in range(len(K)-1)) or all(L[x]<=K[x]<=L[x+1] for x in range(len(K)-1))
def coupling(neg,pos,key):
 neg=[[K,-z] for K,z in sorted(neg,key=lambda x:key(x[0]))];pos=[[K,z] for K,z in sorted(pos,key=lambda x:key(x[0]))];i=j=0;bad=None
 while i<len(neg) and j<len(pos):
  q=min(neg[i][1],pos[j][1])
  if not edge(neg[i][0],pos[j][0]) and bad is None:bad={'negative_index':neg[i][0],'positive_index':pos[j][0],'mass':str(q)}
  neg[i][1]-=q;pos[j][1]-=q
  if neg[i][1]==0:i+=1
  if pos[j][1]==0:j+=1
 return i==len(neg) and bad is None,bad
orders={'lex':lambda K:K,'colex':lambda K:tuple(reversed(K)),'sum_lex':lambda K:(sum(K),K)};stats={n:{'feasible':0,'first_failure':None} for n in orders};cases=0;capacity=0
for r in range(k-1):
 for S in itertools.combinations(range(k),r):
  rem=[x for x in range(k) if x not in S]
  for i,j in itertools.combinations(rem,2):
   if any(i<q<j for q in S):continue
   R=tuple(sorted(S+(i,)));Q=tuple(sorted(S+(j,)));sgn=(-1)**(j-i+1+sum(x>i for x in S)+sum(x>j for x in S));vals=[(K,sgn*z) for K,z in source_terms(R,Q)];neg=[x for x in vals if x[1]<0];pos=[x for x in vals if x[1]>0];cases+=1;capacity+=sum(-z for _,z in neg)<=sum(z for _,z in pos)
   for name,key in orders.items():
    ok,bad=coupling(neg,pos,key);stats[name]['feasible']+=ok
    if not ok and stats[name]['first_failure'] is None:stats[name]['first_failure']={'base':S,'i':i,'j':j,'forbidden_transport':bad}
checks={'all_769_cases_checked':cases==769,'capacity_sufficient':capacity==cases,'all_orders_classified':all(d['feasible']==cases or d['first_failure'] for d in stats.values())};r={'schema':'marici.strominger.rh_quarter_source_canonical_monotone_transport.v1','status':'passed' if all(checks.values()) else 'failed','verdict':'All three preregistered source-derived canonical monotone couplings are classified under one rival backend.','case_count':cases,'orders':stats,'checks':checks};(base/'results'/'rh_quarter_source_canonical_monotone_transport.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8');print(json.dumps(r,indent=2))
