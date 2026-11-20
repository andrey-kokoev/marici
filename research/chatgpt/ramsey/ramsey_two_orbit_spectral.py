"""Leave two reflection orbits out of record 174; exact real odd nullity."""
from collections import Counter
from functools import lru_cache
from itertools import combinations
from math import gcd
from pathlib import Path
from pauli_realization_audit import decode_graph6,triangle_free,independent_witness,encode_graph6

@lru_cache(None)
def odd(a):
    M=[[((r>>(2*j))&1)-((r>>(2*j+1))&1) for j in range(11)] for r in a[::2]];k=0
    for j in range(11):
        h=next((h for h in range(k,11) if M[h][j]),None)
        if h is None:continue
        M[k],M[h]=M[h],M[k]
        for i in range(k+1,11):
            if M[i][j]:
                row=[M[k][j]*x-M[i][j]*y for x,y in zip(M[i],M[k])];g=gcd(*row);M[i]=[v//g for v in row] if g>1 else row
        k+=1
    return 11-k

def flip(a,o):
    b=list(a)
    for i,j in o:b[i]^=1<<j;b[j]^=1<<i
    return tuple(b)

def main():
    a=tuple(decode_graph6((Path(__file__).parent/'pauli-realization-catalogues/r37_22.g6').read_text().splitlines()[173])); O=sorted({tuple(sorted({(i,j),tuple(sorted((i^1,j^1)))})) for i,j in combinations(range(22),2)}); old=[o for o in O if a[o[0][0]]>>o[0][1]&1];stats=Counter();score=Counter();first=Counter();alts=set();ex=None
    for cut in combinations(old,2):
        b=flip(flip(a,cut[0]),cut[1]);start=odd(b)
        if independent_witness(b,7) is None:stats['valid after cut']+=1;continue
        stats['damaged']+=1;cand=[o for o in O if not(b[o[0][0]]>>o[0][1]&1) and all(not(b[i]&b[j]) for i,j in o)];nalt=0;work=set();eligible=set()
        for x,y in combinations(cand,2):
            v=flip(flip(b,x),y)
            if not triangle_free(v):continue
            good=independent_witness(v,7) is None
            if v==a:assert good;continue
            eligible.update([x,y]);score[odd(v)-start,good]+=1
            if good:
                nalt+=1;work.update([x,y]);alts.add(v)
                if ex is None:ex=cut,(x,y),encode_graph6(v),sorted(t.bit_count() for t in v),odd(v)-start
        for x in eligible:first[odd(flip(b,x))-start,x in work]+=1
        stats['with alternative']+=bool(nalt)
    print(stats,'distinct alternate endpoints',len(alts),'endpoint',sorted(score.items()),'first',sorted(first.items()),'example',ex)
    import networkx as nx
    reps=[nx.from_graph6_bytes(encode_graph6(a).encode())];counts=Counter()
    for v in sorted(alts):
        g=nx.from_graph6_bytes(encode_graph6(v).encode());i=next((i for i,h in enumerate(reps) if nx.is_isomorphic(g,h)),len(reps))
        if i==len(reps):reps.append(g)
        counts[i]+=1
    print('unlabeled classes of alternatives',len(counts),'isomorphic to original',counts[0])
if __name__=='__main__':main()
