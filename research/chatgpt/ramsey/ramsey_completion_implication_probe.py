"""Extract exact completion CNF for disjoint two-edge-removal blocks. Nontrivial blue-seven clauses have width<=2. Search unsatisfiable systems not refutable by unit propagation."""
from pathlib import Path
from itertools import combinations,product
from collections import Counter
import json
from ramsey_hall_center_conjecture import decode
from ramsey_mutual_repair_conjecture import switches,sevens,apply
D=Path(__file__).parent;data=json.loads((D/'ramsey_hall_center_conjecture.json').read_text());stats=Counter();found=None

def options(removed):
 (a,b),(c,d)=removed;return [((a,c),(b,d)),((a,d),(b,c))]
def propagate(clauses):
 clauses=set(clauses);assignment={}
 while True:
  if () in clauses:return True,assignment
  units=[c[0] for c in clauses if len(c)==1]
  if not units:return False,assignment
  literal=units[0];variable,value=divmod(literal,2);assignment[variable]=value;clauses={tuple(x for x in c if x!=literal^1) for c in clauses if literal not in c}

for record in reversed(data['regular']):
 A=decode(record['graph6'].encode());blocks=sorted({tuple(tuple(e) for e in s['removed']) for s in switches(A)});supports=[{v for e in b for v in e} for b in blocks]
 for block in blocks:
  legal=0
  for added in options(block):
   if any(A[u]>>v&1 for u,v in added):continue
   B=apply(A,block,added)
   legal+=not any(B[u]&B[v] for u,v in added)
  stats[f'blocks_with_{legal}_triangle_free_completions']+=1
 for ids in combinations(range(len(blocks)),3):
  if any(supports[i]&supports[j] for i,j in combinations(ids,2)):continue
  stats['triples']+=1;removed=[blocks[i] for i in ids];opts=[options(b) for b in removed];H=A[:]
  for block in removed:
   for i,j in block:H[i]^=1<<j;H[j]^=1<<i
  clauses=set();evidence={}
  for i,choices in enumerate(opts):
   for b,edges in enumerate(choices):
    if any(A[u]>>v&1 for u,v in edges):
     clause=(2*i+(1-b),);clauses.add(clause);evidence.setdefault(clause,{'kind':'existing_edge','forbidden_edges':edges});continue
    for u,v in edges:
     guard=H[u]&H[v]
     if guard:
      clause=(2*i+(1-b),);clauses.add(clause);evidence.setdefault(clause,{'kind':'triangle','forbidden_edges':edges,'guard':(guard&-guard).bit_length()-1});break
  for I in sevens(H):
   literals=[];tautology=False
   for i,choices in enumerate(opts):
    hit=[b for b,edges in enumerate(choices) if any(I>>u&1 and I>>v&1 for u,v in edges)]
    if len(hit)==2:tautology=True;break
    if hit:literals.append(2*i+hit[0])
   if tautology:continue
   clause=tuple(literals);assert len(clause)<=2;clauses.add(clause);evidence.setdefault(clause,{'kind':'independent_seven','vertices':[v for v in range(22) if I>>v&1]})
   if not clause:break
  contradiction,assignment=propagate(clauses)
  if contradiction:stats['unit_refutations']+=1;continue
  solutions=[bits for bits in product((0,1),repeat=3) if all(any(bits[x//2]==x%2 for x in c) for c in clauses)]
  if solutions:stats['satisfiable']+=1;continue
  stats['collective_refutations']+=1;found={'source':record['record'],'removed_blocks':removed,'options':opts,'clauses':[{'literals':c,'evidence':evidence[c]} for c in sorted(clauses)],'unit_assignment':assignment};break
 print('source',record['record'],'stats',dict(stats),flush=True)
 if found:break
result={'stats':dict(stats),'first_collective_obstruction':found};(D/'ramsey_completion_implication_probe.json').write_text(json.dumps(result,indent=2)+'\n');print('stats',dict(stats),'collective obstruction',found)
