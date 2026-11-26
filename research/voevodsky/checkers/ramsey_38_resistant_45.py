"""Search for deletion-minimal 45-edge cores by exchanging an edge on the known layer. Exact legality tests and explicit blue-five witnesses for every red edge of any returned core. Discovery is not a census."""
import itertools,json,random
from ramsey_retention_slice import D,check,has
P=D.parent;src=json.loads((P/'ramsey_38_window_new_types.json').read_text());rng=random.Random(4517);rng.shuffle(src);E=[(i,j) for j in range(20) for i in range(j)];F=(1<<20)-1

def red(a,i,j):return (a[i]>>j)&1
def flip(a,i,j):a[i]^=1<<j;a[j]^=1<<i
def witness(a,i,j):
 p=F&~(a[i]|a[j]|1<<i|1<<j)
 return has([~v for v in a],p,5)
def find():
 tested=0
 for row in src:
  a=[0]*20;m=int(row['core'],16)
  for k,e in enumerate(E):
   if m>>k&1:flip(a,*e)
  # Delete first, then add any admissible replacement, including moves not factorable through a legal 46-edge core.
  for i,j in E:
   if not red(a,i,j):continue
   flip(a,i,j);p=F&~(a[i]|a[j]|1<<i|1<<j);q5=[set(t) for t in itertools.combinations([v for v in range(20) if p>>v&1],5) if all(not red(a,h,k) for h,k in itertools.combinations(t,2))];
   for h,k in E:
    if (h,k)==(i,j) or red(a,h,k) or a[h]&a[k] or not all({h,k}<=(t|{i,j}) for t in q5):continue
    flip(a,h,k);tested+=1
    if all(witness(a,u,v) for u,v in E if red(a,u,v)):
     assert check(a,F,3,7);cert={}
     for u,v in E:
      if red(a,u,v):cert[f'{u},{v}']=next(t for t in itertools.combinations(range(20),5) if u not in t and v not in t and all(not red(a,s,z) for s,z in itertools.combinations((*t,u,v),2) if {s,z}!={u,v}))
     return dict(core=a,start=row['core'],removed=[i,j],added=[h,k],tested=tested,cert=cert)
    flip(a,h,k)
   flip(a,i,j)
 return dict(tested=tested)
if __name__=='__main__':
 out=find()
 if 'core' in out:
  from scipy.optimize import linprog
  import numpy as np
  a=out['core'];I=[0]
  for j,v in enumerate(a):I.extend([q|1<<j for q in I if not q&v])
  S=[s for s in I if not any(t!=s and t&s==s for t in I)];Q=[q for q in I if q.bit_count() in (5,6)];d=np.array([q.bit_count() for q in Q]);A=np.array([[int(bool(q&s)) for s in S] for q in Q]);lp=linprog(np.ones(len(S)),A_ub=-A,b_ub=-d);assert lp.success;y=np.rint(-lp.ineqlin.marginals*10**7).astype('int64');den=int(max(A.T@y));num=int(d@y);assert min(y)>=0 and num>7*den;out.update(num=num,den=den,weights={q:int(v) for q,v in zip(Q,y) if v});print('required',num,'available',7*den,'ratio',num/den)
 print({k:v for k,v in out.items() if k not in ('cert','weights')},flush=True);(P/'ramsey_38_resistant_45.json').write_text(json.dumps(out)+'\n')
