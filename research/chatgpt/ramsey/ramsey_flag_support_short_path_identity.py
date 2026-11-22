"""Compare exact sets of complete matchings; separately enumerate local simple prefixes, with no global matching assumption, to expose the mechanism."""
from ramsey_flag_selector_ablation import match,P,T,X,rho,D,json,permutations
from itertools import product

def passes(p,u,v,E):
    for col,ds in [(2,[0,u,u,v]),(3,[0,rho[u],rho[u],rho[v]])]:
        slots=[{e for e in E if any(set(e)=={p[x-1] for x in X[h]} for h in P[d])} for d in ds];a=p[col-1];b,={'C','D'}-{a}
        if not any(x[0]==a and x[1]==y[0] and y[1]==b for i,j in [(0,3),(3,2)] for x,y in product(slots[i],slots[j])):return False
    return True

def run():
    E={''.join(e) for e in json.loads((D.parents[1]/'strominger/inputs/photon-shared-edge-seed.json').read_text())['arrows']};prefixes=[(P.index(a),k,P.index(b)) for a in T[1] if a!=P[0] for k,t in enumerate(T,15) if k!=16 and a in t for b in t if b not in (P[0],a)];rows=[]
    for p in permutations('ABCD'):
        if {p[0],p[3]}!={'A','B'}:continue
        good=[q for q in prefixes if passes(p,q[0],q[2],E)];short=set();local=set();
        for m in match():
            inv={rho[j]:rho[d] for d,j in m.items()};u=inv[m[0]];v=inv[m[u]];key=tuple(m[i] for i in range(15));
            if m[v]==29:short.add(key)
            if passes(p,u,v,E):local.add(key)
        assert short==local and len(short)==13;rows.append(dict(binding=''.join(p),all_local_prefixes=prefixes,passing_prefixes=good,short_only=len(short-local),support_only=len(local-short),common=len(short)))
    return rows
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_flag_support_short_path_identity.json').write_text(json.dumps(out)+'\n')
