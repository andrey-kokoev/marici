"""Exhaust four-neighbor support multisets. Find an irredundant obstruction; verify a rational fractional cover of all demands."""
import itertools,json,random,math
from pathlib import Path
from fractions import Fraction
import numpy as np
from scipy.optimize import linprog
P=Path(__file__).resolve().parents[1]/'results';a=next(z['core'] for z in json.loads((P/'ramsey_core_capacity_36.json').read_text()) if 'deletion' in z['sources']);I=[t for t in range(1<<len(a)) if all(not (a[i]&t) for i in range(len(a)) if t>>i&1)];S=[t for t in I if all(t==u or t&u!=t for u in I)];Q=[t for t in I if t.bit_count()>=2];M=np.array(list(itertools.combinations_with_replacement(range(len(S)),4)));allm=(1<<len(M))-1;fail=[]
for t in Q:
 n=np.array([int(bool(u&t)) for u in S])[M].sum(axis=1);fail.append(int.from_bytes(np.packbits(n<t.bit_count()-1,bitorder='little').tobytes(),'little'))
def union(ids):
 v=0
 for i in ids:v|=fail[i]
 return v
rng=random.Random(10);best=list(range(len(Q)));by={}
for sizes in [(2,),(3,),(4,),(2,3),(2,4),(3,4),(2,3,4)]:
 idx=[i for i,t in enumerate(Q) if t.bit_count() in sizes];by[str(sizes)]=len(M)-union(idx).bit_count()
 if union(idx)!=allm:continue
 for rep in range(25):
  covered=0;ids=[];rng.shuffle(idx)
  while covered!=allm:
   i=max(idx,key=lambda i:(fail[i]&~covered).bit_count());covered|=fail[i];ids.append(i)
  for i in ids.copy():
   if union(j for j in ids if i!=j)==allm:ids.remove(i)
  if len(ids)<len(best):best=ids
assert union(best)==allm;w=[]
for i in best:
 v=allm^union(j for j in best if j!=i);assert v;w.append([S[j] for j in M[(v&-v).bit_length()-1]])
A=[[int(bool(t&u)) for u in S] for t in Q];lp=linprog([1]*len(S),A_ub=-np.array(A),b_ub=[1-t.bit_count() for t in Q]);p=[Fraction(float(v)).limit_denominator(10000) for v in lp.x];assert sum(p)==4 and all(sum(v*b for v,b in zip(p,row))>=t.bit_count()-1 for row,t in zip(A,Q));print('supports',len(S),'multisets',len(M),'survivors',by,'core',[(Q[i],Q[i].bit_count()) for i in best]);(P/'ramsey_capacity_obstruction.json').write_text(json.dumps(dict(core=a,supports=S,multisets=len(M),survivors=by,demands=[Q[i] for i in best],omission_witnesses=w,fractional={u:str(v) for u,v in zip(S,p) if v}),indent=1)+'\n')
