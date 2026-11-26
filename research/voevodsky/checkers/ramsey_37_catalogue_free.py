"""Generate all relevant cores from the empty graph, without reading Ramsey catalogues. Cover all minimum-degree root choices; verify 6h>m on every resulting isomorphism type. Finite exhaustion, not a symbolic universal inequality."""
import itertools,json,collections
from pathlib import Path
import igraph as ig
import numpy as np
P=Path(__file__).resolve().parents[1]/'results'
def key(a):
 G=ig.Graph(len(a),[(i,j) for i,j in itertools.combinations(range(len(a)),2) if a[i]>>j&1]);return tuple(sorted(tuple(sorted(e)) for e in G.permute_vertices(G.canonical_permutation()).get_edgelist()))
def alpha(a):
 v=[0]*(1<<len(a))
 for m in range(1,len(v)):
  b=m&-m;v[m]=max(v[m^b],1+v[(m^b)&~a[b.bit_length()-1]])
 return v
def independent(a):
 p=(1<<len(a))-1;ss=[0]
 for i,g in enumerate(a):ss += [s|(1<<i) for s in ss if not s&g]
 return ss
layer=[[]];core={};counts=[];classes={};rootcounts=collections.Counter()
for n in range(1,15):
 nxt={}
 for a in layer:
  p=(1<<(n-1))-1;A=alpha(a)
  for s in independent(a):
   if A[p^s]>=4:continue
   h=[v|((s>>i&1)<<(n-1)) for i,v in enumerate(a)]+[s];nxt.setdefault(key(h),h)
 layer=list(nxt.values());counts.append(len(layer));
 if n>=11:core[n]=layer
assert not core[14]
for n in (11,12,13):
 d=15-n
 for a in core[n]:
  need=33-d-sum(v.bit_count() for v in a)//2;S=sorted((s for s in independent(a) if d-1<=s.bit_count()<=4),key=int.bit_count);p=(1<<n)-1;A=alpha(a)
  def rec(chosen,j,left,remaining,states):
   if left==0:
    if remaining:return
    b=[v for v in a]+[0]*(d+1)
    for u,s in enumerate(chosen,n):
     b[u]=s|(1<<15);b[15]|=1<<u
     for i in range(n):
      if s>>i&1:b[i]|=1<<u
    if min(v.bit_count() for v in b)!=d:return
    rootcounts[d]+=1;classes.setdefault(key(b),b);return
   for k in range(j,len(S)):
    s=S[k];w=s.bit_count()
    if w*left>remaining:break
    if w+4*(left-1)<remaining:continue
    new=[(m&~s,l+1) for m,l in states];
    if any(A[m]+l>=6 for m,l in new):continue
    rec(chosen+[s],k,left-1,remaining-w,states+new)
  rec([],0,d,need,[(p,0)])
 print(n,len(classes),flush=True)
cert=[]
for a in classes.values():
 S=[s for s in independent(a) if s.bit_count()==5];D=np.array([[int(not(t&s)) for s in S] for t in S]);hits=np.zeros(len(S),dtype=int);w=hits.copy()
 for m in range(1,10001):
  j=int((D@np.exp(-0.1*(hits-hits.min()))).argmax());w[j]+=1;hits+=D[:,j]
  if 6*min(hits)>m:break
 assert min(D@w)*6>sum(w);cert.append(dict(core=a,weights={s:int(v) for s,v in zip(S,w) if v},hits=int(min(hits))))
print('layers',counts,'classes',len(cert),'root representations',rootcounts,flush=True);(P/'ramsey_37_catalogue_free.json').write_text(json.dumps(dict(layer_counts=counts,rootcounts=dict(rootcounts),certificates=cert))+'\n')
