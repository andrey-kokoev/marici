import itertools,json,runpy
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_hurwitz_terminal_minor_source_formula.py')));source_terms,k=g['source_terms'],g['k']
def cover(A,B):
 d=[b-a for a,b in zip(A,B)];return (all(x>=0 for x in d) and sum(d)==1) or (all(x<=0 for x in d) and sum(d)==-1)
cases=0;triples=0;independent=0;first=None;max_signatures=0;max_record=None
for r in range(k-1):
 if first:break
 for T in itertools.combinations(range(k),r):
  if first:break
  rem=[x for x in range(k) if x not in T]
  for i,j in itertools.permutations(rem,2):
   xs=source_terms(tuple(sorted(T+(i,))),tuple(sorted(T+(j,))));o=1 if sum(v for _,v in xs)>0 else -1;xs=[(K,o*v) for K,v in xs];P=[x for x in xs if x[1]>0];D=[x for x in xs if x[1]<0];cases+=1
   for tri in itertools.combinations(D,3):
    triples+=1;signed=[];active=set()
    for K,v in P:
     sig=sum((1<<q) for q,(L,d) in enumerate(tri) if cover(K,L))
     if sig:active.add(sig);signed.append((sig,v,K))
    slacks={m:sum(v for sig,v,K in signed if sig&m)+sum(d for q,(L,d) in enumerate(tri) if m>>q&1) for m in range(1,8)}
    indep=slacks[7]<min(slacks[m] for m in range(1,7));independent+=indep
    if len(active)>max_signatures:max_signatures=len(active);max_record={'base':T,'i':i,'j':j,'demands':[L for L,d in tri],'active_signatures':sorted(active),'slacks':{str(m):str(z) for m,z in slacks.items()}}
    if indep and len(active)>3:
     first={'base':T,'i':i,'j':j,'demands':[L for L,d in tri],'active_signatures':sorted(active),'slacks':{str(m):str(z) for m,z in slacks.items()},'triple_index':triples};break
   if first:break
result={'schema':'marici.strominger.rh_quarter_fixed_eight_three_demand_signature_census.v1','status':'failed' if first else 'passed','terminal_cases_reached':cases,'three_demand_triples_tested':triples,'independent_triples':independent,'maximum_active_signatures':max_signatures,'first_independent_above_three_signatures':first,'verdict':'A fixed-eight independent three-demand cell requires more than three active signatures.' if first else 'No tested independent three-demand cell exceeds three active signatures.','checks':{'triples_tested':triples>0,'three_signature_compression_survives':first is None}}
(base/'results'/'rh_quarter_fixed_eight_three_demand_signature_census.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
