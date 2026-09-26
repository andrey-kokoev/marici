"""COPY rewrites unblock waiting query/eraser principal ports locally."""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json
with redirect_stdout(StringIO()):
 from check_individual_eraser_alpha_states import replay
 from check_reachable_family_diamonds import canonical

def waiting(net):
 return tuple((name,net.wires[name+'.p']) for name in net.types
  if name.startswith(('Q1','Q2','E_')) and net.wires[name+'.p'].split('.')[0].startswith('COPY'))

fixtures=(((),(0,0)),((1,),(0,1)),((1,0),(1,0)),((0,1),(2,2)))
states=0;waits=0;erasure_waits=0;both_waits=0
for bits,indices in fixtures:
 pending=[()];seen=set()
 while pending:
  prefix=pending.pop();net,choices=replay(bits,indices,prefix)
  signature=canonical(net)
  if signature in seen:continue
  seen.add(signature);states+=1
  active=waiting(net)
  if active:
   assert any(n.startswith('COPY') for n in net.types)
   assert any(rank==0 for rank,_ in choices)
   child,_=replay(bits,indices,prefix+((0,None),))
   child.audit()
   for name,old_peer in active:
    assert name in child.types
    new_peer=child.wires[name+'.p']
    assert new_peer.split('.')[0].startswith(('B0_','B1_','N_'))
    assert new_peer.endswith('.p')
    assert new_peer!=old_peer
    waits+=1
    erasure_waits+=name.startswith('E_')
   both_waits+=len(active)==2
  for choice in choices:pending.append(prefix+(choice,))
report={'passed':True,'states':states,'waiting_ports_reconnected':waits,'eraser_waits':erasure_waits,'both_outputs_waiting_states':both_waits,'finding':'every sampled Q/E wait at COPY auxiliary has enabled COPY--B/N active pair; one COPY rewrite reconnects waiters to fresh B/N principals','limit':'Four tiny input graphs; rank argument needs inductive typed-chain invariant for all finite lengths.'}
out=Path(__file__).resolve().parents[1]/'results/copy-aux-wait-progress.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
