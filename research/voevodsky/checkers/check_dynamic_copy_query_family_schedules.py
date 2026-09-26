"""Enumerate dynamic enabled-FAMILY decisions for tiny fully wired nets.

COPY/Q1/Q2/ERASE are families. Multiple simultaneous ERASE nodes use the
existing deterministic within-family order; this is not all redex orders.
"""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json
with redirect_stdout(StringIO()):
 from check_copy_two_queries_interleavings import ScheduledTwin

class Branch(Exception):
 def __init__(self,options):self.options=options

def explore(bits,i,j,cap=200000):
 pending=[()];completed=0;branches=0;max_depth=0
 while pending:
  prefix=pending.pop()
  def choice(history,options):
   nonlocal branches
   distinct=tuple(dict.fromkeys(options))
   if len(history)==len(prefix):
    branches+=1
    raise Branch(distinct)
   chosen=prefix[len(history)]
   assert chosen in distinct
   return (chosen,)+tuple(x for x in range(4) if x!=chosen)
  try:
   outputs,history=ScheduledTwin(bits,i,j).run_order(choice)
  except Branch as split:
   pending.extend(prefix+(x,) for x in split.options)
  else:
   expected=(i<len(bits) and bool(bits[i]),j<len(bits) and bool(bits[j]))
   assert outputs==expected
   completed+=1;max_depth=max(max_depth,len(history))
  assert completed+branches<=cap, ('exploration cap',bits,i,j,completed,branches)
 return completed,branches,max_depth

fixtures=(((),0,0),((0,),0,0),((1,),0,1),((1,0),1,0))
results=[]
for bits,i,j in fixtures:
 paths,branches,depth=explore(bits,i,j)
 results.append({'bits':bits,'indices':[i,j],'terminal_family_schedules':paths,'decision_nodes':branches,'max_depth':depth})
report={'passed':True,'fixtures':results,'coverage':'all dynamically changing enabled-family choices for four named tiny fixtures','limit':'Within-family simultaneous erasers use deterministic order; no fresh-ID alpha-canonical graph search or general confluence theorem.'}
out=Path(__file__).resolve().parents[1]/'results/dynamic-copy-query-family-schedules.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
