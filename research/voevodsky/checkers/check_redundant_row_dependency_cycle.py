"""Equal row packets can encode non-well-founded derivation references."""
from pathlib import Path
import json
rows={'x-high':((1,0),1),'y-high':((0,1),1),'z':((1,1),2),'w':((1,1),2)}
def packet(name,deps):
 normal=tuple(sum(rows[d][0][j]*weight for d,weight in deps) for j in (0,1))
 bound=sum(rows[d][1]*weight for d,weight in deps)
 assert (normal,bound)==rows[name]
packet('z',(('w',1),));packet('w',(('z',1),))
packet('z',(('x-high',1),('y-high',1)))
def validate(dependencies):
 visiting=set();done=set()
 def visit(node):
  if node in visiting:raise ValueError('DERIVATION_CYCLE')
  if node in done:return
  visiting.add(node)
  for dep in dependencies.get(node,()):visit(dep)
  visiting.remove(node);done.add(node)
 for node in dependencies:visit(node)
 return done
cycle={'z':('w',),'w':('z',)}
try:validate(cycle)
except ValueError as err:assert str(err)=='DERIVATION_CYCLE'
else:raise AssertionError('cyclic replay admitted')
rooted={'z':('x-high','y-high'),'w':('z',)}
assert validate(rooted)=={'x-high','y-high','z','w'}
# An algebraic packet is not an anchored derivation: each cyclic edge is
# individually sound, yet recursive expansion has no primitive-root base.
report={'passed':True,'cyclic_individual_row_equations_sound':True,'mutually_referential_replay':'DERIVATION_CYCLE','rooted_alternative':'z from old upper rows; w from z','rooted_alternative_acyclic':True,'scope':'Frozen square row derivation references, not proof that z/w are false inequalities, not source issuer authentication, and not analytic S,A,R,C,G roles.'}
out=Path(__file__).resolve().parents[1]/'results/redundant-row-dependency-cycle.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
