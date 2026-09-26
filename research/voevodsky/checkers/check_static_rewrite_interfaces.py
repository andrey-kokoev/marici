"""Audit literal production replace templates without importing/running the engine."""
import ast
from collections import Counter
from pathlib import Path
import json
source=Path(__file__).with_name('check_copy_two_queries_interleavings.py')
tree=ast.parse(source.read_text())
calls=sorted((n for n in ast.walk(tree) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=='replace'),key=lambda n:n.lineno)
# Source-order branch manifest, checked against the current production branches.
specs=[('COPY--N',('a','b'),(),1),('COPY--B',('a','b'),('a',),2),('E--N',(),(),1),('E--B/K',(),('a',),3),('Q_B--N',('a','r'),(),1),('Q_B--K',('a','r'),('a',),1),('Q_S--N',('a','r'),(),1),('Q_S--B',('a','r'),('a',),2),('Q_R--N',('r',),(),1),('Q_R--B',('r',),('a',),2)]
env=dict(name='A',other='B',l='L',r='R',nxt='X',out='O',erase='E')
def literal(n):
 if isinstance(n,ast.Constant):return n.value
 if isinstance(n,ast.Name):return env[n.id]
 if isinstance(n,(ast.Tuple,ast.List)):return [literal(x) for x in n.elts]
 if isinstance(n,ast.BinOp) and isinstance(n.op,ast.Add):return literal(n.left)+literal(n.right)
 raise AssertionError(ast.dump(n))
assert len(calls)==len(specs)
rows=[]
for call,(rule,ap,bp,multiplicity) in zip(calls,specs):
 removed,edges,created=map(literal,call.args)
 assert removed==['A','B']
 boundary={'A.'+p for p in ap}|{'B.'+p for p in bp}
 new_names=[n for n,ports in created]
 assert len(new_names)==len(set(new_names)) and not set(new_names)&{'A','B'}
 new_ports=[n+'.'+p for n,ports in created for p in ports]
 assert len(new_ports)==len(set(new_ports))
 used=Counter(p for edge in edges for p in edge)
 assert used==Counter(boundary|set(new_ports)),(rule,used)
 assert all(not (a in boundary and b in boundary) for a,b in edges)
 rows.append({'rule_family':rule,'typed_cases':multiplicity,'boundary_ports':len(boundary),'new_ports':len(new_ports),'source_line':call.lineno})
report={'passed':True,'templates':len(rows),'typed_cases':sum(r['typed_cases'] for r in rows),'rows':rows,'scope':'AST audit of actual replace arguments with a manually reviewed branch manifest. Exactly-once interfaces and distinct symbolic new slots; allocator freshness and manifest completeness remain separate assumptions.'}
assert report['typed_cases']==15
out=source.parents[1]/'results/static-rewrite-interfaces.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
