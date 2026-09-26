"""Separate allocator high-water state from the graph-only invariant."""
from contextlib import redirect_stdout
from io import StringIO
from copy import deepcopy
from pathlib import Path
import json
from typed_net_invariant import validate
from forest_canonical import canonical
with redirect_stdout(StringIO()):
 from check_tagged_individual_redex_schedules import replay,fixtures
 from check_admitted_mutation_closure import step

def high_water(net):
 suffixes=[int(n.rsplit('_',1)[1]) for n in net.types if '_' in n and n.rsplit('_',1)[1].isdigit()]
 return isinstance(net.serial,int) and net.serial>=max([0]+suffixes)

states=edges=0
for bits,indices in fixtures:
 pending=[()];seen=set()
 while pending:
  prefix=pending.pop();net,choices=replay(bits,indices,prefix)
  key=canonical(net,True)
  if key in seen:continue
  seen.add(key);assert high_water(net)
  for c in choices:
   child,_=replay(bits,indices,prefix+(c,));assert high_water(child)
   pending.append(prefix+(c,));edges+=1
 states+=len(seen)
# Empty original NIL is N_1. Resetting serial leaves the graph valid but
# COPY--N tries to create N_1 again. An output-side NIL collision is even
# stronger: it survives the removal of the active pair.
base,_=replay((),(0,0),())
other_nil=next(n for n in base.types if n.startswith('N_') and n not in base.origin)
bad=deepcopy(base);bad.serial=int(other_nil.split('_')[1])-1
assert validate(bad) is None and not high_water(bad)
try:step(bad,'COPY')
except AssertionError:collision=True
else:raise AssertionError('expected duplicate fresh name')
report={'passed':True,'states':states,'transitions':edges,'graph_valid_stale_allocator':'COPY--N collides with live budget NIL after serial reset','scope':'Four fixture high-water checks plus concrete counterexample. High-water condition is sufficient for freshness, not necessary; graph-only validator deliberately omits execution metadata.'}
out=Path(__file__).resolve().parents[1]/'results/allocator-execution-invariant.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
