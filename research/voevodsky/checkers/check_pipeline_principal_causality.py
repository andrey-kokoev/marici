"""Necessary principal causality conditions, not a complete pipeline invariant."""
from sequenced_set import SequencedSet
from itertools import product
from pathlib import Path
import json
controls={'COPY','QB','QS','QR','E','AB','AS','AR','UL','U0','U1'}
def check(net):
 waits=0
 for n in net.types:
  k=net.kind(n)
  if k not in controls:continue
  peer,port=net.wires[n+'.p'].split('.');s=net.stage[n];t=net.stage[peer]
  assert t<=s,(n,peer,s,t)
  if k=='COPY':assert t<s,(n,peer,s,t)
  if port!='p':
   waits+=1
   assert net.kind(peer) in controls
   if t==s:assert k in ('QB','QS','QR','E') and net.kind(peer)=='COPY' and port in ('a','b')
 return waits
runs=checks=waits=0
for size in range(4):
 for word in product((0,1),repeat=size):
  for i,j in product(range(size+3),repeat=2):
   program=[('member',j),('add',i),('member',j),('union',(0,1,0)),('add',j),('member',i)]
   for reverse in (False,True):
    net=SequencedSet(word,program)
    while True:
     waits+=check(net);checks+=1
     choices=net.enabled()
     if not choices:break
     choose=max if reverse else min
     net.step(choose(choices,key=lambda n:net.stage[n]))
    net.execute();runs+=1
report={'passed':True,'runs':runs,'checked_states_including_repetitions':checks,'wait_occurrences':waits,'scope':'Two stage priorities; necessary principal causality only, saved-tail roles and universal closure not established.'}
out=Path(__file__).resolve().parents[1]/'results/pipeline-principal-causality.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
