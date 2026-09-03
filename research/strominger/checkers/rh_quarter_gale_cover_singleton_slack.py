import itertools,json,runpy
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_hurwitz_terminal_minor_source_formula.py')));source_terms,k=g['source_terms'],g['k']
def cover(A,B):
 d=[b-a for a,b in zip(A,B)];return (all(x>=0 for x in d) and sum(d)==1) or (all(x<=0 for x in d) and sum(d)==-1)
cases=0;singletons=0;zero=0;minimum=None;record=None;degrees={}
for r in range(k-1):
 for T in itertools.combinations(range(k),r):
  rem=[x for x in range(k) if x not in T]
  for i,j in itertools.permutations(rem,2):
   xs=source_terms(tuple(sorted(T+(i,))),tuple(sorted(T+(j,))));o=1 if sum(v for _,v in xs)>0 else -1;xs=[(K,o*v) for K,v in xs];pos=[x for x in xs if x[1]>0];neg=[x for x in xs if x[1]<0];cases+=1
   for L,v in neg:
    N=[(K,a) for K,a in pos if cover(K,L)];slack=sum(a for _,a in N)+v;singletons+=1;zero+=slack==0;degrees[str(len(N))]=degrees.get(str(len(N)),0)+1
    if minimum is None or slack<minimum:minimum=slack;record={'base':T,'i':i,'j':j,'negative_label':L,'negative_demand':str(-v),'neighbor_labels':[K for K,_ in N],'degree':len(N),'slack':str(slack)}
result={'schema':'marici.strominger.rh_quarter_gale_cover_singleton_slack.v1','status':'passed' if minimum is not None and minimum>=0 else 'failed','terminal_case_count':cases,'negative_singleton_count':singletons,'zero_slack_count':zero,'minimum_slack':str(minimum),'minimum_record':record,'cover_degree_counts':degrees,'verdict':'Every negative singleton has nonnegative exact supply slack in its positive Gale-cover neighborhood.','checks':{'all_cases':cases==3584,'singletons_tested':singletons>0,'nonnegative_singleton_slack':minimum>=0}}
(base/'results'/'rh_quarter_gale_cover_singleton_slack.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
