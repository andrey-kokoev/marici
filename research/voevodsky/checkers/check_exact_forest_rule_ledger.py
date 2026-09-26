"""Recount extended inputs using exact tagged forest keys and unified invariant."""
from contextlib import redirect_stdout
from io import StringIO
from itertools import product
from pathlib import Path
import json
from forest_canonical import canonical
from typed_net_invariant import validate
with redirect_stdout(StringIO()):
 from check_tagged_individual_redex_schedules import replay
cases={};states=arcs=fixtures=terminals=0
for n in range(3):
 for bits in product((0,1),repeat=n):
  for indices in product(range(n+3),repeat=2):
   fixtures+=1;pending=[()];seen=set();ends=set()
   while pending:
    prefix=pending.pop();net,choices=replay(bits,indices,prefix)
    assert validate(net) is None,validate(net)
    key=canonical(net,tagged=True)
    if key in seen:continue
    seen.add(key)
    if not choices:
     assert len(net.types)==4
     answer=tuple(net.wires['OUT'+str(i)+'.p'].startswith('TRUE_') for i in (1,2))
     assert answer==tuple(k<n and bool(bits[k]) for k in indices)
     ends.add(key)
    for rank,eraser in choices:
     agent=eraser if rank==3 else next(x for x in net.types if x.startswith('COPY' if rank==0 else 'Q'+str(rank)))
     family='COPY' if rank==0 else ('E' if rank==3 else 'Q_'+agent[2:].split('_')[0])
     rule=family+'--'+net.wires[agent+'.p'].split('.')[0].split('_')[0]
     cases[rule]=cases.get(rule,0)+1
     child,_=replay(bits,indices,prefix+((rank,eraser),))
     assert validate(child) is None,(rule,validate(child))
     pending.append(prefix+((rank,eraser),));arcs+=1
   assert len(ends)==1
   terminals+=len(ends);states+=len(seen)
assert len(cases)==15
report={'passed':True,'fixtures':fixtures,'exact_tagged_forest_classes':states,'transitions':arcs,'terminal_classes_per_input_sum':terminals,'rule_counts':cases,'historical_serialized_counts':{'states':11319,'transitions':23641},'scope':'Exhaustive enabled individual-redex search n<=2 and indices through n+2, summed per input. Universal preservation and confluence not proved.'}
out=Path(__file__).resolve().parents[1]/'results/exact-forest-rule-ledger.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
