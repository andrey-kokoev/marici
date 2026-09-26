"""Boundary-port checks for COPY--NIL and ERASE--K rewrite templates."""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json
with redirect_stdout(StringIO()):
 from check_tagged_individual_redex_schedules import replay,fixtures
 from check_reachable_family_diamonds import canonical

inputs=fixtures+(((),(2,2)),((1,),(3,3)))
copy_pairs={};erases=0;states=0
for bits,indices in inputs:
 pending=[()];seen=set()
 while pending:
  prefix=pending.pop();net,choices=replay(bits,indices,prefix)
  key=canonical(net)
  if key in seen:continue
  seen.add(key)
  for choice in choices:
   rank,name=choice
   if rank==0:
    copy=next(x for x in net.types if x.startswith('COPY'))
    source=net.wires[copy+'.p'].split('.')[0]
    if source.startswith('N_'):
     left=net.wires[copy+'.a'];right=net.wires[copy+'.b']
     def label(port):
      head,p=port.split('.')
      if head.startswith(('Q1','Q2')):return 'Q'+head[2:].split('_')[0]+'.'+p
      if head.startswith('B0_') or head.startswith('B1_'):return 'B.a'
      if head.startswith('E_'):return 'E.p'
      raise AssertionError(port)
     pair=(label(left),label(right));copy_pairs[str(pair)]=copy_pairs.get(str(pair),0)+1
     child,_=replay(bits,indices,prefix+(choice,))
     assert not any(x.startswith('COPY') for x in child.types)
     for external in (left,right):
      successor=child.wires[external].split('.')[0]
      assert successor.startswith('N_') and successor not in net.types
      assert child.wires[successor+'.p']==external
   elif rank==3 and net.wires[name+'.p'].split('.')[0].startswith('K_'):
    budget=net.wires[name+'.p'].split('.')[0]
    suffix=net.wires[budget+'.a'];assert suffix.endswith('.p') and suffix.split('.')[0].startswith(('K_','N_'))
    child,_=replay(bits,indices,prefix+(choice,))
    assert name not in child.types and budget not in child.types
    assert child.wires[suffix].split('.')[0].startswith('E_')
    erases+=1
   pending.append(prefix+(choice,))
 states+=len(seen)
assert erases>0 and copy_pairs
report={'passed':True,'states':states,'copy_nil_boundary_pairs':copy_pairs,'erase_k_steps':erases,'template':'COPY--NIL replaces each attached output consumer by fresh NIL.p; ERASE--K replaces the eraser/budget head with a fresh eraser at the K/N successor','scope':'Observed reachable boundary contexts only; no proof every abstractly typed pairing preserves global root coverage.'}
out=Path(__file__).resolve().parents[1]/'results/nil-copy-erase-k-boundaries.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
