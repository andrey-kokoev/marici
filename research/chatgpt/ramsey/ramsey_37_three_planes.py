"""Exhaust the adjacent three-plane pilot protocol."""
from itertools import combinations
from collections import Counter
from pathlib import Path
import networkx as nx,json
D=Path(__file__).parent

def run():
    best=Counter();base=Counter();improved=readable=pairs=0;example=None;peak=None;rec=[]
    for num,line in enumerate((D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines(),1):
        g=nx.from_graph6_bytes(line);assert len(g)==22;h=[sum(1<<i for i in g[v]) for v in range(22)];m=n=r=0
        for a,b in combinations(range(22),2):
            u,v=h[a],h[b];X=[i for i in range(22) if i not in (a,b)];ab=[(h[i]>>a&1,(h[i]&u).bit_count(),h[i]>>b&1,(h[i]&v).bit_count()) for i in X];t=[s+((h[i]&u&v).bit_count(),) for i,s in zip(X,ab)];p=len(set(ab));k=len(set(t));pairs+=1;improved+=k>p;n=max(n,p);m=max(m,k)
            if example is None and k>p:
                i,j=next((i,j) for i,j in combinations(range(20),2) if ab[i]==ab[j] and t[i]!=t[j]);example=dict(record=num,anchors=[a,b],sites=[X[i],X[j]],addresses=[t[i],t[j]])
            if peak is None or k>peak['distinct']:peak=dict(record=num,anchors=[a,b],distinct=k)
            # Non-singleton address classes can support a color table only if vertices in them are twins outside the pair.
            valid=all(not ((h[X[i]]^h[X[j]]) & ~((1<<a)|(1<<b)|(1<<X[i])|(1<<X[j]))) for i,j in combinations(range(20),2) if t[i]==t[j]);r+=valid
        readable+=r;best[m]+=1;base[n]+=1;rec.append([num,n,m,r]);
    return dict(anchor_pairs=pairs,improved_pairs=improved,edge_readable_pairs=readable,best_two=dict(base),best_three=dict(best),example=example,peak=peak,per_record=rec)
if __name__=='__main__':
    r=run();print({k:v for k,v in r.items() if k!='per_record'});Path(__file__).with_suffix('.json').write_text(json.dumps(r)+'\n')
