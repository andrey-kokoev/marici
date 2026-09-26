from contextlib import redirect_stdout
from io import StringIO
from copy import deepcopy
from pathlib import Path
import json
from typed_net_invariant import validate
with redirect_stdout(StringIO()):
 from check_tagged_individual_redex_schedules import replay,fixtures
 from check_reachable_family_diamonds import canonical
states=edges=0
for bits,indices in fixtures:
 pending=[()];seen=set()
 while pending:
  prefix=pending.pop();net,choices=replay(bits,indices,prefix)
  key=canonical(net)
  if key in seen:continue
  seen.add(key);assert validate(net) is None,validate(net)
  for c in choices:
   child,_=replay(bits,indices,prefix+(c,));assert validate(child) is None,validate(child)
   pending.append(prefix+(c,));edges+=1
 states+=len(seen)
net,_=replay((1,0),(1,2),());bad=deepcopy(net)
bad.tags[bad.origin[-1]]='COPIED';assert validate(bad)=='origin-tags'
bad=deepcopy(net);bad.types['OUT1']=('p','a');assert validate(bad)=='arity'
report={'passed':True,'states':states,'transitions':edges,'negative_controls':['origin-tags','arity'],'scope':'Unified candidate predicate on four fixtures; other clauses need independent negative controls, tagged quotient and universal preservation unproved.'}
out=Path(__file__).resolve().parents[1]/'results/unified-typed-invariant.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
