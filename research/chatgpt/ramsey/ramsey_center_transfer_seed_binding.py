"""Transport the five-switch center transfer to the actual affine BRNN output; compare marked centers and edge changes with the literal row permutation."""
from pathlib import Path
from itertools import combinations
import json
from ramsey_seed_affine_witness import m,mate,P,T,hub,r6
from ramsey_hall_center_conjecture import decode,root_profile
from ramsey_regular_two_switch import relation,iso
D=Path(__file__).parent

def graph(M):
 removed={tuple(sorted(P.index(d) for d in T[j-15] if d!=P[i])) for i,j in M};E={(0,1+i) for i in range(6)}|{(1+i,7+j) for j,d in enumerate(P) for i in d}|{(7+i,7+j) for i,j in combinations(range(15),2) if not set(P[i])&set(P[j]) and (i,j) not in removed};A=[0]*22
 for i,j in E:A[i]|=1<<j;A[j]|=1<<i
 return A

def edges(A):return {e for e in combinations(range(22),2) if A[e[0]]>>e[1]&1}
def centers(A):return [v for v in range(22) if A[v].bit_count()==6 and root_profile(A,v)['hall_center']]
A=graph(m);row=graph(mate);catalogue=json.loads((D/'ramsey_hall_center_conjecture.json').read_text());C=decode(next(r for r in catalogue['regular'] if r['record']==191)['graph6'].encode());f=iso(A,C,relation(A),relation(C));assert f is not None and f[0]==0 and f[1+hub]==1;back={v:k for k,v in f.items()};example=json.loads((D/'ramsey_closed_repair_size5.json').read_text())[1]['first_valid_example'];switched=A[:];transported=[]
for s in example['switches']:
 rem=[tuple(sorted((back[i],back[j]))) for i,j in s['removed']];add=[tuple(sorted((back[i],back[j]))) for i,j in s['added']]
 for i,j in rem+add:switched[i]^=1<<j;switched[j]^=1<<i
 transported.append({'removed':rem,'added':add})
R=[0]+[1+r6[i] for i in range(6)]+[7+P.index(tuple(sorted(r6[x] for x in d))) for d in P];assert {tuple(sorted((R[i],R[j]))) for i,j in edges(A)}==edges(row)
assert centers(A)==centers(row)==[0] and centers(switched)==[1+hub]
# Transport the original incidence flags as marked triples of output duad vertices.
marks=[]
for i,j in [(0,16),(7,29)]:
 duads=[7+P.index(d) for d in T[j-15]];marks.append({'selected_duad_vertex':7+i,'partition_duad_vertices':duads,'after_switch_still_all_outside_new_center':all(not(switched[1+hub]>>v&1) and v!=1+hub for v in duads)})
result={'affine_to_catalogue':f,'original_center':centers(A),'row_center':centers(row),'transfer_center':centers(switched),'hub_ground_label':'14','hub_output_vertex':1+hub,'row_removed_edges':len(edges(A)-edges(row)),'transfer_removed_edges':len(edges(A)-edges(switched)),'transported_switches':transported,'boundary_marks':marks};(D/'ramsey_center_transfer_seed_binding.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
