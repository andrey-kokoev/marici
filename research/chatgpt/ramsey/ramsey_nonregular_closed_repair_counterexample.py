"""Independent seven-subset verification of the unique pair-closure counterexample in the full22-vertex catalogue. Does not use recursive independent-set enumeration."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
from ramsey_hall_center_conjecture import decode
from ramsey_mutual_repair_conjecture import apply
D=Path(__file__).parent;records=json.loads((D/'ramsey_closed_repair_all_extremal_size2.json').read_text());record=next(r for r in records if r['first_counterexample']);assert record['source']==149;example=record['first_counterexample'];A=decode((D/'pauli-realization-catalogues'/'r37_22.g6').read_bytes().splitlines()[148]);moves=example['switches'];results=[];bad_by_state={}
for state in range(4):
 B=A[:]
 for k,s in enumerate(moves):
  if state>>k&1:B=apply(B,s['removed'],s['added'])
 assert [n.bit_count() for n in B]==[n.bit_count() for n in A]
 triangles=[I for I in combinations(range(22),3) if all(B[i]>>j&1 for i,j in combinations(I,2))];bad=[I for I in combinations(range(22),7) if all(not(B[i]>>j&1) for i,j in combinations(I,2))];assert not triangles;bad_by_state[state]=bad;results.append({'state':state,'triangles':len(triangles),'independent_sevens':bad})
assert not bad_by_state[0] and len(bad_by_state[1])==5 and len(bad_by_state[2])==3 and len(bad_by_state[3])==2
repairs=[]
for k in range(2):
 for I in bad_by_state[1<<k]:
  hits=[e for e in moves[1-k]['added'] if set(e)<=set(I)];assert hits;repairs.append({'created_by':k,'seven':I,'repair_edges':hits})
assert not (set(bad_by_state[3])&(set(bad_by_state[1])|set(bad_by_state[2])))
result={'source':149,'degree_histogram':dict(Counter(n.bit_count() for n in A)),'degrees':[n.bit_count() for n in A],'switches':moves,'states':results,'repair_certificates':repairs,'new_seven_original_edges':[{'seven':I,'original_red_edges':[e for e in combinations(I,2) if A[e[0]]>>e[1]&1]} for I in bad_by_state[3]]};(D/'ramsey_nonregular_closed_repair_counterexample.json').write_text(json.dumps(result,indent=2)+'\n');print('degree histogram',result['degree_histogram'],'seven counts',[len(r['independent_sevens']) for r in results]);print('new obstructions',result['new_seven_original_edges'])
