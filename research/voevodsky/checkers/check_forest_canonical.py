from contextlib import redirect_stdout
from io import StringIO
from copy import deepcopy
from pathlib import Path
import json
from forest_canonical import canonical
with redirect_stdout(StringIO()):
 from check_tagged_individual_redex_schedules import replay,fixtures
 from check_reachable_family_diamonds import canonical as old
 from check_full_unary_query_port_graph import Net

def rename(net):
 out=deepcopy(net);mapping={}
 names=sorted(net.types)
 for i,n in enumerate(names):
  parts=n.rsplit('_',1)
  mapping[n]=parts[0]+'_'+str(90000-i) if len(parts)==2 and parts[1].isdigit() else n
 def port(p):
  n,q=p.split('.');return mapping[n]+'.'+q
 out.types={mapping[n]:ps for n,ps in net.types.items()}
 out.wires={port(p):port(q) for p,q in net.wires.items()}
 if hasattr(net,'tags'):out.tags={mapping[n]:t for n,t in net.tags.items()}
 return out

# Two garbage chains of unequal lengths expose serial-dependent component order.
net=Net.__new__(Net);net.types={};net.wires={}
for n,ps in [('OUT1',('p',)),('OUT2',('p',)),('TRUE_1',('p',)),('FALSE_2',('p',)),('E_3',('p',)),('N_4',('p',)),('E_5',('p',)),('K_6',('p','a')),('N_7',('p',))]:net.add(n,ps)
for p,q in [('OUT1.p','TRUE_1.p'),('OUT2.p','FALSE_2.p'),('E_3.p','N_4.p'),('E_5.p','K_6.p'),('K_6.a','N_7.p')]:net.link(p,q)
assert old(net)!=old(rename(net))
assert canonical(net)==canonical(rename(net))
old_total=new_total=checks=0
for bits,indices in fixtures:
 pending=[()];seen=set();new=set()
 while pending:
  prefix=pending.pop();net,choices=replay(bits,indices,prefix)
  key=old(net)
  if key in seen:continue
  seen.add(key);new.add(canonical(net))
  assert canonical(net,True)==canonical(rename(net),True)
  checks+=1;pending.extend(prefix+(c,) for c in choices)
 old_total+=len(seen);new_total+=len(new)
report={'passed':True,'old_serialized_states':old_total,'new_forest_classes':new_total,'renaming_checks':checks,'old_counterexample':'unequal detached garbage tails change old signature after renaming','scope':'Exact finite forest encoding argument; tests on four fixtures and a constructed counterexample. Historical extended counts not yet recomputed.'}
out=Path(__file__).resolve().parents[1]/'results/forest-canonical.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
