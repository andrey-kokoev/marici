from contextlib import redirect_stdout
from io import StringIO
from itertools import product
from pathlib import Path
import json
from forest_canonical import canonical
from typed_net_invariant import validate
from live_membership_semantics import values
with redirect_stdout(StringIO()):
 from check_tagged_individual_redex_schedules import replay
states=edges=skip_waits=0
for n in range(3):
 for bits in product((0,1),repeat=n):
  for indices in product(range(n+3),repeat=2):
   expected=tuple(k<n and bool(bits[k]) for k in indices)
   pending=[()];seen=set()
   while pending:
    prefix=pending.pop();net,choices=replay(bits,indices,prefix)
    assert validate(net) is None
    key=canonical(net,True)
    if key in seen:continue
    seen.add(key);assert values(net)==expected,(bits,indices,prefix)
    skip_waits+=sum(x.startswith(('Q1S','Q2S')) and net.wires[x+'.p'].startswith('COPY') for x in net.types)
    for choice in choices:
     child,_=replay(bits,indices,prefix+(choice,))
     assert validate(child) is None and values(child)==expected
     pending.append(prefix+(choice,));edges+=1
   states+=len(seen)
report={'passed':True,'states':states,'transitions':edges,'skip_phase_COPY_wait_occurrences':skip_waits,'finding':'Both live channel denotations equal original indexed membership before and after every checked rewrite.','scope':'All n<=2 inputs with indices through n+2; not universal semantic preservation proof.'}
out=Path(__file__).resolve().parents[1]/'results/live-membership-semantics.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
