"""Row redundancy from ALL strict supersets, independent of which global supports are proposed. A locally possible violation chooses b+1 independent traces on the one-vertex extensions E. Enumerate traces and test every nonempty independent subextension."""
from ramsey_integral_obstruction import D,json,attach,bits,Counter
from itertools import combinations,combinations_with_replacement
from functools import lru_cache

@lru_cache(None)
def possible(adj,b):
    I=[0]
    for v,r in enumerate(adj):I += [s|1<<v for s in I if not s&r]
    M=[s for s in I if all(s>>v&1 or s&r for v,r in enumerate(adj))];return any(all(sum(not(s&t) for s in q)<=b-t.bit_count() for t in I if t) for q in combinations_with_replacement(M,b+1))

def analyze(H,k):
    I=[0];F=(1<<len(H))-1
    for i,r in enumerate(H):I += [s|1<<i for s in I if not s&r]
    status={};hist=Counter();examples={}
    for s in I:
        b=k-1-s.bit_count()
        if b not in (2,3):continue
        E=F^s
        for v in bits(s):E&=~H[v]
        V=list(bits(E));adj=tuple(sum(1<<j for j,v in enumerate(V) if H[u]>>v&1) for u in V);ok=possible(adj,b);hist[(s.bit_count(),ok)]+=1;status[s]=(V,ok);examples.setdefault(str((s.bit_count(),ok)),s)
    return status,hist
if __name__=='__main__':
    p=json.loads((D/'ramsey_pure_port_fork.json').read_text());H=attach(p['stem_graphs'][-1],p['alternate']['to34']);status,h=analyze(H,10);out={'counts':{str(k):v for k,v in h.items()},'neighborhoods':{v:status[H[v]] for v in (2,22,16,9,23,3,7,33)}};print(out);(D/'ramsey_extension_row_filter.json').write_text(json.dumps(out)+'\n')
