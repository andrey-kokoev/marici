"""Noncircular strengthening of triangle protection: must some edge that repairs a visible blue defect itself create a red triangle? Allow all degree-preserving switches, not only triangle-free ones."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json,argparse
from ramsey_hall_center_conjecture import decode
from ramsey_mutual_repair_conjecture import apply,sevens
D=Path(__file__).parent;parser=argparse.ArgumentParser();parser.add_argument('--max-graphs',type=int,default=10);args=parser.parse_args();lines=(D/'pauli-realization-catalogues'/'r37_22.g6').read_bytes().splitlines();ordered=sorted(enumerate(lines,1),key=lambda row:-min(n.bit_count() for n in decode(row[1])));stats=Counter();found=None
for record,line in ordered:
 A=decode(line)
 if min(n.bit_count() for n in A)<5 or stats['graphs_tested']>=args.max_graphs:break
 stats['graphs_tested']+=1;E=[e for e in combinations(range(22),2) if A[e[0]]>>e[1]&1];moves=[]
 for removed in combinations(E,2):
  (a,b),(c,d)=removed
  if len({a,b,c,d})!=4:continue
  for added0 in [((a,c),(b,d)),((a,d),(b,c))]:
   added=tuple(tuple(sorted(e)) for e in added0)
   if any(A[i]>>j&1 for i,j in added):continue
   B=apply(A,removed,added);bad=list(sevens(B))
   if not bad:continue
   cover={}
   for k,I in enumerate(bad):
    vertices=[v for v in range(22) if I>>v&1]
    for e in combinations(vertices,2):cover[e]=cover.get(e,0)|(1<<k)
   moves.append({'removed':removed,'added':added,'bad':bad,'support':sum(1<<v for v in (a,b,c,d)),'cover':cover,'full':(1<<len(bad))-1,'guarded_edges':[e for e in added if B[e[0]]&B[e[1]]]})
 for s,t in combinations(moves,2):
  if s['support']&t['support']:continue
  stats['disjoint_pairs']+=1
  if (s['cover'].get(t['added'][0],0)|s['cover'].get(t['added'][1],0))!=s['full']:continue
  if (t['cover'].get(s['added'][0],0)|t['cover'].get(s['added'][1],0))!=t['full']:continue
  stats['blue_mutual_pairs']+=1
  if any(t['cover'].get(e,0) for e in s['guarded_edges']) or any(s['cover'].get(e,0) for e in t['guarded_edges']):continue
  stats['mutual_pairs_without_guarded_repair_edge']+=1;B=apply(apply(A,s['removed'],s['added']),t['removed'],t['added']);bad=list(sevens(B))
  if not bad:continue
  found={'source':record,'degree_histogram':dict(Counter(n.bit_count() for n in A)),'switches':[{k:v for k,v in m.items() if k not in ('cover','full')} for m in (s,t)],'combined_independent_sevens':[[v for v in range(22) if I>>v&1] for I in bad],'combined_triangles':[I for I in combinations(range(22),3) if all(B[i]>>j&1 for i,j in combinations(I,2))]};break
 print('record',record,'stats',dict(stats),flush=True)
 if found:break
if found:
 states=[]
 for mask in range(4):
  B=A[:]
  for k,s in enumerate(found['switches']):
   if mask>>k&1:B=apply(B,s['removed'],s['added'])
  bad=[I for I in combinations(range(22),7) if all(not(B[i]>>j&1) for i,j in combinations(I,2))];tri=[I for I in combinations(range(22),3) if all(B[i]>>j&1 for i,j in combinations(I,2))];states.append({'mask':mask,'independent_sevens':bad,'triangles':tri})
 found['independent_verification']=states
 repairs=[]
 for k in range(2):
  for I in states[1<<k]['independent_sevens']:
   hits=[e for e in found['switches'][1-k]['added'] if set(e)<=set(I)];assert hits;repairs.append({'created_by':k,'seven':I,'hit_by':hits})
 found['blue_repair_certificates']=repairs
result={'stats':dict(stats),'first_counterexample':found};(D/'ramsey_repair_edge_guard_probe.json').write_text(json.dumps(result,indent=2)+'\n');print('counterexample',found)
