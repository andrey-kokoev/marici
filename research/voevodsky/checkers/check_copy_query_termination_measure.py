"""Check a lexicographic termination rank on wired copier/two-query rewrites."""
from contextlib import redirect_stdout
from io import StringIO
from itertools import product
from pathlib import Path
import json
with redirect_stdout(StringIO()):
 from check_copy_two_queries_interleavings import ScheduledTwin

class Ranked(ScheduledTwin):
 def __init__(self,bits,i,j):
  super().__init__(bits,i,j)
  head=self.wires['COPY.p'].split('.')[0];original=set()
  while True:
   original.add(head)
   if head.startswith('N_'):break
   head=self.wires[head+'.a'].split('.')[0]
  self.original=original;self.transitions=0
 def rank(self):
  primary=len(self.original & self.types.keys())
  secondary=sum(n.startswith(('B0_','B1_','K_','N_')) and n not in self.original for n in self.types)
  return primary,secondary
 def replace(self,names,connections,new_agents):
  before=self.rank()
  super().replace(names,connections,new_agents)
  after=self.rank()
  assert after<before,(before,after,names)
  self.transitions+=1

cases=0;maximum=0
for n in range(6):
 for bits in product((0,1),repeat=n):
  for i in range(n+2):
   for j in range(n+2):
    net=Ranked(bits,i,j)
    answers,_=net.run_order((2,1,3,0))
    assert answers==(i<n and bool(bits[i]),j<n and bool(bits[j]))
    maximum=max(maximum,net.transitions);cases+=1
report={'passed':True,'cases':cases,'rank':'lexicographic (live original support B/N nodes, live nonoriginal B/N/K nodes)','strict_decrease':'every tested COPY/QUERY/ERASE rewrite under query-first schedule','max_steps':maximum,'general_argument':'COPY consumes one original B/N; all other rules consume at least one nonoriginal B/N/K and never create one','qualification':'Rank applies to intended finite input class and listed rules; rule table checked operationally on tested runs, not a machine-checked universal proof or extension to add/union.'}
out=Path(__file__).resolve().parents[1]/'results/copy-query-termination-measure.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
