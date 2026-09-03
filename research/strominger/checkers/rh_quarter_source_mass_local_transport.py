import itertools,json,runpy
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name("rh_quarter_hurwitz_terminal_minor_source_formula.py")))
source_terms,k=g["source_terms"],g["k"]
def feasible(neg,pos,edge):
 # exact augmenting transport; positive nodes carry capacities
 caps=[z for _,z in pos];remaining=F(0)
 for K,demand in neg:
  remaining+=demand
  for b,(L,_) in enumerate(pos):
   if edge(K,L) and demand and caps[b]:
    z=min(demand,caps[b]);demand-=z;caps[b]-=z;remaining-=z
  if demand:return False
 return remaining==0
def exchange(K,L):return len(set(K)^set(L))==2
def adjacent(K,L):
 d=list(set(K)^set(L));return len(d)==2 and abs(d[0]-d[1])==1
def comparable(K,L):return all(a<=b for a,b in zip(K,L)) or all(b<=a for a,b in zip(K,L))
def interlace(K,L):
 if len(K)<=1:return True
 return (all(K[x]<=L[x]<=K[x+1] for x in range(len(K)-1)) or all(L[x]<=K[x]<=L[x+1] for x in range(len(K)-1)))
schemes={"adjacent_exchange":adjacent,"single_exchange":exchange,"componentwise_comparable":comparable,"interlacing":interlace}
stats={n:{"passed":0,"failed":0,"first_failure":None} for n in schemes};cases=0
for r in range(k-1):
 for S in itertools.combinations(range(k),r):
  rem=[x for x in range(k) if x not in S]
  for i,j in itertools.combinations(rem,2):
   if any(i<q<j for q in S):continue
   R=tuple(sorted(S+(i,)));Q=tuple(sorted(S+(j,)));expected=(-1)**(j-i+1+sum(x>i for x in S)+sum(x>j for x in S));vals=[(K,expected*z) for K,z in source_terms(R,Q)];neg=[(K,-z) for K,z in vals if z<0];pos=[(K,z) for K,z in vals if z>0];cases+=1
   for name,edge in schemes.items():
    ok=feasible(neg,pos,edge);stats[name]["passed" if ok else "failed"]+=1
    if not ok and stats[name]["first_failure"] is None:stats[name]["first_failure"]={"base":S,"i":i,"j":j,"negative_term_count":len(neg),"positive_term_count":len(pos)}
success=[n for n,d in stats.items() if d["failed"]==0]
checks={"all_769_cases_checked":cases==769,"all_four_local_transport_graphs_classified":len(stats)==4,"successful_local_transport_found":bool(success)}
result={"schema":"marici.strominger.rh_quarter_source_mass_local_transport.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Four local index relations were tested as capacity-respecting transports from negative to positive source terms. Failure means some negative mass cannot be assigned greedily to related positive capacity; success would supply a bounded weighted-injection candidate. The test is order-dependent and therefore only a falsifier for this specified greedy construction, not for all flows on the relation.","case_count":cases,"successful_relations":success,"relation_statistics":stats,"checks":checks}
(base/"results"/"rh_quarter_source_mass_local_transport.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
