"""Construct genuinely k-switch-born sevens directly from endpoint links, k=1,2,3. No completed graph or seven-subset enumeration is needed for construction; independent comparison is used only for verification."""
from pathlib import Path
from itertools import product,combinations
from collections import Counter
import json
from ramsey_hall_center_conjecture import decode
from ramsey_mutual_repair_conjecture import apply,sevens
from ramsey_closed_repair_conjecture import disjoint_collections

def independent_sets(A,mask,k,chosen=0):
 if not k:yield chosen;return
 while mask.bit_count()>=k:
  bit=mask&-mask;mask^=bit
  yield from independent_sets(A,mask&~A[bit.bit_length()-1],k-1,chosen|bit)

def link_defects(A,moves):
 k=len(moves);support=0
 for s in moves:
  assert not support&s['support'];support|=s['support']
 result=set();links=[]
 for deleted in product(*(s['removed'] for s in moves)):
  endpoints=[v for e in deleted for v in e];removed={frozenset(e) for e in deleted}
  if any(A[i]>>j&1 for i,j in combinations(endpoints,2) if frozenset((i,j)) not in removed):continue
  L=((1<<len(A))-1)&~support
  for v in endpoints:L&=~A[v]
  base=sum(1<<v for v in endpoints);sets=list(independent_sets(A,L,7-2*k));result.update(base|I for I in sets);links.append({'deleted_edges':deleted,'link_vertices':[v for v in range(len(A)) if L>>v&1],'needed_independent_size':7-2*k,'defect_count':len(sets)})
 return result,links

if __name__=='__main__':
 D=Path(__file__).parent;A=decode((D/'pauli-realization-catalogues'/'r37_22.g6').read_bytes().splitlines()[190]);moves=json.loads((D/'ramsey_block_selection_repair_rules.json').read_text())[-1]['switches'];cache={};stats=Counter();hist=Counter()
 for k in (1,2,3):
  for ids in disjoint_collections(moves,k):
   constructed,links=link_defects(A,[moves[i] for i in ids]);B=A[:]
   for i in ids:B=apply(B,moves[i]['removed'],moves[i]['added'])
   all_bad=set(sevens(B));lower=set()
   for size in range(1,k):
    for subset in combinations(ids,size):lower|=cache[subset]
   assert constructed==all_bad-lower
   if k<3:cache[ids]=all_bad
   stats[f'arity{k}_birth_sets_checked']+=1;stats[f'arity{k}_defect_occurrences']+=len(constructed)
   for L in links:hist[k,len(L['link_vertices'])]+=1
 reps=json.loads((D/'ramsey_local_switch_incidence_profiles.json').read_text())['representatives'];examples={str(i):link_defects(A,[reps[i]])[1] for i in (10,12)};result={'stats':dict(stats),'link_size_histogram':{str(k):v for k,v in sorted(hist.items())},'local_twin_examples':examples};(D/'ramsey_defect_link_constructor.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
