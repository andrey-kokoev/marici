"""A linear forest with one query can still be stuck without typed-tail grammar."""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json
with redirect_stdout(StringIO()):
 from check_full_unary_query_port_graph import Net
net=Net.__new__(Net);net.types={};net.wires={};net.serial=0;net.steps=0
for name,ports in (('OUT',('p',)),('Q_B',('p','a','r')),('TRUE',('p',)),('N',('p',))):net.add(name,ports)
net.link('Q_B.p','TRUE.p');net.link('Q_B.a','N.p');net.link('Q_B.r','OUT.p')
net.audit()
assert len(net.types)==4 and len(net.wires)//2==3 # connected tree
assert net.wires['Q_B.p'].split('.')[0]=='TRUE'
assert not net.wires['Q_B.p'].split('.')[0].startswith(('K_','N_'))
report={'passed':True,'malformed_graph':'connected linear tree, one Q_B, correct port degree but Q_B principal meets TRUE principal','no_query_rule':'Q_B requires K or NIL; this graph is stuck with no valid query active-pair rule','finding':'forest+linearity+one-Q invariant is insufficient; require typed query-tail reachability and output-rooted component grammar','scope':'Adversarial well-wired graph not reachable from intended constructor; demonstrates why stronger invariant is necessary.'}
out=Path(__file__).resolve().parents[1]/'results/forest-invariant-insufficiency.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
