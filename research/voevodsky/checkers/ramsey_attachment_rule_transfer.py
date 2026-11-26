"""Freeze highest-sum zero-overlap selector. Exclude discovery core. For each remaining core, construct one regular triangle-free completion without overlap hints. Mark lexicographically first blue seven with 5 core + 2 neighbors, if present."""
import itertools,json,collections
from pysat.card import CardEnc
from pysat.formula import IDPool
from pysat.solvers import Solver
from ramsey_retention_slice import D
P=D.parent;R=json.loads((P/'ramsey_37_catalogue_free.json').read_text())['certificates'];orig=json.loads((P/'ramsey_fixed_core_chord.json').read_text())['core_index'];out=[]
for idx,z in enumerate(R):
 if idx==orig:continue
 a=z['core'];C=range(16);J=range(6);pool=IDPool();V={(i,j):pool.id((i,j)) for i in C for j in J};cs=[];rec=dict(core_index=idx);out.append(rec)
 for i in C:cs+=CardEnc.equals([V[i,j] for j in J],6-a[i].bit_count(),vpool=pool).clauses
 for j in J:
  cs+=CardEnc.equals([V[i,j] for i in C],5,vpool=pool).clauses;cs.extend([[-V[i,j],-V[h,j]] for i,h in itertools.combinations(C,2) if a[i]>>h&1])
 with Solver(name='g4',bootstrap_with=cs) as sl:
  if not sl.solve():rec['status']='no completion';continue
  pos=set(sl.get_model());sets=[{j for j in J if V[i,j] in pos} for i in C];sel={};
  for i,h in itertools.combinations(C,2):
   if a[i]>>h&1 or sets[i]&sets[h]:continue
   gate=pool.id();sel[gate]=len(sets[i])+len(sets[h]);
   for j in J:sl.add_clause([-gate,-V[i,j],-V[h,j]])
  mark=next(((t,tuple(sorted(js))[:2]) for t in itertools.combinations(C,5) if not any(a[i]>>h&1 for i,h in itertools.combinations(t,2)) and len(js:=set(J).difference(*(sets[i] for i in t)))>=2),None)
  if mark is None:rec['status']='no matching mark';continue
  es=list(itertools.product(*mark));rec.update(status='tested',mark=mark,red_supports=[sorted(s) for s in sets]);
  for name,gates in [('base',[]),('selected',[i for i,k in sel.items() if k==max(sel.values())]),('all',list(sel))]:
   rec[name]=[e for e in es if not sl.solve(assumptions=gates+[V[e]]+[-V[f] for f in es if f!=e])]
print(collections.Counter(r['status'] for r in out));print(collections.Counter((len(r['base']),len(r['selected']),len(r['all'])) for r in out if r['status']=='tested'));(P/'ramsey_attachment_rule_transfer.json').write_text(json.dumps(out)+'\n')
