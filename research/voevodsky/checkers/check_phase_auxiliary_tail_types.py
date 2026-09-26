"""Check query phase auxiliary roles (support versus budget)."""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json
with redirect_stdout(StringIO()):
 from check_tagged_individual_redex_schedules import replay,fixtures
 from check_reachable_family_diamonds import canonical
 from check_typed_tail_grammar import validate as principal

def kind(name):return name.split('_')[0]
def valid(net):
 if not principal(net)[0]:return False
 for name in net.types:
  if not name.startswith(('Q1','Q2')):continue
  phase=name[2:].split('_')[0]
  if phase=='R':
   if name+'.a' in net.wires:return False
   continue
  peer=net.wires[name+'.a'];head,port=peer.split('.')
  if phase=='B':
   if kind(head) not in ('B0','B1','N','COPY') or port not in ('p','a','b'):return False
   if kind(head)=='COPY' and port=='p':return False
   if kind(head)!='COPY' and port!='p':return False
  elif phase=='S':
   if kind(head) not in ('K','N') or port!='p':return False
  else:return False
 return True

states=transitions=0
for bits,indices in fixtures:
 queue=[()];seen=set()
 while queue:
  prefix=queue.pop();net,choices=replay(bits,indices,prefix)
  key=canonical(net)
  if key in seen:continue
  seen.add(key)
  assert valid(net),(bits,indices,prefix,{x:net.wires[x+'.a'] for x in net.types if x.startswith(('Q1','Q2')) and x+'.a' in net.wires})
  for c in choices:
   child,_=replay(bits,indices,prefix+(c,))
   assert valid(child)
   transitions+=1;queue.append(prefix+(c,))
 states+=len(seen)
report={'passed':True,'states':states,'transitions':transitions,'phase_roles':'Q_B.a faces copied support B/N or COPY auxiliary; Q_S.a faces budget K/N; Q_R has no auxiliary','scope':'Four tiny inputs all redex choices, local phase-role conditions only; full recursive grammar and arbitrary-n preservation unproved.'}
out=Path(__file__).resolve().parents[1]/'results/phase-auxiliary-tail-types.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
