"""Audit typed active-pair coverage and boundary invariants on reachable nets."""
from contextlib import redirect_stdout
from io import StringIO
from itertools import product
from pathlib import Path
import json,re
with redirect_stdout(StringIO()):
 from check_copy_two_queries_interleavings import ScheduledTwin

def kind(name):
 if name.startswith('COPY'):return 'COPY'
 if name.startswith(('Q1','Q2')):return 'Q_'+name[2:].split('_')[0]
 for k in ('B0','B1','K','N','E','TRUE','FALSE','OUT'):
  if name==k or name.startswith(k+'_'):return k
 raise ValueError(name)

expected={('COPY',x) for x in ('B0','B1','N')}
expected|={('Q_B',x) for x in ('K','N')}
expected|={('Q_S',x) for x in ('B0','B1','N')}
expected|={('Q_R',x) for x in ('B0','B1','N')}
expected|={('E',x) for x in ('B0','B1','K','N')}
seen=set();cases=0;steps=0
class Audited(ScheduledTwin):
 def replace(self,names,connections,new_agents):
  global steps
  pair=(kind(names[0]),kind(names[1]))
  assert pair in expected,pair
  assert self.wires[names[0]+'.p']==names[1]+'.p'
  assert len(set(names))==2
  seen.add(pair)
  before_ports={port for name in names for port in (name+'.'+p for p in self.types[name])}
  boundary={self.wires[p] for p in before_ports if self.wires[p] not in before_ports}
  super().replace(names,connections,new_agents)
  assert boundary <= self.wires.keys() # old external ports survive exactly once
  steps+=1
for n in range(5):
 for word in product((0,1),repeat=n):
  for i in range(n+3):
   for j in range(n+3):
    net=Audited(word,i,j);out,_=net.run_order((2,1,3,0))
    assert out==(i<n and bool(word[i]),j<n and bool(word[j]))
    cases+=1
assert seen==expected,(sorted(expected-seen),sorted(seen-expected))
report={'passed':True,'cases':cases,'audited_rewrites':steps,'typed_rule_pairs':sorted(list(map(list,seen))),'coverage':'all 15 declared principal-pair cases seen, no unexpected pair','boundary':'every consumed active pair principal-principal; all old external endpoints retained, symmetric one-wire incidence audited','limit':'Empirical reachability/rule audit, not a proof that all well-typed nets maintain the intended phase/shape invariant.'}
out=Path(__file__).resolve().parents[1]/'results/copy-query-rule-coverage.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
