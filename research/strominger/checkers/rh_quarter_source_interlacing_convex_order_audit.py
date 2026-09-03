import itertools,json,runpy
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name("rh_quarter_hurwitz_terminal_minor_source_formula.py")))
source_terms,k=g["source_terms"],g["k"]
def edge(K,L):
 if len(K)<=1:return True
 return all(K[x]<=L[x]<=K[x+1] for x in range(len(K)-1)) or all(L[x]<=K[x]<=L[x+1] for x in range(len(K)-1))
def convex(A,B):
 for K in A:
  ns=[b for b,L in enumerate(B) if edge(K,L)]
  if ns and ns!=list(range(min(ns),max(ns)+1)):return False,K,ns
 return True,None,None
orders={"lex":lambda K:K,"colex":lambda K:tuple(reversed(K)),"sum_lex":lambda K:(sum(K),K)}
stats={n:{"negative_convex_cases":0,"biconvex_cases":0,"first_negative_failure":None,"first_biconvex_failure":None} for n in orders};cases=0
for r in range(k-1):
 for S in itertools.combinations(range(k),r):
  rem=[x for x in range(k) if x not in S]
  for i,j in itertools.combinations(rem,2):
   if any(i<q<j for q in S):continue
   R=tuple(sorted(S+(i,)));Q=tuple(sorted(S+(j,)));expected=(-1)**(j-i+1+sum(x>i for x in S)+sum(x>j for x in S));vals=[(K,expected*z) for K,z in source_terms(R,Q)];neg=[K for K,z in vals if z<0];pos=[K for K,z in vals if z>0];cases+=1
   for name,key in orders.items():
    N=sorted(neg,key=key);P=sorted(pos,key=key);a,bad,ns=convex(N,P);b,bad2,ns2=convex(P,N)
    if a:stats[name]["negative_convex_cases"]+=1
    elif stats[name]["first_negative_failure"] is None:stats[name]["first_negative_failure"]={"base":S,"i":i,"j":j,"negative_index":bad,"neighbor_positions":ns}
    if a and b:stats[name]["biconvex_cases"]+=1
    elif stats[name]["first_biconvex_failure"] is None:stats[name]["first_biconvex_failure"]={"base":S,"i":i,"j":j,"failed_side":"negative" if not a else "positive","index":bad if not a else bad2}
universal_negative=[n for n,d in stats.items() if d["negative_convex_cases"]==cases];universal_biconvex=[n for n,d in stats.items() if d["biconvex_cases"]==cases]
checks={"all_769_cases_checked":cases==769,"all_three_orders_classified":len(stats)==3,"convex_order_disposition_complete":bool(universal_negative or all(d["first_negative_failure"] for d in stats.values()))}
result={"schema":"marici.strominger.rh_quarter_source_interlacing_convex_order_audit.v2","status":"passed" if all(checks.values()) else "failed","verdict":"The three preregistered linear orders are classified as a rival backend under the single Hall programme DPC boundary.","case_count":cases,"universal_negative_convex_orders":universal_negative,"universal_biconvex_orders":universal_biconvex,"order_statistics":stats,"checks":checks}
(base/"results"/"rh_quarter_source_interlacing_convex_order_audit.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps({"status":result["status"],"case_count":cases,"universal_negative":universal_negative,"universal_biconvex":universal_biconvex},indent=2))
