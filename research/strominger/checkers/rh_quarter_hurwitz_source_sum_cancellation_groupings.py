import itertools,json,runpy
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name("rh_quarter_hurwitz_terminal_minor_source_formula.py")))
source_terms,k=g["source_terms"],g["k"]
schemes={
 "sum_K":lambda K,T,i,j:sum(K),
 "min_K":lambda K,T,i,j:min(K),
 "max_K":lambda K,T,i,j:max(K),
 "intersection_with_base_size":lambda K,T,i,j:len(set(K)&set(T)),
 "symmetric_difference_from_rows_size":lambda K,T,i,j:len(set(K)^set(T+(i,))),
 "inside_terminal_interval_size":lambda K,T,i,j:sum(min(i,j)<=x<=max(i,j) for x in K),
 "below_terminal_interval_size":lambda K,T,i,j:sum(x<min(i,j) for x in K),
 "above_terminal_interval_size":lambda K,T,i,j:sum(x>max(i,j) for x in K),
}
stats={name:{"group_count":0,"bad_group_count":0,"zero_group_count":0,"first_bad":None} for name in schemes};cases=0
for r in range(k-1):
 for T in itertools.combinations(range(k),r):
  rem=[x for x in range(k) if x not in T]
  for i,j in itertools.permutations(rem,2):
   R=tuple(sorted(T+(i,)));S=tuple(sorted(T+(j,)));expected_terminal=(-1)**(j-i+1) if i<j else (-1)**(i-j);expected=expected_terminal*(-1)**(sum(x>i for x in T)+sum(x>j for x in T));terms=source_terms(R,S);cases+=1
   for name,key in schemes.items():
    groups={}
    for K,z in terms:groups[key(K,T,i,j)]=groups.get(key(K,T,i,j),0)+z
    for q,z in groups.items():
     d=stats[name];d["group_count"]+=1
     if z==0:d["zero_group_count"]+=1
     elif z*expected<0:
      d["bad_group_count"]+=1
      if d["first_bad"] is None:d["first_bad"]={"base":T,"i":i,"j":j,"group":q,"oriented_group_sum":str(z*expected)}
success=[name for name,d in stats.items() if d["bad_group_count"]==0]
checks={"all_3584_terminal_cases_grouped":cases==3584,"all_eight_grouping_rules_classified":len(stats)==8,"successful_sign_coherent_grouping_found":bool(success)}
result={"schema":"marici.strominger.rh_quarter_hurwitz_source_sum_cancellation_groupings.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Natural index-statistic groupings were tested as exact cancellation certificates. A successful rule makes every grouped source sum have the terminal orientation; otherwise the first negative oriented group is a concrete obstruction and cancellation requires a structure beyond these one-statistic partitions.","terminal_case_count":cases,"successful_groupings":success,"grouping_statistics":stats,"checks":checks}
(base/"results"/"rh_quarter_hurwitz_source_sum_cancellation_groupings.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
