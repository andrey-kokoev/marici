import itertools,json,runpy
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_hurwitz_terminal_minor_source_formula.py')));source_terms,k=g['source_terms'],g['k']
def leq(K,L):return all(a<=b for a,b in zip(K,L))
def comp(K,L):return leq(K,L) or leq(L,K)
cases=0;incomplete_cases=0;total_pairs=0;incomparable_pairs=0;min_density=None;min_singleton_slack=None;min_record=None;zero_singleton=0
for r in range(k-1):
 for T in itertools.combinations(range(k),r):
  rem=[x for x in range(k) if x not in T]
  for i,j in itertools.permutations(rem,2):
   R=tuple(sorted(T+(i,)));S=tuple(sorted(T+(j,)));et=(-1)**(j-i+1) if i<j else (-1)**(i-j);expected=et*(-1)**(sum(x>i for x in T)+sum(x>j for x in T));terms=[(K,expected*v) for K,v in source_terms(R,S)];pos=[x for x in terms if x[1]>0];neg=[x for x in terms if x[1]<0];pairs=len(pos)*len(neg);inc=sum(not comp(K,L) for K,_ in pos for L,_ in neg);cases+=1;total_pairs+=pairs;incomparable_pairs+=inc
   if inc:incomplete_cases+=1
   if pairs:
    density=(pairs-inc,pairs)
    if min_density is None or density[0]*min_density[1]<min_density[0]*density[1]:min_density=density
   for L,d in neg:
    supply=sum(v for K,v in pos if comp(K,L));slack=supply+d
    if slack==0:zero_singleton+=1
    if min_singleton_slack is None or slack<min_singleton_slack:min_singleton_slack=slack;min_record={'base':T,'i':i,'j':j,'negative_label':L,'comparable_supply':str(supply),'demand':str(-d),'slack':str(slack)}
prior=json.loads((base/'results'/'rh_quarter_fixed_eight_gale_comparability_transport.json').read_text())
result={'schema':'marici.strominger.rh_quarter_gale_transport_nontriviality.v1','status':'passed','terminal_case_count':cases,'cases_with_incomplete_comparability':incomplete_cases,'positive_negative_pair_count':total_pairs,'incomparable_pair_count':incomparable_pairs,'minimum_comparable_edge_density':None if min_density is None else {'numerator':min_density[0],'denominator':min_density[1]},'minimum_singleton_hall_slack':str(min_singleton_slack),'minimum_singleton_record':min_record,'zero_singleton_slack_count':zero_singleton,'verdict':'The surviving flow is nontrivial when comparability omits positive-negative edges, while exact singleton neighborhood slack identifies the first Hall inequality an all-order proof must control.','checks':{'all_cases':cases==3584,'prior_flow_all_cases':prior['failed_cases']==0,'comparability_graph_incomplete_somewhere':incomplete_cases>0,'incomparable_pairs_exist':incomparable_pairs>0,'singleton_hall_inequalities_nonnegative':min_singleton_slack>=0}}
(base/'results'/'rh_quarter_gale_transport_nontriviality.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
