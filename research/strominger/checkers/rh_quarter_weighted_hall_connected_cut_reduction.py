import itertools,json
from fractions import Fraction as F
from pathlib import Path
# Positive supplies p0,p1,p2; negative demands n0..n3.
supply=(F(5),F(4),F(3));demand=(F(3),F(4),F(2),F(2));nbr=({0},{0,1},{1,2},{2})
def slack(S):return sum(supply[p] for p in set().union(*(nbr[i] for i in S)))-sum(demand[i] for i in S)
def connected(S):
 S=set(S);seen={next(iter(S))}
 while True:
  more={j for i in seen for j in S-seen if nbr[i]&nbr[j]}
  if not more:return seen==S
  seen|=more
subs=[tuple(i for i in range(4) if mask>>i&1) for mask in range(1,16)]
connected_subs=[S for S in subs if connected(S)]
all_min=min((slack(S),S) for S in subs);conn_min=min((slack(S),S) for S in connected_subs)
# Deliberate failure: raise n1 demand so connected singleton {1} has negative slack.
bad_demand=(F(3),F(10),F(2),F(2));bad_slack=supply[0]+supply[1]-bad_demand[1]
checks={'all_subset_minimum_equals_connected_minimum':all_min[0]==conn_min[0],'disconnected_slack_adds_over_overlap_components':slack((0,3))==slack((0,))+slack((3,)),'connected_family_smaller':len(connected_subs)<len(subs),'deliberate_connected_deficit_nonzero':bad_slack<0,'exact_nonnegative_witness':all_min[0]>=0}
result={'schema':'marici.strominger.rh_quarter_weighted_hall_connected_cut_reduction.v1','status':'passed' if all(checks.values()) else 'failed','theorem':'For weighted Hall transport, form the overlap graph on negative labels by joining demands that share a positive neighbor. Hall slack is additive across connected components, so it suffices to test connected negative subsets.','proof_core':'Distinct overlap components have disjoint positive neighborhoods; both neighborhood supply and demand are additive. Any deficient subset therefore has a deficient connected component.','finite_witness':{'all_subset_count':len(subs),'connected_subset_count':len(connected_subs),'minimum_slack':str(all_min[0]),'minimizer':all_min[1],'deliberate_deficit':str(bad_slack)},'consequence':'The all-order Gale request can be sharpened from every subset to every connected subset in the negative-label overlap graph.','checks':checks}
p=Path(__file__).parents[1]/'results'/'rh_quarter_weighted_hall_connected_cut_reduction.json';p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
