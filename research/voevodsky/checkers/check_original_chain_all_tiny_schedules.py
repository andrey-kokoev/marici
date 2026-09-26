"""Check original-suffix ownership in all alpha states of tiny inputs."""
from contextlib import redirect_stdout
from io import StringIO
from itertools import product
from pathlib import Path
import json
with redirect_stdout(StringIO()):
 from check_individual_eraser_alpha_states import replay
 from check_reachable_family_diamonds import canonical
 from check_full_unary_query_port_graph import Net

def originals(initial):
 name=initial.wires['COPY.p'].split('.')[0];out=[]
 while True:
  out.append(name)
  if name.startswith('N_'):return tuple(out)
  name=initial.wires[name+'.a'].split('.')[0]

def owns(net,origin):
 live=[name for name in origin if name in net.types]
 copiers=[name for name in net.types if name.startswith('COPY')]
 if bool(live)!=bool(copiers) or len(copiers)>1:return False
 if copiers and net.wires[copiers[0]+'.p']!=live[0]+'.p':return False
 for a,b in zip(live,live[1:]):
  if net.wires[a+'.a']!=b+'.p':return False
 for name in net.types:
  if name.startswith(('Q1','Q2','E_')) and net.wires[name+'.p'].split('.')[0] in origin:return False
 return True

fixtures=0;states=0;transitions=0
for n in range(3):
 for word in product((0,1),repeat=n):
  for i,j in product(range(n+2),repeat=2):
   initial,_=replay(word,(i,j),())
   origin=originals(initial)
   pending=[()];seen=set()
   while pending:
    prefix=pending.pop();net,choices=replay(word,(i,j),prefix)
    state=canonical(net)
    if state in seen:continue
    seen.add(state)
    assert owns(net,origin),(word,i,j,prefix)
    for choice in choices:
     child,_=replay(word,(i,j),prefix+(choice,))
     assert owns(child,origin)
     pending.append(prefix+(choice,));transitions+=1
   states+=len(seen);fixtures+=1

# Well-wired adversarial forest with COPY unable to own its marked original B.
mal=Net.__new__(Net);mal.types={};mal.wires={};mal.serial=0;mal.steps=0
for name,ps in (('COPY',('p','a','b')),('B0',('p','a')),('N1',('p',)),('N2',('p',)),('E_1',('p',)),('OUT1',('p',)),('OUT2',('p',))):mal.add(name,ps)
for a,b in (('COPY.p','N1.p'),('COPY.a','OUT1.p'),('COPY.b','OUT2.p'),('E_1.p','B0.p'),('B0.a','N2.p')):mal.link(a,b)
mal.audit();assert not owns(mal,('B0','N2'))
report={'passed':True,'fixtures':fixtures,'alpha_states':states,'validated_transitions':transitions,'malformed_linear_forest':'E owns marked original B while COPY owns different N; rejected','scope':'All individual-redex choices on n<=2 intended inputs only; arbitrary-n inductive ownership proof remains open.'}
out=Path(__file__).resolve().parents[1]/'results/original-chain-all-tiny-schedules.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
