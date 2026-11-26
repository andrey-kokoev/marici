"""Select symmetric zero overlaps before querying any chord. Drop red-adjacent core pairs: their overlap is zero by triangle avoidance. Query every marked cross-edge in turn with all other marked pairs fixed. Also test without any marked cross-edge observations."""
import json,itertools,collections
from pysat.card import CardEnc
from pysat.formula import IDPool
from pysat.solvers import Solver
from ramsey_retention_slice import D
P=D.parent;z=json.loads((P/'ramsey_fixed_core_chord.json').read_text());a=z['before'];C=range(16);J=range(16,22);M=z['marked'];mask=sum(1<<j for j in J);pool=IDPool();V={(i,j):pool.id((i,j)) for i in C for j in J};E=[e for e in V if set(e)<=set(M)];cs=[]
def eq(ids,k):return CardEnc.equals(ids,k,vpool=pool).clauses
for i in C:cs+=eq([V[i,j] for j in J],(mask&a[i]).bit_count())
for j in J:cs+=eq([V[i,j] for i in C],5)
selected={}
for i,h in itertools.combinations(C,2):
 red=a[i]>>h&1;zero=not(a[i]&a[h]&mask)
 if red:assert zero
 if not zero:continue
 gate=[] if red else [-pool.id()]
 if gate:selected[i,h]=-gate[0]
 for j in J:cs.append(gate+[-V[i,j],-V[h,j]])
# A second structural filter: select only zero-overlap pairs with maximum possible degree-sum among the selected pairs, not based on a query edge.
weight=lambda p:sum((a[i]&mask).bit_count() for i in p);top=max(map(weight,selected));policies={'none':[],'highest_sum':[v for p,v in selected.items() if weight(p)==top],'all_zero':list(selected.values())};out={};
with Solver(name='g4',bootstrap_with=cs) as s:
 for context in ['none','other_marked']:
  out[context]={}
  for policy,gates in policies.items():
   forced=[]
   for e in (V if context=='none' else E):
    obs=[-V[f] for f in E if f!=e] if context=='other_marked' else [];assert all(not(a[i]>>j&1) for i,j in E);i,j=e;opp=-V[e] if a[i]>>j&1 else V[e]
    if not s.solve(assumptions=gates+obs+[opp]):forced.append(e)
   out[context][policy]=forced
print('gates',[(k,len(v)) for k,v in policies.items()]);print(out);(P/'ramsey_attachment_blind_rule.json').write_text(json.dumps(dict(selected=[[i,h,v,weight((i,h))] for (i,h),v in selected.items()],tested_marked=E,forced=out),indent=1)+'\n')
