"""Fractional joint-coverage screen. At d=7 each blue q-clique requires q distinct neighbor hits. Minimize total support mass; any verified dual value above 7 excludes seven whole supports. Use maximal supports; do not assume regularity."""
import json,itertools,collections
import numpy as np
from scipy.optimize import linprog
from ramsey_retention_slice import D
P=D.parent;rows=json.loads((P/'ramsey_38_window.json').read_text())['rows'];out=[]
for row in rows:
 m=int(row['core'],16);a=[0]*20
 for j in range(20):
  for i in range(j):
   if m>>(j*(j-1)//2+i)&1:a[i]|=1<<j;a[j]|=1<<i
 I=[0]
 for j,v in enumerate(a):I += [q|1<<j for q in I if not q&v]
 Q=I[1:];S=[s for s in Q if not any(t!=s and t&s==s for t in Q)];A=np.array([[int(bool(t&q)) for t in S] for q in Q]);d=np.array([q.bit_count() for q in Q]);rec=dict(core=row['core'],edges=row['edges']);out.append(rec)
 for name in ['16','5','56','123456']:
  ix=np.flatnonzero(np.isin(d,list(map(int,name))));B=A[ix,:];h=d[ix];lp=linprog(np.ones(len(S)),A_ub=-B,b_ub=-h);assert lp.success
  y=np.rint(np.maximum(-lp.ineqlin.marginals,0)*10**7).astype('int64');den=int(max(B.T@y));num=int(h@y);z=dict(excluded=num>7*den);rec[name]=z
  if z['excluded']:z.update(den=den,required=num,weights={Q[i]:int(w) for i,w in zip(ix,y) if w})
  else:
   from fractions import Fraction as F
   p=np.ceil(np.maximum(0,lp.x)*10**7).astype('int64');hs=B@p
   if p.sum()<=7*10**7 and np.all(hs>=10**7*h):
    z.update(fractional_verified=True,primal_den=10**7,primal={s:int(w) for s,w in zip(S,p) if w});continue
   x=[F(float(w)).limit_denominator(10**6) for w in lp.x];nz=[(j,w) for j,w in enumerate(x) if w];z['fractional_verified']=sum(x)<=7 and all(sum(w for j,w in nz if b[j])>=int(v) for b,v in zip(B,h))
print({name:dict(collections.Counter((r['edges'],r[name]['excluded']) for r in out)) for name in ['16','5','56','123456']});(P/'ramsey_38_joint_window.json').write_text(json.dumps(out)+'\n')
