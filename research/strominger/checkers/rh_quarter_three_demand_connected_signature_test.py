import itertools,json,runpy
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_hurwitz_terminal_minor_source_formula.py')));source_terms,k=g['source_terms'],g['k']
def cover(A,B):
 d=[b-a for a,b in zip(A,B)];return (all(x>=0 for x in d) and sum(d)==1) or (all(x<=0 for x in d) and sum(d)==-1)
cases=0;triples=0;with101=0;found=None
for r in range(k-1):
 if found:break
 for T in itertools.combinations(range(k),r):
  if found:break
  rem=[x for x in range(k) if x not in T]
  for i,j in itertools.permutations(rem,2):
   xs=source_terms(tuple(sorted(T+(i,))),tuple(sorted(T+(j,))));o=1 if sum(v for _,v in xs)>0 else -1;xs=[(K,o*v) for K,v in xs];P=[x for x in xs if x[1]>0];D=[x for x in xs if x[1]<0];cases+=1
   for tri in itertools.combinations(D,3):
    triples+=1;signed=[];witness=[]
    for K,v in P:
     sig=sum(1<<q for q,(L,d) in enumerate(tri) if cover(K,L))
     if sig:signed.append((sig,v,K))
     if sig==5:witness.append(K)
    if not witness:continue
    with101+=1;slacks={m:sum(v for sig,v,K in signed if sig&m)+sum(d for q,(L,d) in enumerate(tri) if m>>q&1) for m in range(1,8)}
    if slacks[7]<min(slacks[m] for m in range(1,7)):
     found={'base':T,'i':i,'j':j,'ordered_demands':[L for L,d in tri],'signature_101_supplies':witness,'active_signatures':sorted({s for s,v,K in signed}),'slacks':{str(m):str(z) for m,z in slacks.items()},'triple_index':triples};break
   if found:break
result={'schema':'marici.strominger.rh_quarter_three_demand_connected_signature_test.v1','status':'failed' if found else 'passed','terminal_cases_reached':cases,'triples_tested':triples,'triples_with_101':with101,'first_independent_101':found,'verdict':'Lex-ordered chain-interval signature compression fails.' if found else 'No tested independent cell has disconnected signature 101.','checks':{'triples_tested':triples>0,'connected_signature_conjecture':found is None}}
(base/'results'/'rh_quarter_three_demand_connected_signature_test.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
