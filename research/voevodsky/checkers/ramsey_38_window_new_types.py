"""Exact one-edge augmentation of all recorded minimum 44-edge cores; no completeness claim for 45-edge cores with no such spanning subgraph. Test frozen joint (5,6) cover with rational dual verification."""
import itertools,json,collections,igraph as ig,numpy as np
from scipy.optimize import linprog
from ramsey_retention_slice import D,CAT,check
P=D.parent;n=20;E=[(i,j) for j in range(n) for i in range(j)];parents=[int(s,16) for s in (CAT.parent/'ramsey_37_20_44_cores.txt').read_text().split()];types={};inc=0
for parent in parents:
 a=[0]*n
 for k,(i,j) in enumerate(E):
  if parent>>k&1:a[i]|=1<<j;a[j]|=1<<i
 for k,(i,j) in enumerate(E):
  if parent>>k&1 or a[i]&a[j]:continue
  m=parent|1<<k;G=ig.Graph(n,[e for h,e in enumerate(E) if m>>h&1]);key=tuple(sorted(tuple(sorted(e)) for e in G.permute_vertices(G.canonical_permutation()).get_edgelist()));types.setdefault(key,dict(core=hex(m),parents=set()))['parents'].add(hex(parent));inc+=1
import sys
path=P/'ramsey_38_window_new_types.json'
if '--degree3' in sys.argv or '--degree4' in sys.argv:
 d=3 if '--degree3' in sys.argv else 4;types={};inc=0;path=P/f'ramsey_38_degree{d}_weights.json'
 for a in json.loads((P/('ramsey_38_degree3_inventory_32_36.json' if d==3 else 'ramsey_38_degree4_inventory.json')).read_text())['resistant']:
  m=sum(1<<k for k,(i,j) in enumerate(E) if a[i]>>j&1);types[m]=dict(core=hex(m),parents=[])
out=json.loads(path.read_text()) if path.exists() else [];done={r['core'] for r in out};print('inventory',inc,len(types),'already tested',len(done),flush=True)
for r in types.values():
 if r['core'] in done:continue
 m=int(r['core'],16);a=[0]*n
 for k,(i,j) in enumerate(E):
  if m>>k&1:a[i]|=1<<j;a[j]|=1<<i
 assert check(a,2**n-1,3,7);I=[0]
 for i,v in enumerate(a):I += [s|1<<i for s in I if not s&v]
 S=[s for s in I if not any(s!=t and s&t==s for t in I)];Q=[q for q in I if q.bit_count() in (5,6)];A=np.array([[int(bool(q&s)) for s in S] for q in Q]);d=np.array([q.bit_count() for q in Q]);res=linprog(np.ones(len(S)),A_ub=-A,b_ub=-d);assert res.success;y=np.rint(-res.ineqlin.marginals*1e7).astype('int64');assert min(y)>=0;den=int(max(A.T@y));num=int(d@y);out.append(dict(core=r['core'],parents=sorted(r['parents']),excluded=num>7*den,den=den,num=num,weights={q:int(v) for q,v in zip(Q,y) if v}));
 if len(out)%10==0:path.write_text(json.dumps(out)+'\n')
print('parents',len(parents),'moves',inc,'distinct',len(out),'exclude',sum(r['excluded'] for r in out),'range',min(r['num']/r['den'] for r in out),max(r['num']/r['den'] for r in out));path.write_text(json.dumps(out)+'\n')
