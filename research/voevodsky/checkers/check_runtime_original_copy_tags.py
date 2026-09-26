"""Propagate internal ORIGINAL/COPIED tags through executable port rewrites."""
from contextlib import redirect_stdout
from io import StringIO
from itertools import product
from pathlib import Path
import json
with redirect_stdout(StringIO()):
 from check_copy_two_queries_interleavings import ScheduledTwin

class Tagged(ScheduledTwin):
 def __init__(self,bits,i,j):
  super().__init__(bits,i,j)
  self.tags={name:'COPIED' for name in self.types if name.startswith(('B0_','B1_','K_','N_'))}
  head=self.wires['COPY.p'].split('.')[0];self.origin=[]
  while True:
   self.tags[head]='ORIGINAL';self.origin.append(head)
   if head.startswith('N_'):break
   head=self.wires[head+'.a'].split('.')[0]
  self.tag_checks=0
  self.validate_tags()
 def validate_tags(self):
  assert set(self.tags)=={name for name in self.types if name.startswith(('B0_','B1_','K_','N_'))}
  originals=[name for name in self.tags if self.tags[name]=='ORIGINAL']
  live=[name for name in self.origin if name in self.types]
  assert set(originals)==set(live)
  for a,b in zip(live,live[1:]):assert self.wires[a+'.a']==b+'.p'
  copy=[name for name in self.types if name.startswith('COPY')]
  assert bool(originals)==bool(copy)
  if copy:
   head=self.wires[copy[0]+'.p'].split('.')[0]
   assert self.tags[head]=='ORIGINAL'
  for name in self.types:
   if name.startswith(('Q1','Q2','E_')):
    target=self.wires[name+'.p'].split('.')[0]
    if target in self.tags:assert self.tags[target]=='COPIED'
  self.tag_checks+=1
 def replace(self,names,connections,new_agents):
  if not hasattr(self,'tags'):return super().replace(names,connections,new_agents)
  family='COPY' if names[0].startswith('COPY') else 'OTHER'
  consumed=names[1]
  assert consumed in self.tags
  assert self.tags[consumed]==('ORIGINAL' if family=='COPY' else 'COPIED')
  before=(sum(t=='ORIGINAL' for t in self.tags.values()),sum(t=='COPIED' for t in self.tags.values()))
  for name in names:self.tags.pop(name,None)
  super().replace(names,connections,new_agents)
  for name,_ in new_agents:
   if name.startswith(('B0_','B1_','K_','N_')):self.tags[name]='COPIED'
  after=(sum(t=='ORIGINAL' for t in self.tags.values()),sum(t=='COPIED' for t in self.tags.values()))
  assert after<before,(before,after,names)
  self.validate_tags()

runs=checks=0
for n in range(5):
 for bits in product((0,1),repeat=n):
  for i in range(n+3):
   for j in range(n+3):
    net=Tagged(bits,i,j)
    answer,_=net.run_order((2,1,3,0))
    assert answer==(i<n and bool(bits[i]),j<n and bool(bits[j]))
    checks+=net.tag_checks;runs+=1
# Deliberate tag forgery fails even before a rewrite.
forged=Tagged((1,),0,0)
head=forged.wires['COPY.p'].split('.')[0]
forged.tags[head]='COPIED'
try:forged.validate_tags()
except AssertionError:pass
else:raise AssertionError('forged copy tag accepted')
report={'passed':True,'runs':runs,'tag_invariant_checks':checks,'rule':'COPY consumes ORIGINAL; Q/ERASE consumes COPIED; every fresh B/N/K tagged COPIED','forged_original_head':'rejected','rank':'typed lexicographic node counts decrease after each rewrite','scope':'Runtime constructor/rewriter audit, one priority order bounded n<=4; no arbitrary-n shape theorem or real provenance grant.'}
out=Path(__file__).resolve().parents[1]/'results/runtime-original-copy-tags.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
