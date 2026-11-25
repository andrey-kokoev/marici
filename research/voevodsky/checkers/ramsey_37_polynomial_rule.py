"""Direct total-degree polynomial weight rule. Verify failure by an exact nonnegative combination of linear requirements annihilating every monomial (including at least one strict requirement)."""
import sys,json,gzip,math
from pathlib import Path
from collections import Counter
from fractions import Fraction as Q
import numpy as np
from scipy.optimize import linprog
root=Path(__file__).resolve().parents[2];p=root/'chatgpt/ramsey';sys.path.insert(0,str(p));from ramsey_r37_recursive_proof_verify import graph6,independent_fives
R=[];ids=[];out=[]
for rec,line in enumerate(gzip.open(p/'r36_16.g6.gz','rb'),1):
 A=graph6(line)
 if sum(n.bit_count() for n in A)!=66:continue
 F=independent_fives(A);D=[[j for j,b in enumerate(F) if not a&b] for a in F];k=[(len(d),sum(len(D[j]) for j in d)) for d in D];counts=Counter(k);seen=set()
 for t,d in zip(F,D):
  c=Counter(k[j] for j in d);row=tuple((key,6*c[key]-v) for key,v in sorted(counts.items()));
  if row not in seen:seen.add(row);R.append(dict(row));ids.append([rec,t])
K=sorted(set.union(*(set(r) for r in R)));n=len(R);R += [{k:1} for k in K];names=ids+[['nonnegative',k] for k in K]
for deg in [1,2,3,4]:
 powers=[(a,h-a) for h in range(deg+1) for a in range(h+1)];V=[[sum(v*(d-15)**a*(s-200)**b for (d,s),v in r.items()) for a,b in powers] for r in R];mat=V+[];N=len(V);eq=np.array(V,dtype=float).T;eq/=np.max(abs(eq),axis=1)[:,None];eq=np.vstack([eq,[1]*n+[0]*(N-n)]);res=linprog(np.ones(N),A_eq=eq,b_eq=[0]*len(powers)+[1],bounds=(0,None));assert res.success,res.message;use=np.where(res.x>1e-10)[0].tolist();tab=[[Q(V[i][j]) for i in use]+[Q(0)] for j in range(len(powers))]+[[Q(i<n) for i in use]+[Q(1)]]
 for j in range(len(use)):
  h=next(h for h in range(j,len(tab)) if tab[h][j]);tab[j],tab[h]=tab[h],tab[j];u=tab[j]=[v/tab[j][j] for v in tab[j]]
  for h,v in enumerate(tab):
   if h!=j and v[j]:tab[h]=[x-v[j]*y for x,y in zip(v,u)]
 w=[tab[i][-1] for i in range(len(use))];assert min(w)>0 and any(i<n for i in use) and all(sum(v*V[i][j] for i,v in zip(use,w))==0 for j in range(len(powers)));out.append(dict(degree=deg,terms=len(powers),certificate=[(names[i],str(v)) for i,v in zip(use,w)]));print(deg,len(use),len(set(names[i][0] for i in use if i<n)))
(root/'voevodsky/results/ramsey_37_polynomial_rule.json').write_text(json.dumps(out,indent=2)+'\n')
