"""Exact connected-detour search. Enumerate independent subsets once per parent; after deleting D, reject a support exactly when an old independent six is missed. Supersets of minimal missed-hit constraints need no approximation."""
from pathlib import Path
from itertools import combinations
from collections import deque,Counter
import networkx as nx,json
D=Path(__file__).parent;ls=lambda s:[i for i in range(s.bit_length()) if s>>i&1]
def path(B,v,w,axes):
    pred={v:None};q=deque([v]);
    while q:
        x=q.popleft()
        if x==w:
            p=[]
            while x is not None:p.append(x);x=pred[x]
            return p[::-1]
        for i in axes:
            y=x^1<<i
            if y in B and y not in pred:pred[y]=x;q.append(y)
    return []
def run():
    ps=[];stats=Counter()
    for line in (D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines():
        g=nx.from_graph6_bytes(line);h=[sum(1<<j for j in g[i]) for i in range(22)];I=[0]
        for i,r in enumerate(h):I.extend([s|1<<i for s in I if not s&r]);
        T=[s for s in I if s.bit_count()==6];ps.append((I,T,h,{}))
    for size in (1,2):
        for rec,(I,T,h,cache) in enumerate(ps,1):
            # Precompute whether deleted sites hit every six missed by a given support.
            for deleted in combinations(range(22),size):
                mask=sum(1<<i for i in deleted);B=set();stats[f'cores_{size}']+=1
                for s in I:
                    if not s&mask:
                        if s not in cache:cache[s]=[t for t in T if not t&s]
                        if all(t&mask for t in cache[s]):B.add(s)
                if len(B)<2:continue
                M=sorted(s for s in B if not any((s^(1<<i)) in B for i in ls(s)))
                for v,w in combinations(M,2):
                    if v|w in B:continue
                    ax=ls(v^w);p=path(B,v,w,ax)
                    if p and len(p)-1==len(ax):continue
                    p=path(B,v,w,range(22));
                    if not p:stats['disconnected_pairs']+=1;continue
                    if len(p)-1==len(ax):continue
                    u=v|w;c=v&w;interval=sorted(s for s in B if s&c==c and not s&~u);changed=sorted({(a^b).bit_length()-1 for a,b in zip(p,p[1:])}-set(ax));return dict(stats=stats,record=rec,deleted=list(deleted),states=len(B),minimal=len(M),start=ls(v),target=ls(w),distance=len(p)-1,hamming=len(ax),shortest_path=list(map(ls,p)),extra_axes=changed,legal_interval=list(map(ls,interval)),other_fixed_paths=bool(path(B,v,w,ax)),cross_conflicts=[(a,b) for a in ls(v&~w) for b in ls(w&~v) if h[a]>>b&1],removal_certificates={i:ls(next(t for t in T if not t&mask and t&v==1<<i)) for i in ls(v&~w)})
    return dict(stats=stats)
if __name__=='__main__':
    r=run();print(r);(D/'ramsey_support_detour.json').write_text(json.dumps(r,indent=2)+'\n')
