"""Joint free-row and red-core edit search on the exact-six winner. No edit budget. Every original blue clique can be covered either by edits inside it or hits from rows, with the number of newcomer misses enforced exactly. Enumerate anchor subsets as requested by CLI; budgeted solver reports unknown explicitly."""
import json,itertools,collections,sys
from pysat.solvers import Solver
from ramsey_retention_slice import D,check
P=D.parent;r=next(x for x in json.loads((P/'ramsey_gain26_edge_descend.json').read_text())['passing'] if x['rows']);a=r['adj'];S=r['rows'];d=7;n=26;F=(1<<n)-1;I=[0]
for i,v in enumerate(a):I.extend([q|1<<i for q in I if not q&v]);
E=[(i,j) for i in range(n) for j in range(i) if not a[i]>>j&1 and not a[i]&a[j]];es={e:1+k for k,e in enumerate(E)};V=lambda h,i:1+len(E)+h*n+i;base=[]
for t in itertools.combinations(range(n),3):
 lits=[]
 for j,i in itertools.combinations(t,2):
  if a[i]>>j&1:continue
  if (i,j) not in es:break
  lits.append(-es[i,j])
 else:base.append(lits)
for i in range(n):
 for j in range(i):
  z=es.get((i,j));
  if z or a[i]>>j&1:
   for h in range(d):base.append(([-z] if z else [])+[-V(h,i),-V(h,j)])
# Build full panel model once. Encode a hit flag for q,h in just the direction needed: true implies at least one red neighbor in q.
last=V(d-1,n-1);qs=sorted((q for q in I if q.bit_count()>=2),key=int.bit_count,reverse=True)
for q in qs:
 k=q.bit_count();need=9-k;esc=[v for (i,j),v in es.items() if q>>i&1 and q>>j&1];b=[i for i in range(n) if q>>i&1];hits=[]
 for h in range(d):
  last+=1;hits.append(last);base.append([-last]+[V(h,i) for i in b])
 for sub in itertools.combinations(hits,need):base.append(esc+list(sub))
out=[];lo=int(sys.argv[1]);hi=int(sys.argv[2]);budget=int(sys.argv[3]);path=P/f'ramsey_gain26_joint_repair7_{lo}_{hi}.json'
with Solver(name='cadical195',bootstrap_with=base) as sl:
 for size in range(hi,lo-1,-1):
  for ix in itertools.combinations(range(6),size):
   ass=[V(h,i)*(1 if S[j]>>i&1 else -1) for h,j in enumerate(ix) for i in range(n)];sl.conf_budget(budget);ok=sl.solve_limited(assumptions=ass);z=dict(ix=ix,ok=ok)
   if ok:
    m=set(sl.get_model());b=a[:];ed=[(i,j) for (i,j),v in es.items() if v in m];w=[sum(1<<i for i in range(n) if V(h,i) in m) for h in range(d)]
    for i,j in ed:b[i]|=1<<j;b[j]|=1<<i
    g=b+[0]*8
    for h,s in enumerate(w,n):
     g[h]=s|1<<33;g[-1]|=1<<h
     for i in range(n):g[i]|=(s>>i&1)<<h
    assert check(g,(1<<34)-1,3,9);z.update(edges=ed,rows=w)
   out.append(z);path.write_text(json.dumps(dict(candidate_edges=E,runs=out))+'\n')
  print(size,collections.Counter(x['ok'] for x in out if len(x['ix'])==size),flush=True)
