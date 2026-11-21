"""Ask whether singleton/pair rules imply every triple-born repair obligation by unit propagation, not merely by exhaustive final-state checking."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
from ramsey_hall_center_conjecture import decode
from ramsey_mutual_repair_conjecture import apply,sevens
from ramsey_closed_repair_conjecture import disjoint_collections
D=Path(__file__).parent;data=json.loads((D/'ramsey_block_selection_repair_rules.json').read_text());lines=(D/'pauli-realization-catalogues'/'r37_22.g6').read_bytes().splitlines();report=[]
for record in data:
 A=decode(lines[record['source']-1]);moves=record['switches'];n=len(moves);conflicts=[sum(1<<j for j,t in enumerate(moves) if i!=j and s['support']&t['support']) for i,s in enumerate(moves)];clauses=[(head,sum(1<<i for i in row['birth'])) for row in record['rules'] for head in row['repairer_masks']]
 def propagate(T,F):
  while True:
   old=(T,F);mask=T
   while mask:
    bit=mask&-mask;mask^=bit;F|=conflicts[bit.bit_length()-1]
   if T&F:return None
   for positive,negative in clauses:
    if positive&T or negative&F:continue
    remaining=(positive|negative)&~(T|F)
    if not remaining:return None
    if not remaining&(remaining-1):
     if positive&remaining:T|=remaining
     else:F|=remaining
   if old==(T,F):return T,F
 base=propagate(0,0);assert base is not None;stats=Counter();stats['initially_excluded_switches']=base[1].bit_count();pair_cache={};first_unproved=None;first_certificate=None;surviving_births=[];repair_edges={}
 for i,s in enumerate(moves):
  for e in s['added']:
   e=tuple(sorted(e));repair_edges[e]=repair_edges.get(e,0)|(1<<i)
 def bad(ids):
  B=A[:]
  for i in ids:B=apply(B,moves[i]['removed'],moves[i]['added'])
  return set(sevens(B))
 for ids in disjoint_collections(moves,3):
  stats['triples']+=1;selected=sum(1<<i for i in ids);closure=propagate(selected,base[1])
  if closure is None:stats['birth_impossible_by_propagation']+=1;continue
  stats['birth_not_excluded']+=1;lower=set()
  for pair in combinations(ids,2):
   if pair not in pair_cache:pair_cache[pair]=bad(pair)
   lower|=pair_cache[pair]
  for i in ids:lower|=set(moves[i]['bad'])
  triple_defects=bad(ids);new_defects=triple_defects-lower;surviving_births.append({'birth':ids,'total_sevens':len(triple_defects),'genuinely_triple_born':len(new_defects)})
  for I in new_defects:
   stats['triple_born_defects']+=1;repairers=0
   for edge in combinations([v for v in range(22) if I>>v&1],2):repairers|=repair_edges.get(edge,0)
   result=propagate(selected,base[1]|repairers)
   certificate={'birth':ids,'seven':[v for v in range(22) if I>>v&1],'repairers':repairers,'closure_true':closure[0],'closure_false':closure[1]}
   if result is None:
    stats['obligations_implied_by_propagation']+=1
    if first_certificate is None:first_certificate=certificate
   else:
    stats['obligations_not_decided_by_propagation']+=1
    if first_unproved is None:first_unproved=certificate
 row={'source':record['source'],'stats':dict(stats),'first_implied':first_certificate,'first_unproved':first_unproved,'surviving_births':surviving_births};report.append(row);print(row,flush=True)
(D/'ramsey_triple_defect_implication.json').write_text(json.dumps(report,indent=2)+'\n')
