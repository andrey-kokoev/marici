"""A rooted typed forest can lose root coverage on COPY--NIL."""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json
with redirect_stdout(StringIO()):
 from check_full_unary_query_port_graph import Net
 from check_rooted_component_coverage import rooted
 from check_recursive_tail_endpoints import valid as typed
net=Net.__new__(Net);net.types={};net.wires={};net.serial=0;net.steps=0
for name,ports in (('COPY',('p','a','b')),('N_1',('p',)),('B0_1',('p','a')),('N_2',('p',)),('E_1',('p',)),('OUT1',('p',)),('OUT2',('p',)),('TRUE_1',('p',)),('FALSE_1',('p',))):net.add(name,ports)
for a,b in (('COPY.p','N_1.p'),('COPY.a','B0_1.a'),('COPY.b','E_1.p'),('B0_1.p','N_2.p'),('OUT1.p','TRUE_1.p'),('OUT2.p','FALSE_1.p')):net.link(a,b)
net.audit();assert rooted(net) and typed(net)
left=net.wires['COPY.a'];right=net.wires['COPY.b']
net.replace(('COPY','N_1'),[('COPY.a','N_3.p'),('COPY.b','N_4.p')],[('N_3',('p',)),('N_4',('p',))])
net.audit();assert net.wires[left]=='N_3.p' and net.wires[right]=='N_4.p'
assert typed(net) and not rooted(net)
report={'passed':True,'counterexample':'before COPY--NIL: all components rooted; COPY.a--B0.a and B0.p--NIL forms rootless side branch while COPY.b--ERASE.p supplies component root. After COPY--NIL, B0--NIL--NIL disconnects without OUT/ERASE root.','finding':'Root coverage + typed principal/recursive tails is NOT closed under COPY--NIL on arbitrary typed forests; require each COPY auxiliary side branch to carry its own output/eraser root.','scope':'Constructed well-wired graph outside intended constructor reachability; disproves preservation of the proposed coarse invariant, not intended-net progress.'}
out=Path(__file__).resolve().parents[1]/'results/copy-nil-root-preservation-counterexample.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
