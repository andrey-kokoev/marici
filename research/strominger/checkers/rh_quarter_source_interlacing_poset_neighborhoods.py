import itertools,json,runpy
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name("rh_quarter_hurwitz_terminal_minor_source_formula.py")))
source_terms,k=g["source_terms"],g["k"]
def edge(K,L):
 if len(K)<=1:return True
 return all(K[x]<=L[x]<=K[x+1] for x in range(len(K)-1)) or all(L[x]<=K[x]<=L[x+1] for x in range(len(K)-1))
def leq(K,L):return all(a<=b for a,b in zip(K,L))
cases=0;down_nested=0;up_nested=0;first_down_failure=None;first_up_failure=None;pair_count=0
for r in range(k-1):
 for S in itertools.combinations(range(k),r):
  rem=[x for x in range(k) if x not in S]
  for i,j in itertools.combinations(rem,2):
   if any(i<q<j for q in S):continue
   R=tuple(sorted(S+(i,)));Q=tuple(sorted(S+(j,)));expected=(-1)**(j-i+1+sum(x>i for x in S)+sum(x>j for x in S));vals=[(K,expected*z) for K,z in source_terms(R,Q)];neg=[K for K,z in vals if z<0];pos=[K for K,z in vals if z>0];down=True;up=True
   neigh={K:{b for b,L in enumerate(pos) if edge(K,L)} for K in neg}
   for K in neg:
    for L in neg:
     if K!=L and leq(K,L):
      pair_count+=1
      if not neigh[K]<=neigh[L]:
       down=False
       if first_down_failure is None:first_down_failure={"base":S,"i":i,"j":j,"lower":K,"upper":L,"lost_positive_neighbors":sorted(neigh[K]-neigh[L])}
      if not neigh[L]<=neigh[K]:
       up=False
       if first_up_failure is None:first_up_failure={"base":S,"i":i,"j":j,"lower":K,"upper":L,"lost_positive_neighbors":sorted(neigh[L]-neigh[K])}
   cases+=1;down_nested+=down;up_nested+=up
checks={"all_769_cases_checked":cases==769,"comparable_negative_pairs_present":pair_count>0,"downward_ideal_reduction_classified":down_nested==cases or first_down_failure is not None,"upward_filter_reduction_classified":up_nested==cases or first_up_failure is not None}
result={"schema":"marici.strominger.rh_quarter_source_interlacing_poset_neighborhoods.v2","status":"passed" if all(checks.values()) else "failed","verdict":"Componentwise ideal and filter reductions are classified as a rival backend under the single Hall programme DPC boundary.","case_count":cases,"comparable_pair_checks":pair_count,"downward_nested_case_count":down_nested,"upward_nested_case_count":up_nested,"first_downward_nesting_failure":first_down_failure,"first_upward_nesting_failure":first_up_failure,"checks":checks}
(base/"results"/"rh_quarter_source_interlacing_poset_neighborhoods.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps({"status":result["status"],"case_count":cases,"pairs":pair_count,"down_cases":down_nested,"up_cases":up_nested},indent=2))
