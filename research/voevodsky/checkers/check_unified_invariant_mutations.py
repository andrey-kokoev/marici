"""Deterministic single-tag and two-wire adversarial mutations; no reachability claim."""
from contextlib import redirect_stdout
from io import StringIO
from copy import deepcopy
from itertools import combinations
from pathlib import Path
import json
from typed_net_invariant import validate
with redirect_stdout(StringIO()):
 from check_tagged_individual_redex_schedules import replay,fixtures
 from check_reachable_family_diamonds import canonical
counts={};accepted=0;tested=0;states=0
for bits,indices in fixtures:
 pending=[()];seen=set()
 while pending:
  prefix=pending.pop();net,choices=replay(bits,indices,prefix)
  key=canonical(net)
  if key in seen:continue
  seen.add(key);assert validate(net) is None
  wires=[(p,q) for p,q in net.wires.items() if p<q]
  for (a,b),(c,d) in combinations(wires,2):
   for x,y in ((c,d),(d,c)):
    bad=deepcopy(net)
    for p,q in ((a,x),(b,y)):
     bad.wires[p]=q;bad.wires[q]=p
    result=validate(bad);tested+=1
    if result is None:accepted+=1
    else:counts[result]=counts.get(result,0)+1
  for node in net.tags:
   bad=deepcopy(net);bad.tags[node]='COPIED' if net.tags[node]=='ORIGINAL' else 'ORIGINAL'
   result=validate(bad);assert result is not None
   counts[result]=counts.get(result,0)+1;tested+=1
  pending.extend(prefix+(choice,) for choice in choices)
 states+=len(seen)
report={'passed':True,'base_states':states,'mutations':tested,'rejected_by_first_clause':counts,'accepted_rewirings':accepted,'scope':'Accepted rewires may satisfy the invariant without being reachable; no assertion that every mutation is invalid. Counts measure first-failure coverage, not independent clause necessity or universal closure.'}
out=Path(__file__).resolve().parents[1]/'results/unified-invariant-mutations.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
