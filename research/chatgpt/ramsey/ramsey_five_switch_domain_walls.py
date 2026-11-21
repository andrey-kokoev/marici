"""Derive exact Boolean conditions for every possible independent seven over the five-switch cube. Test a domain-wall description in intrinsic C5 order."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
from ramsey_hall_center_conjecture import decode
from ramsey_mutual_repair_conjecture import apply,sevens
from ramsey_repair_cyclic_phase import key,transport
D=Path(__file__).parent
data=json.loads((D/'ramsey_hall_center_conjecture.json').read_text());A=decode(next(r for r in data['regular'] if r['record']==191)['graph6'].encode());stored=json.loads((D/'ramsey_closed_repair_size5.json').read_text())[1]['first_valid_example']['switches'];p=json.loads((D/'ramsey_repair_cyclic_phase.json').read_text())[1]['unique_C5_generator'];lookup={key(s):s for s in stored};q=key(stored[0]);moves=[]
for _ in range(5):moves.append(lookup[q]);q=transport(q,p)
assert q==key(moves[0]);universe=set();counts={}
for state in range(32):
 B=A[:]
 for i,s in enumerate(moves):
  if state>>i&1:B=apply(B,s['removed'],s['added'])
 bad=set(sevens(B));counts[state]=len(bad);universe|=bad
removed={tuple(sorted(e)):i for i,s in enumerate(moves) for e in s['removed']};added={tuple(sorted(e)):i for i,s in enumerate(moves) for e in s['added']};patterns=Counter();examples={}
for mask in universe:
 vertices=[v for v in range(22) if mask>>v&1];ones=set();zeros=set()
 for edge in combinations(vertices,2):
  a,b=edge
  if A[a]>>b&1:assert edge in removed;ones.add(removed[edge])
  elif edge in added:zeros.add(added[edge])
 assert not ones&zeros;pattern=(tuple(sorted(ones)),tuple(sorted(zeros)));patterns[pattern]+=1;examples.setdefault(pattern,vertices)
for state,n in counts.items():assert n==sum(m for (ones,zeros),m in patterns.items() if all(state>>i&1 for i in ones) and all(not(state>>i&1) for i in zeros))
print('distinct seven-sets',len(universe),'patterns',dict(patterns))
for step in (1,2):print('domain wall step',step,'fits',all(n==3*sum((state>>i&1)!=(state>>((i+step)%5)&1) for i in range(5)) for state,n in counts.items()))
result={'switches_in_cyclic_order':moves,'patterns':[{'ones':o,'zeros':z,'multiplicity':n,'example':examples[o,z]} for (o,z),n in sorted(patterns.items())],'counts':counts};(D/'ramsey_five_switch_domain_walls.json').write_text(json.dumps(result,indent=2)+'\n')
