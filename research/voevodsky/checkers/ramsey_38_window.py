"""Use published minima (60,51,44) from the order-27 small-core audit. Test every in-window core in the stored two-deletion slice, not a complete census of 20-cores. Replay LP sign with exact integer products."""
import gzip,json,collections,numpy as np
from scipy.optimize import linprog
from ramsey_retention_slice import D,CAT,check
P=D.parent;profiles=[]
for a in range(29):
 for b in range(29-a):
  c=28-a-b
  if (a+c)%2 or not c:continue
  u=(45*a+48*b+49*c-60*a-51*b)//c
  if u>=45:profiles.append([a,b,c,u]);
assert max(p[-1] for p in profiles)==49 and [p[:3] for p in profiles if p[-1]==49]==[[0,0,28]]
with gzip.open(CAT.parent/'ramsey_border_37_22_to_20.tsv.gz','rt') as f:
 next(f);keys={int(s[1],16) for line in f if (s:=line.split())[0]=='20'}
out=[]
for m in sorted(k for k in keys if k.bit_count()<=49):
 a=[0]*20
 for j in range(20):
  for i in range(j):
   if m>>(j*(j-1)//2+i)&1:a[i]|=1<<j;a[j]|=1<<i
 assert check(a,2**20-1,3,7);I=[0]
 for i,v in enumerate(a):I += [q|1<<i for q in I if not q&v]
 S=[q for q in I if not any(q!=t and t&q==q for t in I)];Q=[q for q in I if q.bit_count()==6];B=np.array([[int(not t&q) for t in S] for q in Q]);lp=linprog(-np.ones(len(S)),A_ub=B,b_ub=np.ones(len(Q)));r=dict(core=hex(m),edges=m.bit_count());out.append(r)
 if lp.success:
  y=np.ceil(np.maximum(0,-lp.ineqlin.marginals)*10**7).astype('int64');h=int(min(B.T@y));r['excluded']=bool(h and y.sum()<7*h)
  if r['excluded']:r.update(weights={q:int(v) for q,v in zip(Q,y) if v},den=h)
  else:
   x=np.rint(lp.x*10**6).astype('int64');den=int(max(B@x));r['fractional_pass_verified']=bool(den and x.sum()>=7*den)
 else:
  assert lp.status==3;z=next(s for j,s in enumerate(S) if not B[:,j].any());assert all(z&q for q in Q);r.update(excluded=False,unbounded=True,universal_support=z)
print(collections.Counter((r['edges'],r['excluded']) for r in out));(P/'ramsey_38_window.json').write_text(json.dumps(dict(profiles=profiles,rows=out))+'\n')
