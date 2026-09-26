"""Validate phase-tail compatibility on reachable tiny port graphs."""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json
with redirect_stdout(StringIO()):
 from check_individual_eraser_alpha_states import replay
 from check_reachable_family_diamonds import canonical
 from check_forest_invariant_insufficiency import net as malformed

def typ(name):
 if name.startswith('COPY'):return 'COPY'
 if name in ('Q_B','Q_S','Q_R'):return name
 if name.startswith(('Q1','Q2')):return 'Q_'+name[2:].split('_')[0]
 for p in ('B0','B1','K','N','E','TRUE','FALSE','OUT'):
  if name==p or name.startswith(p+'_') or (p=='OUT' and name in ('OUT1','OUT2')):return p
 raise ValueError(name)

allowed={'COPY':{'B0','B1','N'},'Q_B':{'K','N'},'Q_S':{'B0','B1','N','COPY'},'Q_R':{'B0','B1','N','COPY'},'E':{'B0','B1','K','N','COPY'}}
def validate(net):
 net.audit();waits=0
 for name in net.types:
  t=typ(name)
  if t not in allowed:continue
  peer=net.wires[name+'.p'];neighbor=peer.split('.')[0]
  if typ(neighbor) not in allowed[t]:return False,waits
  if typ(neighbor)=='COPY':
   if peer.split('.')[1] not in ('a','b'):return False,waits
   waits+=1
  elif peer.split('.')[1]!='p':return False,waits
  if t.startswith('Q_'):
   if name.startswith(('Q1','Q2')):
    channel=int(name[1]);out=net.wires[name+'.r']
    if out!='OUT'+str(channel)+'.p':return False,waits
 return True,waits

assert not validate(malformed)[0]
fixtures=(((),(0,0)),((1,),(0,1)),((1,0),(1,0)),((0,1),(2,2)))
visited=0;edges=0;waits=0
for bits,indices in fixtures:
 pending=[()];seen=set()
 while pending:
  prefix=pending.pop();net,choices=replay(bits,indices,prefix)
  state=canonical(net)
  if state in seen:continue
  seen.add(state)
  ok,w=validate(net)
  assert ok,(bits,indices,prefix)
  waits+=w;visited+=1
  for choice in choices:
   child,_=replay(bits,indices,prefix+(choice,))
   assert validate(child)[0],(bits,indices,prefix,choice,{name:(typ(name),child.wires.get(name+'.p')) for name in child.types if typ(name) in allowed})
   edges+=1;pending.append(prefix+(choice,))
report={'passed':True,'alpha_states':visited,'validated_transitions':edges,'temporary_query_or_eraser_to_COPY_auxiliary_occurrences':waits,'malformed_Q_B_TRUE':'rejected','scope':'Typed principal-neighbor and channel-output checks on four small reachable inputs; not complete recursive component grammar or arbitrary-n inductive proof.'}
out=Path(__file__).resolve().parents[1]/'results/typed-tail-grammar.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
