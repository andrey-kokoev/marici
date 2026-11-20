"""Two verdicts at a new role. Swap thresholds, colors AND proposed neighborhood. Standard library."""
from itertools import combinations,product
from collections import Counter
from pathlib import Path
import json

def audit(n,E,l,k):
    V=set(range(n));pairs=set(combinations(range(n),2));B=pairs-E
    def cl(S,e,r):return any(set(combinations(t,2))<=e for t in combinations(sorted(S),r))
    assert not cl(V,E,l) and not cl(V,B,k)
    def signs(S,E,B,l,k):return ('-' if cl(S,E,l-1) else '+')+('-' if cl(V-S,B,k-1) else '+')
    h=Counter();dual=Counter();first={}
    for m in range(1<<n):
        S={i for i in V if m>>i&1};s=signs(S,E,B,l,k);rev=signs(V-S,B,E,k,l);assert rev==s[::-1];h[s]+=1;dual[rev]+=1;first.setdefault(s,sorted(S))
    return dict(pair=[l,k],old_roles=n,red_edges=sorted(E),counts=h,exchanged_counts=dual,examples_red_neighbors=first)
if __name__=='__main__':
    signs=list(product((1,-1),repeat=2));rows=[[1,p,c,p*c] for p,c in signs];assert [[sum(r[i]*r[j] for r in rows) for j in range(4)] for i in range(4)]==[[4*int(i==j) for j in range(4)] for i in range(4)]
    swap=lambda s:s[::-1];flip=lambda s:tuple(-x for x in s);agree=lambda s:s[0]*s[1];assert all(swap(swap(s))==flip(flip(s))==s and flip(swap(s))==swap(flip(s)) and agree(s)==agree(swap(s))==agree(flip(s)) for s in signs)
    # For simultaneous failure we need disjoint old witnesses of sizes l-1 and k-1.
    # Balanced double star attains the resulting lower bound at (3,7).
    out=[audit(4,{(0,1),(1,2),(2,3)},3,3),audit(8,{(0,1),*((0,i) for i in (2,3,4)),*((1,i) for i in (5,6,7))},3,7)]
    print(json.dumps(out));(Path(__file__).resolve().parents[1]/'results/ramsey_reciprocal_verdicts.json').write_text(json.dumps(out,indent=2)+'\n')
