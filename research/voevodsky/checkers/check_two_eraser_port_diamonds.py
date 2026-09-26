"""Two distinct enabled erasers commute on wired support/query graph fragments."""
from contextlib import redirect_stdout
from copy import deepcopy
from io import StringIO
from itertools import product
from pathlib import Path
import json
with redirect_stdout(StringIO()):
 from check_reachable_family_diamonds import snapshot,canonical
 from check_copy_two_queries_interleavings import ScheduledTwin

def enabled_erasers(net):
 return tuple(n for n in net.types if n.startswith('E_') and net.wires[n+'.p'].split('.')[0].startswith(('N_','B0_','B1_','K_')))

def erase(net,name):
 other=net.wires[name+'.p'].split('.')[0]
 assert other.startswith(('N_','B0_','B1_','K_'))
 if other.startswith('N_'):net.replace((name,other),[],[])
 else:
  nxt=net.fresh('E')
  net.replace((name,other),[(other+'.a',nxt+'.p')],[(nxt,('p',))])
 return net

checked=0;fixtures=0
for bits in product((0,1),repeat=3):
 for indices in ((0,0),(1,2),(3,1)):
  fixtures+=1
  _,history=ScheduledTwin(bits,*indices).run_order((1,2,0,3))
  for depth in range(len(history)+1):
   net,_=snapshot(bits,indices,tuple(history[:depth]))
   erasers=enabled_erasers(net)
   if len(erasers)<2:continue
   a,b=erasers[:2]
   left=erase(erase(deepcopy(net),a),b)
   right=erase(erase(deepcopy(net),b),a)
   assert canonical(left)==canonical(right),(bits,indices,depth)
   checked+=1
assert checked>0
report={'passed':True,'source_fixtures':fixtures,'same_family_eraser_diamonds':checked,'result':'two distinct enabled ERASE active pairs commute modulo fresh IDs, port linearity audited after each rewrite','scope':'Only reachable snapshots from one static priority per fixture; general disjoint-redex lemma and arbitrary contexts not verified.'}
out=Path(__file__).resolve().parents[1]/'results/two-eraser-port-diamonds.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
