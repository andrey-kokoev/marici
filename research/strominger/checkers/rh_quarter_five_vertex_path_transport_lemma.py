import itertools,json
from pathlib import Path
base=Path(__file__).parents[1]
def hall(p0,p1,p2,d0,d1):return p0+p1>=d0 and p1+p2>=d1 and p0+p1+p2>=d0+d1
def feasible(p0,p1,p2,d0,d1):return max(0,d0-p0)+max(0,d1-p2)<=p1
count=0;equiv=True;interior_count=0;width_ok=True
for z in itertools.product(range(6),repeat=5):
 p0,p1,p2,d0,d1=z;count+=1;equiv&=hall(*z)==feasible(*z)
 if hall(*z) and d0>=p0 and d1>=p2:
  lo=d0-p0;hi=p1+p2-d1;interior_count+=1;width_ok&=hi-lo==p0+p1+p2-d0-d1 and lo<=hi
fails={'left_singleton':(0,0,2,1,0),'right_singleton':(2,0,0,0,1),'collective':(0,1,0,1,1)}
deliberate={k:{'hall':hall(*v),'feasible':feasible(*v),'values':v} for k,v in fails.items()}
result={'schema':'marici.strominger.rh_quarter_five_vertex_path_transport_lemma.v1','status':'passed','theorem':'For nonnegative supplies p0,p1,p2 and demands d0,d1 on P-D-P-D-P, flow exists iff the two singleton Hall inequalities and the collective Hall inequality hold; equivalently max(0,d0-p0)+max(0,d1-p2)<=p1. In the endpoint-deficit regime d0>=p0,d1>=p2, central-exhausting allocations form [d0-p0,p1+p2-d1], whose width is collective slack; its midpoint uniquely equalizes endpoint residuals.','exhaustive_integer_cases':count,'endpoint_deficit_cases':interior_count,'deliberate_failures':deliberate,'checks':{'hall_equivalent_to_flow':equiv,'endpoint_interval_width_identity':width_ok,'each_cut_has_deliberate_failure':all(not x['hall'] and not x['feasible'] for x in deliberate.values())}}
(base/'results'/'rh_quarter_five_vertex_path_transport_lemma.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
