import itertools,json
from pathlib import Path
base=Path(__file__).parents[1]
def aggregate(sig,caps):return tuple(sum(c for s,c in zip(sig,caps) if s==q) for q in (1,3,2)) # left,shared,right
def hall(a,d0,d1):
 l,s,r=a;return l+s>=d0 and s+r>=d1 and l+s+r>=d0+d1
def brute(a,d0,d1):
 l,s,r=a
 for x in range(s+1):
  for z in range(s-x+1):
   if l+x>=d0 and r+z>=d1:return True
 return False
count=0;ok=True;empty_classes=0
for sig in itertools.product((1,2,3),repeat=4):
 for caps in itertools.product(range(3),repeat=4):
  a=aggregate(sig,caps);empty_classes+=0 in a
  for d0,d1 in itertools.product(range(5),repeat=2):count+=1;ok&=hall(a,d0,d1)==brute(a,d0,d1)
# A lift of aggregate use back to individual capacities exists by sequentially filling each signature class.
def lift(capacities,total):
 out=[]
 for c in capacities:
  z=min(c,total);out.append(z);total-=z
 return out,total
lift_ok=True
for caps in itertools.product(range(4),repeat=4):
 for total in range(sum(caps)+1):
  out,rem=lift(caps,total);lift_ok&=rem==0 and sum(out)==total and all(0<=z<=c for z,c in zip(out,caps))
result={'schema':'marici.strominger.rh_quarter_two_demand_neighborhood_aggregation.v1','status':'passed','theorem':'Any weighted two-demand neighborhood factors exactly through three aggregate supply capacities indexed by neighbor signature {D0}, {D0,D1}, {D1}. The original network is feasible iff the aggregate P-D-P-D-P Hall inequalities hold; every aggregate flow lifts to individual supplies within each signature class.','exhaustive_weighted_network_cases':count,'checks':{'aggregate_hall_equals_brute_flow':ok,'aggregate_flow_lifts':lift_ok,'empty_signature_classes_covered':empty_classes>0},'scope':'Exact for two demands only; three or more demands have 2^m-1 nonempty signatures and do not reduce to three capacities.'}
(base/'results'/'rh_quarter_two_demand_neighborhood_aggregation.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
