"""Test one-vertex local inheritance of every emergent independent seven. Also record nearest surviving individual obstruction, with and without support restriction."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
from ramsey_hall_center_conjecture import decode
from ramsey_mutual_repair_conjecture import switches,sevens,apply
vertices=lambda mask:[v for v in range(22) if mask>>v&1]
if __name__=='__main__':
 data=json.loads(Path(__file__).with_name('ramsey_hall_center_conjecture.json').read_text());report=[]
 for record in data['regular']:
  if record['record'] not in (190,191):continue
  A=decode(record['graph6'].encode());moves=list(switches(A));hist=Counter();unrestricted=Counter();counterexample=None;total=0;worst=None;worst_distance=-1
  for s,t in combinations(moves,2):
   if s['support']&t['support']:continue
   joint=set(sevens(apply(apply(A,s['removed'],s['added']),t['removed'],t['added'])));individual=set(s['bad'])|set(t['bad']);survivors=joint&individual;support=s['support']|t['support']
   for I in joint-individual:
    total+=1;local=[J for J in survivors if not (J&~I&~support)];distance=min(((J&~I).bit_count() for J in local),default=None);hist[str(distance)]+=1;global_distance=min(((J&~I).bit_count() for J in survivors),default=None);unrestricted[str(global_distance)]+=1
    if global_distance is not None and global_distance>worst_distance:
     worst_distance=global_distance;worst={'A':s,'B':t,'emergent':vertices(I),'surviving_individual_obstructions':[vertices(J) for J in sorted(survivors)],'minimum_replacements':global_distance}
    if distance!=1 and counterexample is None:
     counterexample={'A':s,'B':t,'emergent':vertices(I),'support':vertices(support),'surviving_individual_obstructions':[vertices(J) for J in sorted(survivors)],'local_minimum_replacements':distance}
  result={'source':record['record'],'emergent_obstruction_occurrences':total,'local_distance_histogram':dict(hist),'unrestricted_distance_histogram':dict(unrestricted),'first_counterexample':counterexample,'most_distant_example':worst};report.append(result);print(result)
 Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n')
