"""Probe stronger guard explanation: allow triangle-producing switches, demand blue mutual repair plus joint blue failure, and ask whether a guard must lie OUTSIDE BOTH supports. Search stops at first counterexample."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json,argparse
from ramsey_hall_center_conjecture import decode
from ramsey_mutual_repair_conjecture import sevens,apply,repairs
D=Path(__file__).parent;lines=(D/'pauli-realization-catalogues'/'r37_22.g6').read_bytes().splitlines();stats=Counter();found=None;first_guarded=None
parser=argparse.ArgumentParser();parser.add_argument('--max-graphs',type=int,default=10);args=parser.parse_args();ordered=sorted(enumerate(lines,1),key=lambda row:-min(n.bit_count() for n in decode(row[1])))
for record,line in ordered:
 A=decode(line)
 if min(n.bit_count() for n in A)<5:continue
 if stats['graphs_tested']>=args.max_graphs:break
 stats['graphs_tested']+=1;E=[e for e in combinations(range(22),2) if A[e[0]]>>e[1]&1];moves=[]
 for removed in combinations(E,2):
  (a,b),(c,d)=removed
  if len({a,b,c,d})!=4:continue
  for added in [((a,c),(b,d)),((a,d),(b,c))]:
   if any(A[i]>>j&1 for i,j in added):continue
   B=apply(A,removed,added);bad=list(sevens(B))
   if not bad:continue
   support=sum(1<<v for v in (a,b,c,d));guard=0
   for i,j in added:guard|=B[i]&B[j]
   assert not guard&support
   moves.append({'removed':removed,'added':added,'bad':bad,'support':support,'guard_mask':guard})
 stats['blue_invalid_switches']+=len(moves)
 for s,t in combinations(moves,2):
  if s['support']&t['support']:continue
  stats['disjoint_pairs']+=1
  if (s['guard_mask']|t['guard_mask'])&~(s['support']|t['support']):continue
  stats['pairs_without_outside_guard']+=1
  if not(repairs(s,t) and repairs(t,s)):continue
  stats['blue_mutual_pairs']+=1;B=apply(apply(A,s['removed'],s['added']),t['removed'],t['added']);bad=list(sevens(B))
  if not bad:continue
  stats['closed_but_blue_invalid']+=1;outside=(s['guard_mask']|t['guard_mask'])&~(s['support']|t['support']);example={'record':record,'degree_histogram':dict(Counter(n.bit_count() for n in A)),'switches':[s,t],'outside_guards':[v for v in range(22) if outside>>v&1],'new_sevens':[[v for v in range(22) if I>>v&1] for I in bad],'triangles':[I for I in combinations(range(22),3) if all(B[i]>>j&1 for i,j in combinations(I,2))]}
  if first_guarded is None:first_guarded=example
  if not outside:found=example;break
 print('record',record,'stats',dict(stats),flush=True)
 (D/'ramsey_external_triangle_guard_progress.json').write_text(json.dumps({'stats':dict(stats),'last_record':record,'counterexample':found},indent=2)+'\n')
 if found:break
result={'stats':dict(stats),'first_outside_guard_counterexample':found,'first_blue_failure':first_guarded};(D/'ramsey_external_triangle_guard.json').write_text(json.dumps(result,indent=2)+'\n');print('stats',dict(stats));print('counterexample',found)
