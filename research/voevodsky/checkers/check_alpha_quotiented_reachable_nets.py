"""Alpha-quotiented dynamic-family state search on tiny copier/query nets."""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json
with redirect_stdout(StringIO()):
 from check_reachable_family_diamonds import snapshot,canonical

fixtures=(((),(0,0)),((0,),(0,1)),((1,),(0,0)),((1,0),(1,0)))
results=[]
for bits,indices in fixtures:
 pending=[()];seen=set();terminal=0;edges=0;max_depth=0
 while pending:
  prefix=pending.pop()
  net,options=snapshot(bits,indices,prefix)
  net.audit()
  state=canonical(net)
  if state in seen:continue
  seen.add(state);max_depth=max(max_depth,len(prefix))
  assert sum(n.startswith('COPY') for n in net.types)<=1
  assert sum(n.startswith('Q1') for n in net.types)<=1
  assert sum(n.startswith('Q2') for n in net.types)<=1
  assert all(net.wires['OUT'+str(i)+'.p'].split('.')[0] in net.types for i in (1,2))
  if not options:
   assert len(net.types)==4
   answer=tuple(net.wires['OUT'+str(i)+'.p'].startswith('TRUE_') for i in (1,2))
   assert answer==(indices[0]<len(bits) and bool(bits[indices[0]]),indices[1]<len(bits) and bool(bits[indices[1]]))
   terminal+=1
  else:
   for family in options:
    child=prefix+(family,)
    successor,_=snapshot(bits,indices,child)
    assert canonical(successor)!=state
    edges+=1;pending.append(child)
  assert len(seen)<100000
 results.append({'bits':bits,'indices':indices,'alpha_states':len(seen),'transitions':edges,'terminal_states':terminal,'max_depth':max_depth})
assert all(r['terminal_states']==1 for r in results)
report={'passed':True,'fixtures':results,'search':'dynamic enabled-family choices with alpha-canonical graph deduplication','invariants':'linear wires; at most one COPY and one Q agent per output; unique correct terminal graph per fixture','limit':'Same-family erasers deterministic, only four tiny initial nets; not an inductive grammar or universal confluence proof.'}
out=Path(__file__).resolve().parents[1]/'results/alpha-quotiented-reachable-nets.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
