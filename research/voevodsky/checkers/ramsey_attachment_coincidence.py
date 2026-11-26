"""Which endpoint coincidence readings actually force the example chord? Allow all other cross edges to change except the other marked pairs. Compare one saved switch with exact reoptimization."""
import json,itertools
from pysat.card import CardEnc
from pysat.formula import IDPool
from pysat.solvers import Solver
from ramsey_retention_slice import D
P=D.parent;z=json.loads((P/'ramsey_fixed_core_chord.json').read_text());a,b=z['before'],z['after'];C=range(16);J=range(16,22);q=set(z['marked']);edge=tuple(z['changed_chord']);pool=IDPool();v={(i,j):pool.id((i,j)) for i in C for j in J};base=[]
def eq(l,k):return CardEnc.equals(l,k,vpool=pool).clauses
for i in C:base+=eq([v[i,j] for j in J],sum(a[i]>>j&1 for j in J))
for j in J:
 base+=eq([v[i,j] for i in C],5);base.extend([[-v[i,j],-v[h,j]] for i,h in itertools.combinations(C,2) if a[i]>>h&1])
for i,j in v:
 if i in q and j in q:base.append([v[i,j] if (i,j)==edge else -v[i,j]])
reads=[];gates={}
for name,side,other in [('core',C,J),('neighbor',J,C)]:
 mask=sum(1<<i for i in other)
 for i,h in itertools.combinations(side,2):
  k=(a[i]&a[h]&mask).bit_count();l=(b[i]&b[h]&mask).bit_count();gate=pool.id();ands=[]
  for j in other:
   x,y=(v[i,j],v[h,j]) if name=='core' else (v[j,i],v[j,h]);t=pool.id();base.extend([[-t,x],[-t,y],[t,-x,-y]]);ands.append(t)
  base.extend([[-gate,*c] for c in eq(ands,k)]);gates[gate]=(name,i,h,k,l)
with Solver(name='g4',bootstrap_with=base) as sl:
 assert sl.solve();out={}
 for name in ('core','neighbor','both'):
  ids=[i for i,t in gates.items() if name=='both' or t[0]==name];ok=sl.solve(assumptions=ids);rec=dict(chord_red_possible=ok);out[name]=rec
  if not ok:
   sub=sl.get_core()
   for i in sub.copy():
    test=[j for j in sub if j!=i]
    if not sl.solve(assumptions=test):sub=test
   rec['irredundant']=[gates[j] for j in sub]
  else:rec['red_cross_edges']=[e for e,t in v.items() if t in set(sl.get_model())]
 single=[gates[t] for t in gates if not sl.solve(assumptions=[t])];out['single']=single
print({n:(x if n=='single' else (x['chord_red_possible'],x.get('irredundant'))) for n,x in out.items()});(P/'ramsey_attachment_coincidence.json').write_text(json.dumps(out,indent=1)+'\n')
