"""Refine 52 uncertified flips. Given each maximal fresh attachment S, use labelled upper marginals up to order three. Bound the one missing fourfold marginal by nonnegative exact-incidence bins and by the size of the triangle-free two-color residual pocket. Verify against withheld costs."""
from pathlib import Path
from itertools import combinations
from collections import defaultdict,Counter
import json
H=Path(__file__).resolve().parents[1];D=H/'results';load=lambda f:json.loads((D/(f+'.json')).read_text());cat=(H.parent/'chatgpt/ramsey/pauli-realization-catalogues/r37_22.g6').read_text().splitlines();reference={(r['record'],tuple(d['edge'])):d for r in load('ramsey_37_switch_extension_catalogue')['report'] for d in r['deletions']};V=set(range(22));out=[]
# All two-color K_n (n<=5) with neither monochromatic triangle, by number of blue edges.
possible=defaultdict(set)
for n in range(6):
    edges=list(combinations(range(n),2));tri=[sum(1<<edges.index(e) for e in combinations(t,2)) for t in combinations(range(n),3)]
    for m in range(1<<len(edges)):
        if all(m&t not in (0,t) for t in tri):possible[n].add(m.bit_count())
for d in load('ramsey_37_switch_coverage_moments')['details']:
    if d['cert'][5] is not None:continue
    idx=d['record'];u,v=d['edge'];P={u,v};b=''.join(f'{ord(c)-63:06b}' for c in cat[idx-1][1:]);E={(i,j) for j in V for i in range(j) if b[j*(j-1)//2+i]=='1'};N=[{j for j in V if tuple(sorted((i,j))) in E} for i in V];W=V-P-N[u]-N[v];A=[frozenset()]
    for i in sorted(V-P):A += [s|{i} for s in A if not s&N[i]]
    F=[s for s in A if len(s)==6];bounds=[[999,999] for _ in range(3)];pockets=[]
    for S in A:
        if not S<=W or any(not N[i]&S for i in W-S):continue
        m=len(S);terms={frozenset(t):sum(set(t)<=h for h in F) for k in range(min(m,3)+1) for t in combinations(S,k)};base=sum((-1)**len(t)*c for t,c in terms.items());lo=hi=exact=0;pl=ph=0
        if m==4:
            hi=min(terms[t] for t in terms if len(t)==3)
            for t in terms:
                const=sum((-1)**(len(y)-len(t))*c for y,c in terms.items() if t<=y)
                if len(t)%2:hi=min(hi,const)
                else:lo=max(lo,-const)
            B=V-P-S-set.union(*(N[i] for i in S));assert len(B)<=5;exact=sum(y not in N[x] for x,y in combinations(B,2));opts={i for i in possible[len(B)] if lo<=i<=hi};assert exact in opts;pl=min(opts);ph=max(opts);pockets.append(len(B))
        for pair,(x,y) in zip(bounds,[(lo,hi),(pl,ph),(exact,exact)]):pair[0]=min(pair[0],base+x);pair[1]=min(pair[1],base+y)
    ref=reference[idx,(u,v)];assert bounds[2]==[ref['freshMin']]*2
    def sign(x):return -1 if x<d['base'] else 0 if x==d['base'] or d['oldOK'] else 1
    verdict=[sign(l) if sign(l)==sign(h) else None for l,h in bounds];assert verdict[-1]==(ref['after']>d['base'])-(ref['after']<d['base']);out.append(dict(record=idx,edge=[u,v],base=d['base'],oldOK=d['oldOK'],bounds=bounds,verdict=verdict,pocket_sizes=sorted(set(pockets))))
print(len(out),[sum(r['verdict'][k] is not None for r in out) for k in range(3)],dict(possible));print(next((r for r in out if r['verdict'][1] is None),out[0]));(D/'ramsey_37_switch_residual_pocket.json').write_text(json.dumps(out,indent=2)+'\n')
