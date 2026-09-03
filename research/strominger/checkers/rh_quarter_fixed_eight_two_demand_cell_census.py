import itertools,json,runpy
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_hurwitz_terminal_minor_source_formula.py')));source_terms,k=g['source_terms'],g['k']
def cover(A,B):
 d=[b-a for a,b in zip(A,B)];return (all(x>=0 for x in d) and sum(d)==1) or (all(x<=0 for x in d) and sum(d)==-1)
cases=0;pairs=0;independent=0;paths=0;endpoint_paths=0;first_other=None;topologies={}
for r in range(k-1):
 for T in itertools.combinations(range(k),r):
  rem=[x for x in range(k) if x not in T]
  for i,j in itertools.permutations(rem,2):
   xs=source_terms(tuple(sorted(T+(i,))),tuple(sorted(T+(j,))));o=1 if sum(v for _,v in xs)>0 else -1;xs=[(K,o*v) for K,v in xs];P=[x for x in xs if x[1]>0];D=[x for x in xs if x[1]<0];cases+=1
   for (L0,v0),(L1,v1) in itertools.combinations(D,2):
    pairs+=1;N0=[x for x in P if cover(x[0],L0)];N1=[x for x in P if cover(x[0],L1)];U={K:v for K,v in N0+N1};s0=sum(v for K,v in N0)+v0;s1=sum(v for K,v in N1)+v1;sc=sum(U.values())+v0+v1
    if sc>=min(s0,s1):continue
    independent+=1;edges=[(K,L) for K in U for L in (L0,L1) if cover(K,L)];pdeg=sorted(sum(a==K for a,b in edges) for K in U);ddeg=sorted(sum(b==L for a,b in edges) for L in (L0,L1));key=f'P{len(U)}-E{len(edges)}-p{pdeg}-d{ddeg}';topologies[key]=topologies.get(key,0)+1;path=len(U)==3 and pdeg==[1,1,2] and ddeg==[2,2];paths+=path
    regime=path and all(-v>=sum(a for K,a in U.items() if sum(cover(K,L) for L in (L0,L1))==1 and cover(K,Li)) for Li,v in ((L0,v0),(L1,v1)))
    endpoint_paths+=regime
    if (not path or not regime) and first_other is None:first_other={'base':T,'i':i,'j':j,'demands':[L0,L1],'positive_neighbors':list(U),'edges':edges,'topology':key,'path':path,'endpoint_deficit_regime':regime,'slacks':list(map(str,(s0,s1,sc)))}
result={'schema':'marici.strominger.rh_quarter_fixed_eight_two_demand_cell_census.v1','status':'passed','terminal_cases':cases,'negative_pairs':pairs,'independent_two_demand_cells':independent,'five_vertex_paths':paths,'endpoint_deficit_paths':endpoint_paths,'topology_counts':topologies,'first_non_path_or_regime':first_other,'verdict':'Five-vertex endpoint-deficit paths are not universal.' if first_other else 'Every independent fixed-eight two-demand cell is an endpoint-deficit five-vertex path.','checks':{'all_cases':cases==3584,'independent_cells_found':independent>0,'universal_path_regime':first_other is None}}
(base/'results'/'rh_quarter_fixed_eight_two_demand_cell_census.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
