"""Distinguish degree-floor protection from extremal-order protection. Delete one vertex of a regular22 witness: all21 degrees remain5 or6. Search mutually repaired disjoint switch pairs with joint-only independent sevens."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
from ramsey_hall_center_conjecture import decode
from ramsey_mutual_repair_conjecture import switches,sevens,apply,repairs
D=Path(__file__).parent;data=json.loads((D/'ramsey_hall_center_conjecture.json').read_text());stats=Counter();found=None
for record in data['regular']:
 original=decode(record['graph6'].encode())
 for deleted in range(22):
  labels=[v for v in range(22) if v!=deleted];A=[sum(1<<j for j,w in enumerate(labels) if original[v]>>w&1) for v in labels];assert min(n.bit_count() for n in A)==5 and not list(sevens(A));stats['deletions_tested']+=1;moves=list(switches(A))
  for s,t in combinations(moves,2):
   if s['support']&t['support']:continue
   stats['disjoint_pairs_tested']+=1
   if not(repairs(s,t) and repairs(t,s)):continue
   stats['mutual_pairs']+=1;B=apply(apply(A,s['removed'],s['added']),t['removed'],t['added']);bad=list(sevens(B))
   if not bad:continue
   # Independently enumerate all seven-subsets in all four states.
   states=[]
   for state in range(4):
    C=A[:]
    for k,m in enumerate((s,t)):
     if state>>k&1:C=apply(C,m['removed'],m['added'])
    assert all(not(C[i]&C[j]) for i,j in combinations(range(21),2) if C[i]>>j&1)
    exact=[I for I in combinations(range(21),7) if all(not(C[i]>>j&1) for i,j in combinations(I,2))];states.append({'mask':state,'independent_sevens':exact})
   assert [len(x['independent_sevens']) for x in states]==[0,len(s['bad']),len(t['bad']),len(bad)]
   found={'parent_record':record['record'],'deleted_vertex':deleted,'vertex_labels_in_parent':labels,'starting_adjacency':A,'degree_histogram':dict(Counter(n.bit_count() for n in A)),'switches':[s,t],'states':states};break
  if found:break
 if found:break
if found:
 parent=decode(next(r for r in data['regular'] if r['record']==found['parent_record'])['graph6'].encode());labels=found['vertex_labels_in_parent'];parent_moves=[{key:[(labels[i],labels[j]) for i,j in s[key]] for key in ('removed','added')} for s in found['switches']];restored=[]
 for state in range(4):
  B=parent[:]
  for k,s in enumerate(parent_moves):
   if state>>k&1:B=apply(B,s['removed'],s['added'])
  restored.append({'state':state,'triangles':[I for I in combinations(range(22),3) if all(B[i]>>j&1 for i,j in combinations(I,2))],'independent_sevens':len(list(sevens(B)))})
 found['switches_in_parent_labels']=parent_moves;found['restored_vertex_states']=restored
result={'stats':dict(stats),'first_counterexample':found};(D/'ramsey_degree5_vertex_deletion_probe.json').write_text(json.dumps(result,indent=2)+'\n');print('stats',dict(stats),'counterexample',None if found is None else (found['parent_record'],found['deleted_vertex'],[len(s['independent_sevens']) for s in found['states']]));print('degrees',None if found is None else found['degree_histogram'])
