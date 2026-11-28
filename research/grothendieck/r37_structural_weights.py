"""Three table-only weight generators. Disjointness is used only to score them."""
from fractions import Fraction as F
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
D=Path(__file__).resolve().parents[1]/'voevodsky/results';cores=json.loads((D/'ramsey_37_catalogue_free.json').read_text())['certificates']
def weights(R):
    moves={r:{3<<i for i in range(15) if (r>>i)&3 in (1,2) and r^(3<<i) in R} for r in R};comp={}
    for r in R:
        if r in comp:continue
        seen={r};stack=[r]
        while stack:
            v=stack.pop()
            for m in moves[v]:
                t=v^m
                if t not in seen:seen.add(t);stack.append(t)
        comp.update(dict.fromkeys(seen,F(1,len(seen))))
    faces={r:[r^(1<<i) for i in range(16) if r>>i&1] for r in R};n=Counter(t for L in faces.values() for t in L)
    return comp,{r:sum(F(1,n[t]) for t in L) for r,L in faces.items()},{r:1+sum(not m&h and r^m^h in R for m,h in combinations(L,2)) for r,L in moves.items()}
if __name__=='__main__':
    passes=Counter()
    for idx,rec in enumerate(cores):
        a=rec['core'];R={sum(1<<i for i in t) for t in combinations(range(16),5) if all(not a[i]>>j&1 for i,j in combinations(t,2))}
        for j,w in enumerate(weights(R)):
            m,s=min((sum(w[t] for t in R if not t&r),r) for r in R);W=sum(w.values());passes[j]+=6*m>W
            if idx==0:print(j,s,6*m,W,'margin',6*m-W)
    print('passes',passes,'cores',len(cores))
