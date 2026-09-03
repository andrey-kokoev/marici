import itertools,json,runpy
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_hurwitz_terminal_minor_source_formula.py')));source_terms,k=g['source_terms'],g['k']
def cover(A,B):
 d=[b-a for a,b in zip(A,B)];return (all(x>=0 for x in d) and sum(d)==1) or (all(x<=0 for x in d) and sum(d)==-1)
cases=triples=all7=0;found=None;max_active=0;max_example=None
for r in range(k-1):
 if found:break
 for T in itertools.combinations(range(k),r):
  if found:break
  rem=[x for x in range(k) if x not in T]
  for i,j in itertools.permutations(rem,2):
   xs=source_terms(tuple(sorted(T+(i,))),tuple(sorted(T+(j,))));o=1 if sum(v for _,v in xs)>0 else -1;xs=[(K,o*v) for K,v in xs];P=[x for x in xs if x[1]>0];D=[x for x in xs if x[1]<0];cases+=1
   for tri in itertools.combinations(D,3):
    triples+=1;signed=[]
    for K,v in P:
     sig=sum(1<<q for q,(L,d) in enumerate(tri) if cover(K,L))
     if sig:signed.append((sig,v,K))
    active=sorted({s for s,v,K in signed})
    if len(active)>max_active:max_active=len(active);max_example={'base':T,'i':i,'j':j,'demands':[L for L,d in tri],'active_signatures':active,'triple_index':triples}
    if len(active)<7:continue
    all7+=1;slacks={m:sum(v for sig,v,K in signed if sig&m)+sum(d for q,(L,d) in enumerate(tri) if m>>q&1) for m in range(1,8)}
    if slacks[7]<min(slacks[m] for m in range(1,7)):
     found={'base':T,'i':i,'j':j,'demands':[L for L,d in tri],'active_signatures':active,'slacks':{str(m):str(z) for m,z in slacks.items()},'triple_index':triples};break
   if found:break
result={'schema':'marici.strominger.rh_quarter_fixed_eight_seven_signature_sharpness.v1','status':'passed' if found else 'not_found','terminal_cases_reached':cases,'triples_tested':triples,'all_seven_signature_triples':all7,'maximum_active_signatures':max_active,'first_maximum_example':max_example,'first_independent_all_seven':found,'verdict':'The 2^3-1 signature bound is attained by an independent fixed-eight cell.' if found else 'No independent fixed-eight cell attaining all seven signatures was found in the complete scan.'}
(base/'results'/'rh_quarter_fixed_eight_seven_signature_sharpness.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
