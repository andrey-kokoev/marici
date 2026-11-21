"""Separate regularity from minimum degree; test the unique safe edge addition to the repair counterexample and locate the resulting forbidden triangle."""
from pathlib import Path
from itertools import combinations
from collections import Counter,defaultdict
import json
from ramsey_hall_center_conjecture import decode,independent
from ramsey_mutual_repair_conjecture import apply
from ramsey_regular_two_switch import relation,iso
D=Path(__file__).parent;graphs=[decode(line) for line in (D/'pauli-realization-catalogues'/'r37_22.g6').read_bytes().splitlines()];minimum=[min(n.bit_count() for n in A) for A in graphs];summary={}
for k in (2,3):
 grouped=defaultdict(Counter)
 for r in json.loads((D/f'ramsey_closed_repair_all_extremal_size{k}.json').read_text()):grouped[minimum[r['source']-1]].update(r['stats'])
 summary[k]={d:dict(c) for d,c in grouped.items()}
A=graphs[148];safe=[(i,j) for i,j in combinations(range(22),2) if not(A[i]>>j&1) and not A[i]&A[j]];assert safe==[(0,2)];B=A[:];B[0]|=1<<2;B[2]|=1;assert min(n.bit_count() for n in B)==5 and not independent(B,(1<<22)-1,7);rb=relation(B);hits=[]
for i,C in enumerate(graphs,1):
 mapping=iso(B,C,rb,relation(C))
 if mapping is not None:hits.append(i)
assert len(hits)==1;moves=json.loads((D/'ramsey_nonregular_closed_repair_counterexample.json').read_text())['switches'];triangles={}
for mask in range(4):
 C=B[:]
 for k,s in enumerate(moves):
  if mask>>k&1:C=apply(C,s['removed'],s['added'])
 triangles[mask]=[I for I in combinations(range(22),3) if all(C[i]>>j&1 for i,j in combinations(I,2))]
result={'records_by_minimum_degree':dict(Counter(minimum)),'degree4_records':[i+1 for i,d in enumerate(minimum) if d==4],'repair_counts_by_minimum_degree':summary,'counterexample_safe_additions':safe,'augmented_graph_record':hits[0],'augmented_degree_histogram':dict(Counter(n.bit_count() for n in B)),'augmented_partial_triangles':triangles};(D/'ramsey_repair_minimum_degree_audit.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
