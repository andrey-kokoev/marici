"""Explain the tied maximum 17-cores: measure support-pair compatibility on blue fives, test smaller demands in descending size on whole quartets, and check the fractional five-demand packing bound."""
import itertools,json,collections,numpy as np
from scipy.optimize import linprog
from fractions import Fraction
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'results';rows=json.loads((P/'ramsey_frozen_gain_control.json').read_text())[1];out=[]
for r in rows:
 a=r['core'];I=[0]
 for i,v in enumerate(a):I.extend([s|1<<i for s in I if not s&v])
 S=[s for s in I if all(s&(v|1<<i) for i,v in enumerate(a))];Q={k:[q for q in I if q.bit_count()==k] for k in (3,4,5)};M={k:[sum(1<<j for j,q in enumerate(Q[k]) if not s&q) for s in S] for k in Q};G=[{j for j in range(i,len(S)) if not x&M[5][j]} for i,x in enumerate(M[5])];count=[0,0,0];hist=collections.Counter();examples={}
 for i,adj in enumerate(G):
  for j in adj:
   ij=adj&G[j]
   for k in ij:
    for l in ij&G[k]:
     z=(i,j,k,l);count[0]+=1
     bad=[q for q in Q[4] if sum(bool(S[v]&q) for v in z)<2];hist.update(bad)
     if bad:continue
     count[1]+=1
     if any(not q&(S[i]|S[j]|S[k]|S[l]) for q in Q[3]):continue
     count[2]+=1;examples.setdefault('quartet',[S[v] for v in z])
 B=np.array([[int(not s&q) for s in S] for q in Q[5]]);lp=linprog(-np.ones(len(S)),A_ub=B,b_ub=np.ones(len(B)));val=None if not lp.success else -lp.fun
 E=[(i,j) for i in range(17) for j in range(i) if not(a[i]>>j&1 or a[i]&a[j])];e_degrees=sorted(sum(i in p for p in E) for i in set(sum((list(p) for p in E),[])));out.append(dict(score=r['score'],red_edges=sum(v.bit_count() for v in a)//2,addable_degrees=e_degrees,fives=len(Q[5]),supports=len(S),compatible_pairs=sum(map(len,G)),fractional_fives=val,counts=count,universal_four=[q for q,n in hist.items() if n==count[0]],examples=examples));assert bool(count[-1])==(r['order']==22);print(out[-1]);
(P/'ramsey_gain_tie.json').write_text(json.dumps(out)+'\n')
