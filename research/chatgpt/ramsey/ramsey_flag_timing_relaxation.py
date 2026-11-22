"""Relax the allowed source pairs, keeping observed support and both row directions fixed. Identify the effect on local prefixes and actual matching IDs."""
from ramsey_flag_selector_ablation import match,P,T,X,rho,D,json,permutations
from collections import Counter
from itertools import product

def run():
    E={''.join(e) for e in json.loads((D.parents[1]/'strominger/inputs/photon-shared-edge-seed.json').read_text())['arrows']};prefix=[(P.index(a),k,P.index(b)) for a in T[1] if a!=P[0] for k,t in enumerate(T,15) if k!=16 and a in t for b in t if b not in (P[0],a)];weights=Counter()
    for m in match():
        inv={rho[j]:rho[d] for d,j in m.items()};u=inv[16];weights[u,m[u],inv[m[u]]]+=1
    policies={'strict_turn':[(1,4),(4,3)],'chronological':[(i,j) for i,j in permutations(range(1,5),2) if i<j],'one_back':[(i,j) for i,j in permutations(range(1,5),2) if i<=j+1],'any_distinct':list(permutations(range(1,5),2)),'reuse':list(product(range(1,5),repeat=2))};out=[]
    for p in permutations('ABCD'):
        if {p[0],p[3]}!={'A','B'}:continue
        by={k:[] for k in policies};witness={}
        for q in prefix:
            u,_,v=q;fits=[]
            for col,ds in [(2,[0,u,u,v]),(3,[0,rho[u],rho[u],rho[v]])]:
                tail=p[col-1];head,={'C','D'}-{tail};(a,b),=[(a,b) for a,b in product(E,repeat=2) if a[0]==tail and a[1]==b[0] and b[1]==head];support=[{frozenset(p[i-1] for i in X[h]) for h in P[d]} for d in ds];fits.append({(i,j) for i,j in policies['reuse'] if frozenset(a) in support[i-1] and frozenset(b) in support[j-1]})
            for k,allowed in policies.items():
                if all(f.intersection(allowed) for f in fits):by[k].append(q)
            if q in by['any_distinct']:witness[str(q)]=[sorted(f.intersection(policies['any_distinct'])) for f in fits]
        out.append(dict(binding=''.join(p),counts={k:sum(weights[q] for q in qs) for k,qs in by.items()},prefixes=by,witnesses=witness))
    return out
if __name__=='__main__':
    out=run();print(out[0]);(D/'ramsey_flag_timing_relaxation.json').write_text(json.dumps(out)+'\n')
