"""Keep the marked (3,6) 16-core and root star literal in two 6-regular triangle-free completions. Search legal switches in cross edges only. Certify that a blue seven loses exactly one chord. Not (3,7)-avoiding endpoints."""
import json,itertools
from pysat.solvers import Solver
from pysat.formula import IDPool
from pysat.card import CardEnc
from ramsey_retention_slice import D,check,has
P=D.parent;rows=json.loads((P/'ramsey_37_catalogue_free.json').read_text())['certificates'];N=2**23-1
for idx,z in enumerate(rows):
 c=z['core'];assert check(c,65535,3,6);pool=IDPool();x={(i,j):pool.id((i,j)) for i in range(16) for j in range(16,22)};cs=[]
 for i in range(16):cs+=CardEnc.equals([x[i,j] for j in range(16,22)],6-c[i].bit_count(),vpool=pool).clauses
 for j in range(16,22):
  cs+=CardEnc.equals([x[i,j] for i in range(16)],5,vpool=pool).clauses
  cs += [[-x[i,j],-x[h,j]] for i,h in itertools.combinations(range(16),2) if c[i]>>h&1]
 with Solver(name='g4',bootstrap_with=cs) as s:
  if not s.solve():continue
  m=set(s.get_model());a=c.copy()+[1<<22]*6+[63<<16]
  for (i,j),v in x.items():
   if v in m:a[i]|=1<<j;a[j]|=1<<i
 for i,h in itertools.combinations(range(16),2):
  for j,k in itertools.permutations(range(16,22),2):
   if not(a[i]>>j&1 and a[h]>>k&1) or a[i]>>k&1 or a[h]>>j&1:continue
   b=a.copy();edges=[(i,j),(h,k),(i,k),(h,j)]
   for u,v in edges:b[u]^=1<<v;b[v]^=1<<u
   if has(b,N,3):continue
   # i,k must join the seven; omit h,j to leave exactly one modified internal edge.
   common=[v for v in range(23) if v not in (i,j,h,k) and not((a[i]|a[k])>>v&1)]
   for t in itertools.combinations(common,5):
    if any(a[v]>>w&1 for v,w in itertools.combinations(t,2)):continue
    for g in (a,b):assert all(v.bit_count()==6 for v in g) and not has(g,N,3) and [v&65535 for v in g[:16]]==c and g[22]==63<<16
    out=dict(core_index=idx,fixed_root=22,header=t[0],marked=[i,k,*t],changed_chord=[i,k],red_removed=edges[:2],red_added=edges[2:],before=a,after=b);print({x:v for x,v in out.items() if x not in ('before','after')});(P/'ramsey_fixed_core_chord.json').write_text(json.dumps(out,indent=1)+'\n');quit()
raise ValueError('no example')
